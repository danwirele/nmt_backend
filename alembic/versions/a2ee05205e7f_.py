"""empty message

Revision ID: a2ee05205e7f
Revises: 4b20a93db245
Create Date: 2025-01-02 15:14:06.420429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2ee05205e7f'
down_revision: Union[str, None] = '4b20a93db245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
