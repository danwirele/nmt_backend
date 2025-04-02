"""empty message

Revision ID: ebcf4237166f
Revises: da4f35d67efb
Create Date: 2024-12-17 20:06:12.236250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ebcf4237166f'
down_revision: Union[str, None] = 'da4f35d67efb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
