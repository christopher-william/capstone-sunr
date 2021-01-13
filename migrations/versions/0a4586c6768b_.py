"""empty message

Revision ID: 0a4586c6768b
Revises: 
Create Date: 2021-01-12 21:07:21.791470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a4586c6768b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hsp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=80), nullable=False),
    sa.Column('uf', sa.String(length=120), nullable=False),
    sa.Column('md_anual', sa.Integer(), nullable=False),
    sa.Column('lon', sa.Numeric(), nullable=False),
    sa.Column('lat', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inverter_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('panel_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('panel_price')
    op.drop_table('inverter_price')
    op.drop_table('hsp')
    # ### end Alembic commands ###
