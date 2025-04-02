"""empty message

Revision ID: a40eafd4b5b4
Revises: 74b1801a7dbf
Create Date: 2024-12-17 20:58:42.776505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a40eafd4b5b4'
down_revision: Union[str, None] = '74b1801a7dbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
