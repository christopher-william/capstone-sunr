"""db mockup relantionship

Revision ID: 2affaab090b9
Revises: 0a4586c6768b
Create Date: 2021-01-13 10:03:10.713961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2affaab090b9'
down_revision = '0a4586c6768b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('energy_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('simulation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lead',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('hsp_id', sa.Integer(), nullable=True),
    sa.Column('energy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['energy_id'], ['energy_data.id'], ),
    sa.ForeignKeyConstraint(['hsp_id'], ['hsp.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lead')
    op.drop_table('simulation')
    op.drop_table('energy_data')
    # ### end Alembic commands ###