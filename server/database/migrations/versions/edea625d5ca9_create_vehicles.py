"""create vehicles

Revision ID: edea625d5ca9
Revises: d8e1e648e0fe
Create Date: 2025-04-29 02:59:01.546983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edea625d5ca9'
down_revision: Union[str, None] = 'd8e1e648e0fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
