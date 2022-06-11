"""empty message

Revision ID: 3ad7c2d1b3e3
Revises: 52c3be9fddaf
Create Date: 2022-06-10 18:54:02.662331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ad7c2d1b3e3'
down_revision = '52c3be9fddaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('descuento',
    sa.Column('id_descuento', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('porcentaje', sa.Float(precision=3), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_descuento')
    )
    op.create_table('Producto',
    sa.Column('id_producto', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('codigo', sa.String(length=250), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('valor_venta', sa.Integer(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('descripcion', sa.String(length=250), nullable=True),
    sa.Column('imagen', sa.String(length=250), nullable=True),
    sa.Column('estado', sa.String(length=1), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('descuento_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['descuento_id'], ['descuento.id_descuento'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['descuento_producto.producto_id'], ),
    sa.PrimaryKeyConstraint('id_producto')
    )
    op.drop_table('Descuento')
    op.drop_constraint(None, 'descuento_producto', type_='foreignkey')
    op.create_foreign_key(None, 'descuento_producto', 'descuento', ['descuento_id'], ['id_descuento'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'descuento_producto', type_='foreignkey')
    op.create_foreign_key(None, 'descuento_producto', 'Descuento', ['descuento_id'], ['id_descuento'])
    op.create_table('Descuento',
    sa.Column('id_descuento', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=250), nullable=False),
    sa.Column('fecha', sa.DATE(), nullable=True),
    sa.Column('porcentaje', sa.FLOAT(), nullable=False),
    sa.Column('estado', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id_descuento')
    )
    op.drop_table('Producto')
    op.drop_table('descuento')
    # ### end Alembic commands ###
