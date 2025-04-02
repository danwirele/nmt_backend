"""empty message

Revision ID: 622ad9c58697
Revises: 8ef6816848dd
Create Date: 2025-01-03 00:12:38.399960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '622ad9c58697'
down_revision: Union[str, None] = '8ef6816848dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
