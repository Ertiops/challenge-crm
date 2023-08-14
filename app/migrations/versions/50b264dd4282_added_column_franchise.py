"""Added column franchise

Revision ID: 50b264dd4282
Revises: 53a0ac109545
Create Date: 2023-08-08 13:29:15.372652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50b264dd4282'
down_revision: Union[str, None] = '53a0ac109545'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('franchise', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'franchise')
    # ### end Alembic commands ###