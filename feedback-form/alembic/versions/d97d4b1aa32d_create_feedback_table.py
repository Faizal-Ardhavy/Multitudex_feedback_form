"""create feedback table

Revision ID: d97d4b1aa32d
Revises: 
Create Date: 2024-07-07 01:57:24.414873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd97d4b1aa32d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'feedback',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('score', sa.Integer(5), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('feedback')
