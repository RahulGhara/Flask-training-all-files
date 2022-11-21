"""add column

Revision ID: 7dbb69a61756
Revises: 67d2458c49a7
Create Date: 2022-11-09 18:24:39.797933

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7dbb69a61756'
down_revision = '67d2458c49a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('Student', sa.Column('school', sa.String(30)))


def downgrade() -> None:
    op.drop_column('Student', 'school')

