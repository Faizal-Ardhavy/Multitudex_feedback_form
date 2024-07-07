"""buat tabel lagi lah bismillah

Revision ID: 48481c0e2490
Revises: 8492bab22201
Create Date: 2024-07-07 02:55:07.616438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48481c0e2490'
down_revision: Union[str, None] = '8492bab22201'
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