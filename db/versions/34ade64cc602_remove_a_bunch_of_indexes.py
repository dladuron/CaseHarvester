"""Remove a bunch of indexes

Revision ID: 34ade64cc602
Revises: 7427734c0fc2
Create Date: 2020-04-28 17:21:24.816441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34ade64cc602'
down_revision = '7427734c0fc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_cases_case_type', table_name='cases')
    op.drop_index('ix_cases_court', table_name='cases')
    op.drop_index('ix_cases_detail_loc', table_name='cases')
    op.drop_index('ix_cases_filing_date', table_name='cases')
    op.drop_index('ix_cases_filing_date_original', table_name='cases')
    op.drop_index('ix_cases_last_parse', table_name='cases')
    op.drop_index('ix_cases_last_scrape', table_name='cases')
    op.drop_index('ix_cases_parse_exempt', table_name='cases')
    op.drop_index('ix_cases_query_court', table_name='cases')
    op.drop_index('ix_cases_scrape_exempt', table_name='cases')
    op.drop_index('ix_cases_status', table_name='cases')
    op.drop_index('ix_cc_case_disposition', table_name='cc')
    op.drop_index('ix_cc_case_status', table_name='cc')
    op.drop_index('ix_cc_case_type', table_name='cc')
    op.drop_index('ix_cc_court_system', table_name='cc')
    op.drop_index('ix_cc_disposition_date', table_name='cc')
    op.drop_index('ix_cc_disposition_date_str', table_name='cc')
    op.drop_index('ix_cc_filing_date', table_name='cc')
    op.drop_index('ix_cc_filing_date_str', table_name='cc')
    op.drop_index('ix_cc_title', table_name='cc')
    op.drop_index('ix_dscivil_case_status', table_name='dscivil')
    op.drop_index('ix_dscivil_claim_type', table_name='dscivil')
    op.drop_index('ix_dscivil_court_system', table_name='dscivil')
    op.drop_index('ix_dscivil_district_code', table_name='dscivil')
    op.drop_index('ix_dscivil_filing_date', table_name='dscivil')
    op.drop_index('ix_dscivil_filing_date_str', table_name='dscivil')
    op.drop_index('ix_dscivil_location_code', table_name='dscivil')
    op.drop_index('ix_dscr_case_disposition', table_name='dscr')
    op.drop_index('ix_dscr_case_status', table_name='dscr')
    op.drop_index('ix_dscr_case_type', table_name='dscr')
    op.drop_index('ix_dscr_court_system', table_name='dscr')
    op.drop_index('ix_dscr_district_code', table_name='dscr')
    op.drop_index('ix_dscr_document_type', table_name='dscr')
    op.drop_index('ix_dscr_issued_date', table_name='dscr')
    op.drop_index('ix_dscr_issued_date_str', table_name='dscr')
    op.drop_index('ix_dscr_location_code', table_name='dscr')
    op.drop_index('ix_dscr_tracking_number', table_name='dscr')
    op.drop_index('ix_dsk8_case_status', table_name='dsk8')
    op.drop_index('ix_dsk8_complaint_number', table_name='dsk8')
    op.drop_index('ix_dsk8_court_system', table_name='dsk8')
    op.drop_index('ix_dsk8_district_case_number', table_name='dsk8')
    op.drop_index('ix_dsk8_filing_date', table_name='dsk8')
    op.drop_index('ix_dsk8_filing_date_str', table_name='dsk8')
    op.drop_index('ix_dsk8_incident_date', table_name='dsk8')
    op.drop_index('ix_dsk8_incident_date_str', table_name='dsk8')
    op.drop_index('ix_dsk8_status_date', table_name='dsk8')
    op.drop_index('ix_dsk8_status_date_str', table_name='dsk8')
    op.drop_index('ix_dsk8_tracking_number', table_name='dsk8')
    op.drop_index('ix_odycrim_case_status', table_name='odycrim')
    op.drop_index('ix_odycrim_case_title', table_name='odycrim')
    op.drop_index('ix_odycrim_case_type', table_name='odycrim')
    op.drop_index('ix_odycrim_court_system', table_name='odycrim')
    op.drop_index('ix_odycrim_filing_date', table_name='odycrim')
    op.drop_index('ix_odycrim_filing_date_str', table_name='odycrim')
    op.drop_index('ix_odycrim_location', table_name='odycrim')
    op.drop_index('ix_odycrim_tracking_numbers', table_name='odycrim')
    op.drop_index('ix_odytraf_agency_name', table_name='odytraf')
    op.drop_index('ix_odytraf_case_status', table_name='odytraf')
    op.drop_index('ix_odytraf_case_title', table_name='odytraf')
    op.drop_index('ix_odytraf_case_type', table_name='odytraf')
    op.drop_index('ix_odytraf_citation_number', table_name='odytraf')
    op.drop_index('ix_odytraf_court_system', table_name='odytraf')
    op.drop_index('ix_odytraf_filing_date', table_name='odytraf')
    op.drop_index('ix_odytraf_filing_date_str', table_name='odytraf')
    op.drop_index('ix_odytraf_location', table_name='odytraf')
    op.drop_index('ix_odytraf_officer_id', table_name='odytraf')
    op.drop_index('ix_odytraf_officer_name', table_name='odytraf')
    op.drop_index('ix_odytraf_violation_county', table_name='odytraf')
    op.drop_index('ix_odytraf_violation_date', table_name='odytraf')
    op.drop_index('ix_odytraf_violation_date_str', table_name='odytraf')
    op.drop_index('ix_odytraf_violation_time', table_name='odytraf')
    op.drop_index('ix_odytraf_violation_time_str', table_name='odytraf')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_odytraf_violation_time_str', 'odytraf', ['violation_time_str'], unique=False)
    op.create_index('ix_odytraf_violation_time', 'odytraf', ['violation_time'], unique=False)
    op.create_index('ix_odytraf_violation_date_str', 'odytraf', ['violation_date_str'], unique=False)
    op.create_index('ix_odytraf_violation_date', 'odytraf', ['violation_date'], unique=False)
    op.create_index('ix_odytraf_violation_county', 'odytraf', ['violation_county'], unique=False)
    op.create_index('ix_odytraf_officer_name', 'odytraf', ['officer_name'], unique=False)
    op.create_index('ix_odytraf_officer_id', 'odytraf', ['officer_id'], unique=False)
    op.create_index('ix_odytraf_location', 'odytraf', ['location'], unique=False)
    op.create_index('ix_odytraf_filing_date_str', 'odytraf', ['filing_date_str'], unique=False)
    op.create_index('ix_odytraf_filing_date', 'odytraf', ['filing_date'], unique=False)
    op.create_index('ix_odytraf_court_system', 'odytraf', ['court_system'], unique=False)
    op.create_index('ix_odytraf_citation_number', 'odytraf', ['citation_number'], unique=False)
    op.create_index('ix_odytraf_case_type', 'odytraf', ['case_type'], unique=False)
    op.create_index('ix_odytraf_case_title', 'odytraf', ['case_title'], unique=False)
    op.create_index('ix_odytraf_case_status', 'odytraf', ['case_status'], unique=False)
    op.create_index('ix_odytraf_agency_name', 'odytraf', ['agency_name'], unique=False)
    op.create_index('ix_odycrim_tracking_numbers', 'odycrim', ['tracking_numbers'], unique=False)
    op.create_index('ix_odycrim_location', 'odycrim', ['location'], unique=False)
    op.create_index('ix_odycrim_filing_date_str', 'odycrim', ['filing_date_str'], unique=False)
    op.create_index('ix_odycrim_filing_date', 'odycrim', ['filing_date'], unique=False)
    op.create_index('ix_odycrim_court_system', 'odycrim', ['court_system'], unique=False)
    op.create_index('ix_odycrim_case_type', 'odycrim', ['case_type'], unique=False)
    op.create_index('ix_odycrim_case_title', 'odycrim', ['case_title'], unique=False)
    op.create_index('ix_odycrim_case_status', 'odycrim', ['case_status'], unique=False)
    op.create_index('ix_dsk8_tracking_number', 'dsk8', ['tracking_number'], unique=False)
    op.create_index('ix_dsk8_status_date_str', 'dsk8', ['status_date_str'], unique=False)
    op.create_index('ix_dsk8_status_date', 'dsk8', ['status_date'], unique=False)
    op.create_index('ix_dsk8_incident_date_str', 'dsk8', ['incident_date_str'], unique=False)
    op.create_index('ix_dsk8_incident_date', 'dsk8', ['incident_date'], unique=False)
    op.create_index('ix_dsk8_filing_date_str', 'dsk8', ['filing_date_str'], unique=False)
    op.create_index('ix_dsk8_filing_date', 'dsk8', ['filing_date'], unique=False)
    op.create_index('ix_dsk8_district_case_number', 'dsk8', ['district_case_number'], unique=False)
    op.create_index('ix_dsk8_court_system', 'dsk8', ['court_system'], unique=False)
    op.create_index('ix_dsk8_complaint_number', 'dsk8', ['complaint_number'], unique=False)
    op.create_index('ix_dsk8_case_status', 'dsk8', ['case_status'], unique=False)
    op.create_index('ix_dscr_tracking_number', 'dscr', ['tracking_number'], unique=False)
    op.create_index('ix_dscr_location_code', 'dscr', ['location_code'], unique=False)
    op.create_index('ix_dscr_issued_date_str', 'dscr', ['issued_date_str'], unique=False)
    op.create_index('ix_dscr_issued_date', 'dscr', ['issued_date'], unique=False)
    op.create_index('ix_dscr_document_type', 'dscr', ['document_type'], unique=False)
    op.create_index('ix_dscr_district_code', 'dscr', ['district_code'], unique=False)
    op.create_index('ix_dscr_court_system', 'dscr', ['court_system'], unique=False)
    op.create_index('ix_dscr_case_type', 'dscr', ['case_type'], unique=False)
    op.create_index('ix_dscr_case_status', 'dscr', ['case_status'], unique=False)
    op.create_index('ix_dscr_case_disposition', 'dscr', ['case_disposition'], unique=False)
    op.create_index('ix_dscivil_location_code', 'dscivil', ['location_code'], unique=False)
    op.create_index('ix_dscivil_filing_date_str', 'dscivil', ['filing_date_str'], unique=False)
    op.create_index('ix_dscivil_filing_date', 'dscivil', ['filing_date'], unique=False)
    op.create_index('ix_dscivil_district_code', 'dscivil', ['district_code'], unique=False)
    op.create_index('ix_dscivil_court_system', 'dscivil', ['court_system'], unique=False)
    op.create_index('ix_dscivil_claim_type', 'dscivil', ['claim_type'], unique=False)
    op.create_index('ix_dscivil_case_status', 'dscivil', ['case_status'], unique=False)
    op.create_index('ix_cc_title', 'cc', ['title'], unique=False)
    op.create_index('ix_cc_filing_date_str', 'cc', ['filing_date_str'], unique=False)
    op.create_index('ix_cc_filing_date', 'cc', ['filing_date'], unique=False)
    op.create_index('ix_cc_disposition_date_str', 'cc', ['disposition_date_str'], unique=False)
    op.create_index('ix_cc_disposition_date', 'cc', ['disposition_date'], unique=False)
    op.create_index('ix_cc_court_system', 'cc', ['court_system'], unique=False)
    op.create_index('ix_cc_case_type', 'cc', ['case_type'], unique=False)
    op.create_index('ix_cc_case_status', 'cc', ['case_status'], unique=False)
    op.create_index('ix_cc_case_disposition', 'cc', ['case_disposition'], unique=False)
    op.create_index('ix_cases_status', 'cases', ['status'], unique=False)
    op.create_index('ix_cases_scrape_exempt', 'cases', ['scrape_exempt'], unique=False)
    op.create_index('ix_cases_query_court', 'cases', ['query_court'], unique=False)
    op.create_index('ix_cases_parse_exempt', 'cases', ['parse_exempt'], unique=False)
    op.create_index('ix_cases_last_scrape', 'cases', ['last_scrape'], unique=False)
    op.create_index('ix_cases_last_parse', 'cases', ['last_parse'], unique=False)
    op.create_index('ix_cases_filing_date_original', 'cases', ['filing_date_original'], unique=False)
    op.create_index('ix_cases_filing_date', 'cases', ['filing_date'], unique=False)
    op.create_index('ix_cases_detail_loc', 'cases', ['detail_loc'], unique=False)
    op.create_index('ix_cases_court', 'cases', ['court'], unique=False)
    op.create_index('ix_cases_case_type', 'cases', ['case_type'], unique=False)
    # ### end Alembic commands ###