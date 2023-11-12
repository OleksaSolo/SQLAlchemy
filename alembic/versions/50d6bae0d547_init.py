"""Init

Revision ID: 50d6bae0d547
Revises: 
Create Date: 2023-11-11 23:44:26.738884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50d6bae0d547'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('disciplines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('date_of', sa.Date(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('discipline_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['discipline_id'], ['disciplines.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('students')
    op.drop_table('disciplines')
    op.drop_table('teachers')
    op.drop_table('groups')
    # ### end Alembic commands ###
