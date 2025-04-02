"""empty message

Revision ID: bd43a8bebb9a
Revises: 1982f3ebd3c7
Create Date: 2025-01-02 15:16:22.158986

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd43a8bebb9a'
down_revision: Union[str, None] = '1982f3ebd3c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
