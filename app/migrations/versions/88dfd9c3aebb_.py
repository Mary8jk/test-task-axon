"""empty message

Revision ID: 88dfd9c3aebb
Revises: 51d47c900fc7
Create Date: 2024-02-19 18:16:23.368319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '88dfd9c3aebb'
down_revision: Union[str, None] = '51d47c900fc7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('продукция')
    op.drop_table('products')
    op.drop_table('ВыпускПродукции')
    op.drop_table('про')
    op.drop_table('Продукция')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Продукция',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Продукция_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('УникальныйКодПродукта', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('НомерПартии', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ДатаПартии', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_aggregated', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('aggregated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Продукция_pkey'),
    sa.UniqueConstraint('УникальныйКодПродукта', name='Продукция_УникальныйКодПродукт_key')
    )
    op.create_table('про',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"про_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('УникальныйКодПродукта', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('НомерПартии', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ДатаПартии', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_aggregated', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('aggregated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='про_pkey'),
    sa.UniqueConstraint('УникальныйКодПродукта', name='про_УникальныйКодПродукта_key')
    )
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
    sa.PrimaryKeyConstraint('id', 'НомерПартии', name='ВыпускПродукции_pkey'),
    sa.UniqueConstraint('НомерПартии', 'ДатаПартии', name='ВыпускПродукци_НомерПартии_Дат_key')
    )
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('УникальныйКодПродукта', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('НомерПартии', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ДатаПартии', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_aggregated', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('aggregated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='products_pkey'),
    sa.UniqueConstraint('УникальныйКодПродукта', name='products_УникальныйКодПродукта_key')
    )
    op.create_table('продукция',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"продукция_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('УникальныйКодПродукта', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('НомерПартии', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ДатаПартии', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_aggregated', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('aggregated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='продукция_pkey'),
    sa.UniqueConstraint('УникальныйКодПродукта', name='продукция_УникальныйКодПродукт_key')
    )
    # ### end Alembic commands ###
