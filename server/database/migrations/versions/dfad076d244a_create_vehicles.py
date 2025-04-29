"""create vehicles

Revision ID: dfad076d244a
Revises: edea625d5ca9
Create Date: 2025-04-29 03:06:24.670187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfad076d244a'
down_revision: Union[str, None] = 'edea625d5ca9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
