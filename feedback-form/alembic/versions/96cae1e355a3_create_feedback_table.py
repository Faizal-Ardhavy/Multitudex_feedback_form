"""create feedback table

Revision ID: 96cae1e355a3
Revises: d97d4b1aa32d
Create Date: 2024-07-07 01:59:30.643336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96cae1e355a3'
down_revision: Union[str, None] = 'd97d4b1aa32d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'feedback',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('score', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('feedback')
