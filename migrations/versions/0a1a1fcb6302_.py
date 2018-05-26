"""empty message

Revision ID: 0a1a1fcb6302
Revises: 
Create Date: 2018-05-26 20:35:58.639216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a1a1fcb6302'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=True),
    sa.Column('co2', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('recipe', sa.String(length=512), nullable=True),
    sa.Column('picture', sa.String(length=512), nullable=True),
    sa.Column('dish_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meal')
    op.drop_table('dish')
    # ### end Alembic commands ###
