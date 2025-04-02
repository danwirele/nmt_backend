"""empty message

Revision ID: 8ef6816848dd
Revises: bd43a8bebb9a
Create Date: 2025-01-02 15:17:06.744758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ef6816848dd'
down_revision: Union[str, None] = 'bd43a8bebb9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
