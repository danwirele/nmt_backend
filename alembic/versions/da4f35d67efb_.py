"""empty message

Revision ID: da4f35d67efb
Revises: a8090201e973
Create Date: 2024-12-11 01:38:02.153480

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da4f35d67efb'
down_revision: Union[str, None] = 'a8090201e973'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
