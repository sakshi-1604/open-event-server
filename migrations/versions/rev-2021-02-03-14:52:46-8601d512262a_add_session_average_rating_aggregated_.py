"""Add session.average_rating aggregated column

Revision ID: 8601d512262a
Revises: b75a8dd29262
Create Date: 2021-02-03 14:52:46.176023

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '8601d512262a'
down_revision = 'b75a8dd29262'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('average_rating', sa.Float(), nullable=False, server_default='0'))
    op.execute('update sessions set average_rating = (select COALESCE(avg(rating), 0) from feedback where session_id = sessions.id)')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sessions', 'average_rating')
    # ### end Alembic commands ###