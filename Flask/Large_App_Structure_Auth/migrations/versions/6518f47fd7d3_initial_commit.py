"""Initial commit

Revision ID: 6518f47fd7d3
Revises: 
Create Date: 2018-09-09 16:38:45.259984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6518f47fd7d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_owners_name'), 'owners', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_owners_name'), table_name='owners')
    op.drop_table('owners')
    op.drop_table('puppies')
    # ### end Alembic commands ###
