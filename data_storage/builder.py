import sqlite3
import os

from utils import log
from data_storage import filer

if not os.path.exists('vein-project.db'):
    log('正在创建数据库...')
else:
    log('数据库已存在...')


def db_init(db_size):
    log(f'当前数据库大小设定为：{db_size}')
    # create_trade_date_list_table()
    create_index_quotation_table('SH_INDEX_DAILY')
    create_index_quotation_table('SZ_INDEX_DAILY')
    create_index_quotation_table('SH_INDEX_WEEKLY')
    create_index_quotation_table('SZ_INDEX_WEEKLY')
    create_index_quotation_table('SH_INDEX_MONTHLY')
    create_index_quotation_table('SZ_INDEX_MONTHLY')
    filer.fill_tables(db_size)
    filer.update_tables()
    filer.trim_tables(db_size)


# def create_trade_date_list_table():
#     conn = sqlite3.connect('vein-project.db')
#     log(f'检查或创建表：TRADE_DATE_LIST...')
#     conn.execute('''
#     CREATE TABLE IF NOT EXISTS TRADE_DATE_LIST (
#         TRADE_DATE CHAR(8) PRIMARY KEY
#     );
#     ''')


def create_index_quotation_table(table_name):
    conn = sqlite3.connect('vein-project.db')
    log(f'检查或创建表：{table_name}...')
    conn.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        TRADE_DATE CHAR(8) PRIMARY KEY,
        OPEN REAL,
        CLOSE REAL,
        LOW REAL,
        HIGH REAL,
        VOL REAL,
        K_MA30 REAL,
        VOL_MA30 REAL,
        UPS REAL,
        DOWNS REAL,
        AD_LINE REAL
    );
    ''')


def complete():
    log(f'数据库初始化完成！')