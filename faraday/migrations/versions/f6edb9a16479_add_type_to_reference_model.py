"""add type to reference model

Revision ID: f6edb9a16479
Revises: 581121b181d8
Create Date: 2022-08-05 19:10:54.482312+00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f6edb9a16479'
down_revision = '581121b181d8'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE TYPE reference_types AS ENUM  ('exploit', 'patch', 'other')")
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reference', sa.Column('type', sa.Enum('exploit',
                                                         'patch',
                                                         'other',
                                                         name='reference_types'), default='other', nullable=True))
    op.execute("UPDATE reference set type='other'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reference', 'type')
    op.execute("DROP TYPE reference_types")
    # ### end Alembic commands ###