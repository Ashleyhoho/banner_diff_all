"""empty message

Revision ID: 210caacb6f85
Revises: a5d24a8a1b10
Create Date: 2024-04-01 19:14:30.023444

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '210caacb6f85'
down_revision = 'a5d24a8a1b10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_style',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('original_image_id', sa.Integer(), nullable=True),
    sa.Column('style', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['original_image_id'], ['original_image.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('original_image_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['original_image_id'], ['original_image.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('original_image', schema=None) as batch_op:
        batch_op.drop_column('type')
        batch_op.drop_column('style')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('original_image', schema=None) as batch_op:
        batch_op.add_column(sa.Column('style', sqlite.JSON(), nullable=True))
        batch_op.add_column(sa.Column('type', sqlite.JSON(), nullable=True))

    op.drop_table('image_type')
    op.drop_table('image_style')
    # ### end Alembic commands ###
