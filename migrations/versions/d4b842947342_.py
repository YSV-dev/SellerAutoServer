"""empty message

Revision ID: d4b842947342
Revises: 12c3530035a6
Create Date: 2023-11-28 00:08:25.022993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b842947342'
down_revision = '12c3530035a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stores',
    sa.Column('store_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('shop_name', sa.String(length=50), nullable=True),
    sa.Column('addition_date', sa.DateTime(), nullable=True),
    sa.Column('api_key_hash', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=512), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('second_name', sa.String(length=150), nullable=True),
    sa.Column('middle_name', sa.String(length=150), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('last_login_date', sa.DateTime(), nullable=True),
    sa.Column('last_action_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('stores')
    # ### end Alembic commands ###