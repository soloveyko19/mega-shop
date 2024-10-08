"""Add table produtcs

Revision ID: 88635d8d2c04
Revises: f746ddc6d871
Create Date: 2024-09-07 15:28:57.424978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88635d8d2c04'
down_revision: Union[str, None] = 'f746ddc6d871'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=4000), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=15, scale=2), nullable=False),
    sa.Column('image_url', sa.String(length=2048), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
