"""create feedback table

Revision ID: d5cd7404aa62
Revises: 96cae1e355a3
Create Date: 2024-07-07 02:46:09.317516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5cd7404aa62'
down_revision: Union[str, None] = '96cae1e355a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
