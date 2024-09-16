"""Added Concerts_table modal

Revision ID: 5251a5996204
Revises: af288a160b07
Create Date: 2024-09-16 22:45:30.028800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5251a5996204'
down_revision: Union[str, None] = 'af288a160b07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'concerts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('band_id', sa.Integer(), sa.ForeignKey('bands.id')),
        sa.Column('venue_id', sa.Integer(), sa.ForeignKey('venues.id')),
        sa.Column('concert_date', sa.Date())
    )

def downgrade() -> None:
    op.drop_table('concerts')

