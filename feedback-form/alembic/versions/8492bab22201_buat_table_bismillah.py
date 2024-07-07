"""buat table bismillah

Revision ID: 8492bab22201
Revises: fc033d57a4f1
Create Date: 2024-07-07 02:48:53.097418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8492bab22201'
down_revision: Union[str, None] = 'fc033d57a4f1'
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
