"""empty message

Revision ID: 63d2b0236707
Revises: a2ee05205e7f
Create Date: 2025-01-02 15:15:28.626113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63d2b0236707'
down_revision: Union[str, None] = 'a2ee05205e7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
