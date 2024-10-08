"""Add categories table

Revision ID: 23d7f76d17af
Revises: 88635d8d2c04
Create Date: 2024-09-07 20:32:17.426256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23d7f76d17af'
down_revision: Union[str, None] = '88635d8d2c04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('products', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'products', 'categories', ['category_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'category_id')
    op.drop_table('categories')
    # ### end Alembic commands ###
