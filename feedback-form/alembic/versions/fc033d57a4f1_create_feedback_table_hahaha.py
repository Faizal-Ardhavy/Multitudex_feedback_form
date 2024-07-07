"""create feedback table hahaha

Revision ID: fc033d57a4f1
Revises: d5cd7404aa62
Create Date: 2024-07-07 02:46:47.341441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc033d57a4f1'
down_revision: Union[str, None] = 'd5cd7404aa62'
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
