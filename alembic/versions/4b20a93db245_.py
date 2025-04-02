"""empty message

Revision ID: 4b20a93db245
Revises: a40eafd4b5b4
Create Date: 2025-01-02 15:12:38.968821

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b20a93db245'
down_revision: Union[str, None] = 'a40eafd4b5b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
