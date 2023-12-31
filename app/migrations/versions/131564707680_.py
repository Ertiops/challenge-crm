"""empty message

Revision ID: 131564707680
Revises: 195d4dd0f1e6
Create Date: 2023-08-31 13:58:41.494797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '131564707680'
down_revision: Union[str, None] = '195d4dd0f1e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_franchise_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'franchises', ['franchise_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_franchise_id_fkey', 'users', 'franchises', ['franchise_id'], ['id'])
    # ### end Alembic commands ###
