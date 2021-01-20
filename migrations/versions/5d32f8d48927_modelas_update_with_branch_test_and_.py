"""modelas update with branch test and calculate_roi

Revision ID: 5d32f8d48927
Revises: 525f490e0c2f
Create Date: 2021-01-20 09:04:45.172692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d32f8d48927'
down_revision = '525f490e0c2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('energy_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('month_energy', sa.Numeric(), nullable=False),
    sa.Column('month_value', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('seller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('lead',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
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
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('lead_id', sa.Integer(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lead_id'], ['lead.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('simulation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system_cost', sa.Numeric(), nullable=False),
    sa.Column('energy_cost', sa.Numeric(), nullable=False),
    sa.Column('worker_cost', sa.Numeric(), nullable=False),
    sa.Column('project_cost', sa.Numeric(), nullable=False),
    sa.Column('eletric_materials_cost', sa.Numeric(), nullable=False),
    sa.Column('maintanance_cost', sa.Numeric(), nullable=False),
    sa.Column('total_system_cost', sa.Numeric(), nullable=False),
    sa.Column('roi_years', sa.Numeric(), nullable=False),
    sa.Column('panel_quantity', sa.Numeric(), nullable=False),
    sa.Column('lead_id', sa.Integer(), nullable=True),
    sa.Column('panel_id', sa.Integer(), nullable=True),
    sa.Column('inversor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inversor_id'], ['inverter_price.id'], ),
    sa.ForeignKeyConstraint(['lead_id'], ['lead.id'], ),
    sa.ForeignKeyConstraint(['panel_id'], ['panel_price.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('simulation')
    op.drop_table('message')
    op.drop_table('lead')
    op.drop_table('seller')
    op.drop_table('panel_price')
    op.drop_table('inverter_price')
    op.drop_table('hsp')
    op.drop_table('energy_data')
    # ### end Alembic commands ###
