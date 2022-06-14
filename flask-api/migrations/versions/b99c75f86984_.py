"""empty message

Revision ID: b99c75f86984
Revises: 
Create Date: 2022-06-14 01:18:34.359843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b99c75f86984'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Region',
    sa.Column('id_region', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id_region')
    )
    op.create_table('Usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.Column('primer_nombre', sa.String(length=250), nullable=False),
    sa.Column('segundo_nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=250), nullable=False),
    sa.Column('apellido_materno', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('descuento',
    sa.Column('id_descuento', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('porcentaje', sa.Float(precision=3), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_descuento')
    )
    op.create_table('descuento_producto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fecha_inicio', sa.Date(), nullable=False),
    sa.Column('fecha_termino', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=250), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('valor_venta', sa.Integer(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('descripcion', sa.String(length=250), nullable=True),
    sa.Column('imagen', sa.String(length=250), nullable=True),
    sa.Column('estado', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id_producto')
    )
    op.create_table('Comuna',
    sa.Column('id_comuna', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('Region_id_region', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Region_id_region'], ['Region.id_region'], ),
    sa.PrimaryKeyConstraint('id_comuna')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Comuna')
    op.drop_table('producto')
    op.drop_table('descuento_producto')
    op.drop_table('descuento')
    op.drop_table('Usuario')
    op.drop_table('Region')
    # ### end Alembic commands ###