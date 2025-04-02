"""empty message

Revision ID: 74b1801a7dbf
Revises: f3677f61d9d7
Create Date: 2024-12-17 20:58:41.698889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74b1801a7dbf'
down_revision: Union[str, None] = 'f3677f61d9d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
