"""empty message

Revision ID: 827ccca5421
Revises: None
Create Date: 2015-05-01 15:48:42.526149

"""

# revision identifiers, used by Alembic.
revision = '827ccca5421'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
      'deck_set',
      sa.Column('id', sa.Integer, primary_key=True),
      sa.Column('name', sa.String(80), unique=True, nullable=False),
    )
    op.create_table(
      'deck',
      sa.Column('id', sa.Integer, primary_key=True),
      sa.Column('set_id', sa.Integer, sa.ForeignKey('deck_set.id')),
      sa.Column('name', sa.String(50), unique=True, nullable=False),
    )



def downgrade():
    op.drop_table('deck')
    op.drop_table('deck_set')
