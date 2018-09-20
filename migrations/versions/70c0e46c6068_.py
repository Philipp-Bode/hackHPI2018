"""empty message

Revision ID: 70c0e46c6068
Revises: 0a1a1fcb6302
Create Date: 2018-05-26 20:41:54.607552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70c0e46c6068'
down_revision = '0a1a1fcb6302'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'meal', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'meal', type_='unique')
    # ### end Alembic commands ###
