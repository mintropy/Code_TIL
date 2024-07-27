"""items foreignkey

Revision ID: ba875ecf6f84
Revises: 9bbf0a531ef1
Create Date: 2024-07-24 22:08:42.415652

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ba875ecf6f84"
down_revision: Union[str, None] = "9bbf0a531ef1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key("item_owner", "item", "user", ["owner_id"], ["id"])
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_constraint("item_owner", "item", type_="foreignkey")
    # ### end Alembic commands ###
