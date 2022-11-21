"""create_person_address_table

Revision ID: 618329eb4e83
Revises: 7dbb69a61756
Create Date: 2022-11-14 17:19:52.739992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '618329eb4e83'
down_revision = None
# down_revision = '7dbb69a61756'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'person',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(30), nullable=False),
    )
    op.create_table(
        'address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(35), nullable=False),
        sa.Column('person_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(('person_id',), ['person.id', ], )
    )


def downgrade() -> None:
    op.drop_table('address')
    op.drop_table('person')

