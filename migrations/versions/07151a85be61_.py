"""empty message

Revision ID: 07151a85be61
Revises: None
Create Date: 2017-01-07 02:40:02.208920

"""

# revision identifiers, used by Alembic.
revision = '07151a85be61'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('club__members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('club_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clubs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('home_course_id', sa.Integer(), nullable=True),
    sa.Column('num_members', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('address1', sa.String(), nullable=True),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('province', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('group_type', sa.String(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('tee_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('parent_group_id', sa.Integer(), nullable=True),
    sa.Column('max_players', sa.Integer(), nullable=True),
    sa.Column('num_players', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('holes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('tee_id', sa.Integer(), nullable=True),
    sa.Column('par', sa.Integer(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rounds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('tee_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('par', sa.Integer(), nullable=True),
    sa.Column('index', sa.Float(), nullable=True),
    sa.Column('slope', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_update_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('can_text', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('tees')
    op.drop_table('rounds')
    op.drop_table('holes')
    op.drop_table('groups')
    op.drop_table('courses')
    op.drop_table('clubs')
    op.drop_table('club__members')
    # ### end Alembic commands ###
