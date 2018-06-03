"""add indexes to case subtables

Revision ID: aeac150f0048
Revises: b1dff9d12aba
Create Date: 2018-05-23 12:48:43.269100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aeac150f0048'
down_revision = 'b1dff9d12aba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_cc_attorneys_case_number'), 'cc_attorneys', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_court_schedule_case_number'), 'cc_court_schedule', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_defendants_case_number'), 'cc_defendants', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_district_case_numbers_case_number'), 'cc_district_case_numbers', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_documents_case_number'), 'cc_documents', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_judgment_modifications_case_number'), 'cc_judgment_modifications', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_judgments_case_number'), 'cc_judgments', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_judgments_against_case_number'), 'cc_judgments_against', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_judgments_in_favor_case_number'), 'cc_judgments_in_favor', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_party_addresses_case_number'), 'cc_party_addresses', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_party_alias_case_number'), 'cc_party_alias', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_plaintiffs_case_number'), 'cc_plaintiffs', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_related_persons_case_number'), 'cc_related_persons', ['case_number'], unique=False)
    op.create_index(op.f('ix_cc_support_orders_case_number'), 'cc_support_orders', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscivil_complaints_case_number'), 'dscivil_complaints', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscivil_events_case_number'), 'dscivil_events', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscivil_hearings_case_number'), 'dscivil_hearings', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscivil_judgments_case_number'), 'dscivil_judgments', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscivil_related_persons_case_number'), 'dscivil_related_persons', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscivil_trials_case_number'), 'dscivil_trials', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscr_charges_case_number'), 'dscr_charges', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscr_defendant_aliases_case_number'), 'dscr_defendant_aliases', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscr_defendants_case_number'), 'dscr_defendants', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscr_events_case_number'), 'dscr_events', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscr_related_persons_case_number'), 'dscr_related_persons', ['case_number'], unique=False)
    op.create_index(op.f('ix_dscr_trials_case_number'), 'dscr_trials', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_bail_and_bond_case_number'), 'dsk8_bail_and_bond', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_bondsman_case_number'), 'dsk8_bondsman', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_charges_case_number'), 'dsk8_charges', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_defendant_aliases_case_number'), 'dsk8_defendant_aliases', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_defendants_case_number'), 'dsk8_defendants', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_events_case_number'), 'dsk8_events', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_related_persons_case_number'), 'dsk8_related_persons', ['case_number'], unique=False)
    op.create_index(op.f('ix_dsk8_trials_case_number'), 'dsk8_trials', ['case_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dsk8_trials_case_number'), table_name='dsk8_trials')
    op.drop_index(op.f('ix_dsk8_related_persons_case_number'), table_name='dsk8_related_persons')
    op.drop_index(op.f('ix_dsk8_events_case_number'), table_name='dsk8_events')
    op.drop_index(op.f('ix_dsk8_defendants_case_number'), table_name='dsk8_defendants')
    op.drop_index(op.f('ix_dsk8_defendant_aliases_case_number'), table_name='dsk8_defendant_aliases')
    op.drop_index(op.f('ix_dsk8_charges_case_number'), table_name='dsk8_charges')
    op.drop_index(op.f('ix_dsk8_bondsman_case_number'), table_name='dsk8_bondsman')
    op.drop_index(op.f('ix_dsk8_bail_and_bond_case_number'), table_name='dsk8_bail_and_bond')
    op.drop_index(op.f('ix_dscr_trials_case_number'), table_name='dscr_trials')
    op.drop_index(op.f('ix_dscr_related_persons_case_number'), table_name='dscr_related_persons')
    op.drop_index(op.f('ix_dscr_events_case_number'), table_name='dscr_events')
    op.drop_index(op.f('ix_dscr_defendants_case_number'), table_name='dscr_defendants')
    op.drop_index(op.f('ix_dscr_defendant_aliases_case_number'), table_name='dscr_defendant_aliases')
    op.drop_index(op.f('ix_dscr_charges_case_number'), table_name='dscr_charges')
    op.drop_index(op.f('ix_dscivil_trials_case_number'), table_name='dscivil_trials')
    op.drop_index(op.f('ix_dscivil_related_persons_case_number'), table_name='dscivil_related_persons')
    op.drop_index(op.f('ix_dscivil_judgments_case_number'), table_name='dscivil_judgments')
    op.drop_index(op.f('ix_dscivil_hearings_case_number'), table_name='dscivil_hearings')
    op.drop_index(op.f('ix_dscivil_events_case_number'), table_name='dscivil_events')
    op.drop_index(op.f('ix_dscivil_complaints_case_number'), table_name='dscivil_complaints')
    op.drop_index(op.f('ix_cc_support_orders_case_number'), table_name='cc_support_orders')
    op.drop_index(op.f('ix_cc_related_persons_case_number'), table_name='cc_related_persons')
    op.drop_index(op.f('ix_cc_plaintiffs_case_number'), table_name='cc_plaintiffs')
    op.drop_index(op.f('ix_cc_party_alias_case_number'), table_name='cc_party_alias')
    op.drop_index(op.f('ix_cc_party_addresses_case_number'), table_name='cc_party_addresses')
    op.drop_index(op.f('ix_cc_judgments_in_favor_case_number'), table_name='cc_judgments_in_favor')
    op.drop_index(op.f('ix_cc_judgments_against_case_number'), table_name='cc_judgments_against')
    op.drop_index(op.f('ix_cc_judgments_case_number'), table_name='cc_judgments')
    op.drop_index(op.f('ix_cc_judgment_modifications_case_number'), table_name='cc_judgment_modifications')
    op.drop_index(op.f('ix_cc_documents_case_number'), table_name='cc_documents')
    op.drop_index(op.f('ix_cc_district_case_numbers_case_number'), table_name='cc_district_case_numbers')
    op.drop_index(op.f('ix_cc_defendants_case_number'), table_name='cc_defendants')
    op.drop_index(op.f('ix_cc_court_schedule_case_number'), table_name='cc_court_schedule')
    op.drop_index(op.f('ix_cc_attorneys_case_number'), table_name='cc_attorneys')
    # ### end Alembic commands ###