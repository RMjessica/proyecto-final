"""empty message

Revision ID: a3c42c042437
Revises: 
Create Date: 2022-08-10 14:42:37.777917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3c42c042437'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('artista', sa.Boolean(), nullable=False),
    sa.Column('nacimiento', sa.String(length=10), nullable=True),
    sa.Column('foto_usuario', sa.String(length=500), nullable=True),
    sa.Column('descripcion', sa.String(length=3000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('direccion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tipo_via', sa.String(length=20), nullable=False),
    sa.Column('nombre_via', sa.String(length=20), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('piso', sa.Integer(), nullable=True),
    sa.Column('puerta', sa.String(length=5), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fecha_pedido', sa.String(length=10), nullable=False),
    sa.Column('historico', sa.Boolean(), nullable=False),
    sa.Column('id_comprador', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_comprador'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('fecha_alta', sa.String(length=10), nullable=False),
    sa.Column('categoria', sa.String(length=20), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('vendido', sa.Boolean(), nullable=False),
    sa.Column('foto_producto', sa.String(length=500), nullable=False),
    sa.Column('dimensiones', sa.String(length=10), nullable=False),
    sa.Column('descripcion', sa.String(length=3000), nullable=False),
    sa.Column('vendedor_user_id', sa.Integer(), nullable=False),
    sa.Column('pedido_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedido.id'], ),
    sa.ForeignKeyConstraint(['vendedor_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cesta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cesta')
    op.drop_table('producto')
    op.drop_table('pedido')
    op.drop_table('direccion')
    op.drop_table('user')
    # ### end Alembic commands ###
