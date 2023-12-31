"""empty message

Revision ID: 767ea1a28db2
Revises: 1dfc5a6e512b
Create Date: 2023-08-31 12:25:11.866557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '767ea1a28db2'
down_revision: Union[str, None] = '1dfc5a6e512b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('owners', sa.Column('phone', sa.String(length=11), nullable=False))
    op.drop_column('owners', 'franchise')
    op.add_column('users', sa.Column('phone', sa.String(length=11), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone')
    op.add_column('owners', sa.Column('franchise', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
    op.drop_column('owners', 'phone')
    # ### end Alembic commands ###
