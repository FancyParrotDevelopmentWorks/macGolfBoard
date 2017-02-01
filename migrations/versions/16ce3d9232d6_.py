"""empty message

Revision ID: 16ce3d9232d6
Revises: 6727e2b43794
Create Date: 2017-01-31 22:58:35.230537

"""

# revision identifiers, used by Alembic.
revision = '16ce3d9232d6'
down_revision = '6727e2b43794'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('avatar', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.add_column('users', sa.Column('tokens', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'tokens')
    op.drop_column('users', 'email')
    op.drop_column('users', 'avatar')
    op.drop_column('users', 'active')
    # ### end Alembic commands ###
