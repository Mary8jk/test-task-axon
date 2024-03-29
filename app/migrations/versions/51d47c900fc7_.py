"""empty message

Revision ID: 51d47c900fc7
Revises: b09f8c4e6a51
Create Date: 2024-02-18 22:54:02.270535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '51d47c900fc7'
down_revision: Union[str, None] = 'b09f8c4e6a51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ВыпускПродукции')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ВыпускПродукции',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"ВыпускПродукции_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('closed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('СтатусЗакрытия', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('ПредставлениеЗаданияНаСмену', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Линия', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Смена', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Бригада', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('НомерПартии', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ДатаПартии', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('Номенклатура', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('КодЕКН', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ИдентификаторРЦ', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ДатаВремяНачалаСмены', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('ДатаВремяОкончанияСмены', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', 'НомерПартии', name='ВыпускПродукции_pkey')
    )
    # ### end Alembic commands ###
