"""Add advanced notifs to model

Revision ID: f7ca45632cce
Revises: 61ded0c8fbf6
Create Date: 2023-08-07 21:32:24.180236+00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f7ca45632cce'
down_revision = '51e533d41312'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_notification_settings', sa.Column('adv_high_crit_vuln_enabled', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_high_crit_vuln_app', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_high_crit_vuln_email', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_high_crit_vuln_slack', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_risk_score_threshold_enabled', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_risk_score_threshold_app', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_risk_score_threshold_email', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_risk_score_threshold_slack', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_vuln_open_days_enabled', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_vuln_open_days_app', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_vuln_open_days_email', sa.Boolean(), default=False, server_default=sa.text('false')))
    op.add_column('user_notification_settings', sa.Column('adv_vuln_open_days_slack', sa.Boolean(), default=False, server_default=sa.text('false')))

    op.create_table('email_notification',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_email', sa.String(), nullable=False),
                    sa.Column('message', sa.String(), nullable=False),
                    sa.Column('processed', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('slack_notification',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('slack_id', sa.String(), nullable=False),
                    sa.Column('message', sa.String(), nullable=False),
                    sa.Column('processed', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('slack_notification')
    op.drop_table('email_notification')

    op.drop_column('user_notification_settings', 'adv_vuln_open_days_slack')
    op.drop_column('user_notification_settings', 'adv_vuln_open_days_email')
    op.drop_column('user_notification_settings', 'adv_vuln_open_days_app')
    op.drop_column('user_notification_settings', 'adv_vuln_open_days_enabled')
    op.drop_column('user_notification_settings', 'adv_risk_score_threshold_slack')
    op.drop_column('user_notification_settings', 'adv_risk_score_threshold_email')
    op.drop_column('user_notification_settings', 'adv_risk_score_threshold_app')
    op.drop_column('user_notification_settings', 'adv_risk_score_threshold_enabled')
    op.drop_column('user_notification_settings', 'adv_high_crit_vuln_slack')
    op.drop_column('user_notification_settings', 'adv_high_crit_vuln_email')
    op.drop_column('user_notification_settings', 'adv_high_crit_vuln_app')
    op.drop_column('user_notification_settings', 'adv_high_crit_vuln_enabled')
    # ### end Alembic commands ###
