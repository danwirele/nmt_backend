"""empty message

Revision ID: 59dd582dd156
Revises: 95aeea50337f
Create Date: 2025-01-25 15:32:37.052467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59dd582dd156'
down_revision: Union[str, None] = '95aeea50337f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
