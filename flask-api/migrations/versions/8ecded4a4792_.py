"""empty message

Revision ID: 8ecded4a4792
Revises: 
Create Date: 2022-06-09 01:03:52.702231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ecded4a4792'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('primer_nombre', sa.String(length=250), nullable=False),
    sa.Column('segundo_nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=250), nullable=False),
    sa.Column('apellido_materno', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Usuario')
    # ### end Alembic commands ###
