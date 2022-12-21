"""empty message

Revision ID: 9fcdd35613a6
Revises: 
Create Date: 2022-12-20 18:05:35.486270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fcdd35613a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=25), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=25), nullable=False),
    sa.Column('username', sa.VARCHAR(length=40), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.Column('hashed_password', sa.TEXT(), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('gender', sa.TEXT(), nullable=True),
    sa.Column('profile_picture_url', sa.TEXT(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
