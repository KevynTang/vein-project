from data_api import DataAPI
from database.db_reader import read_from_db


class LocalAPI(DataAPI):

    @staticmethod
    def get(table_name, cols='*', condition='1'):
        data = read_from_db(
            f'''
            SELECT {cols} FROM {table_name}
            WHERE {condition};
            '''
        )
        return data

    def get_stock_list(self, cols='*', condition='1'):
        return self.get('STOCK_LIST', cols, condition)

    def get_indices_daily(self, cols='*', condition='1'):
        return self.get('INDICES_DAILY', cols, condition)

    def get_indices_weekly(self, cols='*', condition='1'):
        return self.get('INDICES_WEEKLY', cols, condition)

    def get_indices_monthly(self, cols='*', condition='1'):
        return self.get('INDICES_MONTHLY', cols, condition)

    def get_quotations_daily(self, cols='*', condition='1'):
        return self.get('QUOTATIONS_DAILY', cols, condition)

    def get_quotations_weekly(self, cols='*', condition='1'):
        return self.get('QUOTATIONS_WEEKLY', cols, condition)

    def get_quotations_monthly(self, cols='*', condition='1'):
        return self.get('QUOTATIONS_MONTHLY', cols, condition)

    def get_limits_statistic(self, cols='*', condition='1'):
        return self.get('LIMITS_STATISTIC', cols, condition)

    def get_adj_factors(self, cols='*', condition='1'):
        return self.get('ADJ_FACTORS', cols, condition)
