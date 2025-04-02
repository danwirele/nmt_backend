"""empty message

Revision ID: 95aeea50337f
Revises: 029b1fc7c967
Create Date: 2025-01-25 15:17:53.154889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95aeea50337f'
down_revision: Union[str, None] = '029b1fc7c967'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
