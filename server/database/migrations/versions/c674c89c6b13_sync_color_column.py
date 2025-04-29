"""sync color column

Revision ID: c674c89c6b13
Revises: dfad076d244a
Create Date: 2025-04-29 03:08:11.933598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c674c89c6b13'
down_revision: Union[str, None] = 'dfad076d244a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
