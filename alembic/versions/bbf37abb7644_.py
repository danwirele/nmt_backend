"""empty message

Revision ID: bbf37abb7644
Revises: 622ad9c58697
Create Date: 2025-01-03 00:12:53.956326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbf37abb7644'
down_revision: Union[str, None] = '622ad9c58697'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
