"""empty message

Revision ID: f3677f61d9d7
Revises: ebcf4237166f
Create Date: 2024-12-17 20:52:03.586296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3677f61d9d7'
down_revision: Union[str, None] = 'ebcf4237166f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
