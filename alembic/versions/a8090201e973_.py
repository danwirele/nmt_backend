"""empty message

Revision ID: a8090201e973
Revises: 97b36308a40d
Create Date: 2024-12-11 01:14:02.787148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8090201e973'
down_revision: Union[str, None] = '97b36308a40d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
