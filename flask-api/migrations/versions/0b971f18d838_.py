"""empty message

Revision ID: 0b971f18d838
Revises: b15da3065faa
Create Date: 2022-06-15 20:24:18.720680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b971f18d838'
down_revision = 'b15da3065faa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'despacho', 'Comuna', ['comuna_id'], ['id_comuna'])
    op.add_column('detalle', sa.Column('venta_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'detalle', 'venta', ['venta_id'], ['id_venta'])
    op.create_foreign_key(None, 'detalle', 'producto', ['producto_id'], ['id_producto'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'detalle', type_='foreignkey')
    op.drop_constraint(None, 'detalle', type_='foreignkey')
    op.drop_column('detalle', 'venta_id')
    op.drop_constraint(None, 'despacho', type_='foreignkey')
    # ### end Alembic commands ###