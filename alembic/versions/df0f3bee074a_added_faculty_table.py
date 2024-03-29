"""added faculty table

Revision ID: df0f3bee074a
Revises: b8debe09a98e
Create Date: 2024-02-06 15:37:54.540866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df0f3bee074a'
down_revision: Union[str, None] = 'b8debe09a98e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_faculty',
    sa.Column('faculty_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('faculty_fname', sa.String(length=45), nullable=False),
    sa.Column('faculty_lname', sa.String(length=45), nullable=False),
    sa.Column('faculty_dept_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['faculty_dept_id'], ['tbl_departments.department_id'], ),
    sa.PrimaryKeyConstraint('faculty_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_faculty')
    # ### end Alembic commands ###
