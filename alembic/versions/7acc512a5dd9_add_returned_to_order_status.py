"""add returned to order status

Revision ID: 7acc512a5dd9
Revises: b2c3d4e5f6a7
Create Date: 2026-10-27 20:58:48.823556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7acc512a5dd9'
down_revision: Union[str, Sequence[str], None] = 'b2c3d4e5f6a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TYPE orderstatus ADD VALUE 'RETURNED'")


def downgrade() -> None:
    """Downgrade schema."""
    pass
