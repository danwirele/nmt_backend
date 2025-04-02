"""empty message

Revision ID: 1982f3ebd3c7
Revises: 63d2b0236707
Create Date: 2025-01-02 15:15:42.302144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1982f3ebd3c7'
down_revision: Union[str, None] = '63d2b0236707'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
