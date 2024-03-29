"""empty message

Revision ID: 2a856324f8b7
Revises: 6513964691d4
Create Date: 2019-12-15 18:57:25.505380

"""

# revision identifiers, used by Alembic.
revision = '2a856324f8b7'
down_revision = '6513964691d4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidate',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('alt_email', sa.String(length=100), nullable=True),
    sa.Column('alt_phone_no', sa.String(length=100), nullable=True),
    sa.Column('phone_no', sa.String(length=100), nullable=True),
    sa.Column('department', sa.String(length=100), nullable=True),
    sa.Column('designation', sa.String(length=100), nullable=True),
    sa.Column('profile_picture_url', sa.String(length=500), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('last_updated_date', sa.DateTime(), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=500), nullable=True),
    sa.Column('resume_url', sa.String(length=500), nullable=True),
    sa.Column('notice_period', sa.String(length=100), nullable=True),
    sa.Column('ctc', sa.String(length=100), nullable=True),
    sa.Column('expected_ctc', sa.String(length=100), nullable=True),
    sa.Column('having_other_offers', sa.String(length=100), nullable=True),
    sa.Column('notes', sa.String(length=500), nullable=True),
    sa.Column('last_updated_hr_id', sa.BigInteger(), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('github_url', sa.String(length=500), nullable=True),
    sa.Column('linkedIn_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candidate')
    # ### end Alembic commands ###
