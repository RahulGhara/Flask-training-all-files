"""create account table

Revision ID: 67d2458c49a7
Revises: 
Create Date: 2022-11-08 17:25:11.135216

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '67d2458c49a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'Student',
        sa.Column('roll_no', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('class', sa.Integer),
        sa.Column('section', sa.String(40)),
    )


def downgrade() -> None:
    op.drop_table('Student')
