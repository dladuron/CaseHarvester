"""Add ODYTRAF models

Revision ID: 795bdb9f58e3
Revises: c72ff2a44e3d
Create Date: 2019-04-10 18:18:05.341892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '795bdb9f58e3'
down_revision = 'c72ff2a44e3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('odytraf',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('court_system', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('citation_number', sa.String(), nullable=True),
    sa.Column('case_title', sa.String(), nullable=True),
    sa.Column('case_type', sa.String(), nullable=True),
    sa.Column('filing_date', sa.Date(), nullable=True),
    sa.Column('filing_date_str', sa.String(), nullable=True),
    sa.Column('violation_date', sa.Date(), nullable=True),
    sa.Column('violation_date_str', sa.String(), nullable=True),
    sa.Column('violation_time', sa.Time(), nullable=True),
    sa.Column('violation_time_str', sa.String(), nullable=True),
    sa.Column('violation_county', sa.String(), nullable=True),
    sa.Column('agency_name', sa.String(), nullable=True),
    sa.Column('officer_id', sa.String(), nullable=True),
    sa.Column('officer_name', sa.String(), nullable=True),
    sa.Column('case_status', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cases.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_case_number'), 'odytraf', ['case_number'], unique=True)
    op.create_table('odytraf_bond_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bail_date', sa.Date(), nullable=True),
    sa.Column('bail_date_str', sa.String(), nullable=True),
    sa.Column('bail_setting_type', sa.String(), nullable=True),
    sa.Column('bail_amount', sa.Numeric(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_bond_settings_case_number'), 'odytraf_bond_settings', ['case_number'], unique=False)
    op.create_table('odytraf_bondsmen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_bondsmen_case_number'), 'odytraf_bondsmen', ['case_number'], unique=False)
    op.create_table('odytraf_charges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charge_number', sa.Integer(), nullable=True),
    sa.Column('charge_description', sa.String(), nullable=True),
    sa.Column('statute_code', sa.String(), nullable=True),
    sa.Column('speed_limit', sa.Integer(), nullable=True),
    sa.Column('recorded_speed', sa.Integer(), nullable=True),
    sa.Column('location_stopped', sa.String(), nullable=True),
    sa.Column('probable_cause_indicator', sa.Boolean(), nullable=True),
    sa.Column('charge_contributed_to_accident', sa.Boolean(), nullable=True),
    sa.Column('charge_personal_injury', sa.Boolean(), nullable=True),
    sa.Column('property_damage', sa.Boolean(), nullable=True),
    sa.Column('seat_belts', sa.Boolean(), nullable=True),
    sa.Column('mandatory_court_appearance', sa.Boolean(), nullable=True),
    sa.Column('fine_amount_owed', sa.Numeric(), nullable=True),
    sa.Column('vehicle_tag', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('vehicle_description', sa.String(), nullable=True),
    sa.Column('convicted_speed', sa.Integer(), nullable=True),
    sa.Column('disposition_contributed_to_accident', sa.Boolean(), nullable=True),
    sa.Column('disposition_personal_injury', sa.Boolean(), nullable=True),
    sa.Column('plea', sa.String(), nullable=True),
    sa.Column('plea_date', sa.Date(), nullable=True),
    sa.Column('plea_date_str', sa.String(), nullable=True),
    sa.Column('disposition', sa.String(), nullable=True),
    sa.Column('disposition_date', sa.Date(), nullable=True),
    sa.Column('disposition_date_str', sa.String(), nullable=True),
    sa.Column('converted_disposition', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_charges_case_number'), 'odytraf_charges', ['case_number'], unique=False)
    op.create_table('odytraf_court_schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_type', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('date_str', sa.String(), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.Column('time_str', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('room', sa.String(), nullable=True),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_court_schedule_case_number'), 'odytraf_court_schedule', ['case_number'], unique=False)
    op.create_table('odytraf_defendant_aliases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alias', sa.String(), nullable=False),
    sa.Column('alias_type', sa.String(), nullable=False),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_defendant_aliases_case_number'), 'odytraf_defendant_aliases', ['case_number'], unique=False)
    op.create_table('odytraf_defendants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('race', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('DOB', sa.Date(), nullable=True),
    sa.Column('DOB_str', sa.String(), nullable=True),
    sa.Column('address_1', sa.String(), nullable=True),
    sa.Column('address_2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('height', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_defendants_case_number'), 'odytraf_defendants', ['case_number'], unique=False)
    op.create_table('odytraf_documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_date', sa.Date(), nullable=True),
    sa.Column('file_date_str', sa.String(), nullable=True),
    sa.Column('filed_by', sa.String(), nullable=True),
    sa.Column('document_name', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_documents_case_number'), 'odytraf_documents', ['case_number'], unique=False)
    op.create_table('odytraf_interpreters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_interpreters_case_number'), 'odytraf_interpreters', ['case_number'], unique=False)
    op.create_table('odytraf_officers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('agency_name', sa.String(), nullable=False),
    sa.Column('address_1', sa.String(), nullable=True),
    sa.Column('address_2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_officers_case_number'), 'odytraf_officers', ['case_number'], unique=False)
    op.create_table('odytraf_plaintiffs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_plaintiffs_case_number'), 'odytraf_plaintiffs', ['case_number'], unique=False)
    op.create_table('odytraf_probation_officers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_probation_officers_case_number'), 'odytraf_probation_officers', ['case_number'], unique=False)
    op.create_table('odytraf_reference_numbers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ref_num', sa.String(), nullable=False),
    sa.Column('ref_num_type', sa.String(), nullable=False),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_reference_numbers_case_number'), 'odytraf_reference_numbers', ['case_number'], unique=False)
    op.create_table('odytraf_sureties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_sureties_case_number'), 'odytraf_sureties', ['case_number'], unique=False)
    op.create_table('odytraf_warrants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('warrant_type', sa.String(), nullable=True),
    sa.Column('issue_date', sa.Date(), nullable=True),
    sa.Column('issue_date_str', sa.String(), nullable=True),
    sa.Column('last_status', sa.String(), nullable=True),
    sa.Column('status_date', sa.Date(), nullable=True),
    sa.Column('status_date_str', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_warrants_case_number'), 'odytraf_warrants', ['case_number'], unique=False)
    op.create_table('odytraf_attorneys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plaintiff_id', sa.Integer(), nullable=True),
    sa.Column('defendant_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address_1', sa.String(), nullable=True),
    sa.Column('address_2', sa.String(), nullable=True),
    sa.Column('address_3', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['defendant_id'], ['odytraf_defendants.id'], ),
    sa.ForeignKeyConstraint(['plaintiff_id'], ['odytraf_plaintiffs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_attorneys_case_number'), 'odytraf_attorneys', ['case_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_odytraf_attorneys_case_number'), table_name='odytraf_attorneys')
    op.drop_table('odytraf_attorneys')
    op.drop_index(op.f('ix_odytraf_warrants_case_number'), table_name='odytraf_warrants')
    op.drop_table('odytraf_warrants')
    op.drop_index(op.f('ix_odytraf_sureties_case_number'), table_name='odytraf_sureties')
    op.drop_table('odytraf_sureties')
    op.drop_index(op.f('ix_odytraf_reference_numbers_case_number'), table_name='odytraf_reference_numbers')
    op.drop_table('odytraf_reference_numbers')
    op.drop_index(op.f('ix_odytraf_probation_officers_case_number'), table_name='odytraf_probation_officers')
    op.drop_table('odytraf_probation_officers')
    op.drop_index(op.f('ix_odytraf_plaintiffs_case_number'), table_name='odytraf_plaintiffs')
    op.drop_table('odytraf_plaintiffs')
    op.drop_index(op.f('ix_odytraf_officers_case_number'), table_name='odytraf_officers')
    op.drop_table('odytraf_officers')
    op.drop_index(op.f('ix_odytraf_interpreters_case_number'), table_name='odytraf_interpreters')
    op.drop_table('odytraf_interpreters')
    op.drop_index(op.f('ix_odytraf_documents_case_number'), table_name='odytraf_documents')
    op.drop_table('odytraf_documents')
    op.drop_index(op.f('ix_odytraf_defendants_case_number'), table_name='odytraf_defendants')
    op.drop_table('odytraf_defendants')
    op.drop_index(op.f('ix_odytraf_defendant_aliases_case_number'), table_name='odytraf_defendant_aliases')
    op.drop_table('odytraf_defendant_aliases')
    op.drop_index(op.f('ix_odytraf_court_schedule_case_number'), table_name='odytraf_court_schedule')
    op.drop_table('odytraf_court_schedule')
    op.drop_index(op.f('ix_odytraf_charges_case_number'), table_name='odytraf_charges')
    op.drop_table('odytraf_charges')
    op.drop_index(op.f('ix_odytraf_bondsmen_case_number'), table_name='odytraf_bondsmen')
    op.drop_table('odytraf_bondsmen')
    op.drop_index(op.f('ix_odytraf_bond_settings_case_number'), table_name='odytraf_bond_settings')
    op.drop_table('odytraf_bond_settings')
    op.drop_index(op.f('ix_odytraf_case_number'), table_name='odytraf')
    op.drop_table('odytraf')
    # ### end Alembic commands ###