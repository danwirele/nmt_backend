"""empty message

Revision ID: 1d6a347daf88
Revises: bbf37abb7644
Create Date: 2025-01-03 15:13:11.777269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d6a347daf88'
down_revision: Union[str, None] = 'bbf37abb7644'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
