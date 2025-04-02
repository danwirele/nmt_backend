"""empty message

Revision ID: 029b1fc7c967
Revises: 1d6a347daf88
Create Date: 2025-01-03 15:13:37.937424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '029b1fc7c967'
down_revision: Union[str, None] = '1d6a347daf88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
