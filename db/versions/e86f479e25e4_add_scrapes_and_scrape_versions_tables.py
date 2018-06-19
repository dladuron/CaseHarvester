"""add scrapes and scrape_versions tables

Revision ID: e86f479e25e4
Revises: c6965a9b34fe
Create Date: 2018-06-19 15:52:19.920577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e86f479e25e4'
down_revision = 'c6965a9b34fe'
branch_labels = None
depends_on = None

from sqlalchemy.orm import sessionmaker
from mjcs.models import Scrape, ScrapeVersion, Case
from mjcs.config import config
from datetime import *
from hashlib import sha256

def upgrade():
    print('Running Alembic commands')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scrape_versions',
    sa.Column('s3_version_id', sa.String(), nullable=False),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('sha256', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cases.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('s3_version_id')
    )
    op.create_index(op.f('ix_scrape_versions_case_number'), 'scrape_versions', ['case_number'], unique=False)
    op.create_table('scrapes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.Column('s3_version_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cases.case_number'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['s3_version_id'], ['scrape_versions.s3_version_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_scrape_timestamp', 'scrapes', ['case_number', sa.text('timestamp DESC')], unique=False)
    op.create_index(op.f('ix_scrapes_case_number'), 'scrapes', ['case_number'], unique=False)
    # ### end Alembic commands ###
    if 0: # no need to do this for dev
        print('Running migration')
        connection = op.get_bind()
        db_factory = sessionmaker(bind = connection)
        db = db_factory()
        try:
            total_cases = db.query(Case).filter(Case.last_scrape.isnot(None)).count()
            i = 0
            for version in config.case_details_bucket.object_versions.all():
                i += 1
                print('Adding version %s for case_number %s (%d of %d)' % (version.id, version.object_key, i, total_cases))
                try:
                    obj = version.get()
                except:
                    print('ERROR')
                    continue
                html = obj['Body'].read()
                timestamp = datetime.strptime(obj['Metadata']['timestamp'], "%Y-%m-%dT%H:%M:%S.%f")
                scrape_version = ScrapeVersion(
                    s3_version_id = version.id,
                    case_number = version.object_key,
                    length = len(html),
                    sha256 = sha256(html).hexdigest()
                )
                scrape = Scrape(
                    case_number = version.object_key,
                    s3_version_id = version.id,
                    timestamp = timestamp,
                    duration = None
                )
                db.add(scrape_version)
                db.add(scrape)
            db.commit()
        except:
            db.rollback()
            raise
        finally:
            db.close()
    print('Finished!')

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_scrapes_case_number'), table_name='scrapes')
    op.drop_index('ix_scrape_timestamp', table_name='scrapes')
    op.drop_table('scrapes')
    op.drop_index(op.f('ix_scrape_versions_case_number'), table_name='scrape_versions')
    op.drop_table('scrape_versions')
    # ### end Alembic commands ###
