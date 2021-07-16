"""
DB에 연결하기 위해 sql문을 작성하는 객체

"""
from typing import Dict

from Controller.db_conneter import mariaDB_connect
from db_settings import elec_table_name, elec_field, eqps_table_name, eqps_field


class DBAdapter:
    """
    sql문을 생성해주는 객체
    부모 객체로서 기본적인 crud sql문들을 구현
    추후 orm방식을 도입하는 것을 고려
    """

    def __init__(self):
        self.db_connect = mariaDB_connect()

    def get_insert_sql(self, table_name, siteId, data: dict, data_format: dict) -> str:
        """
        데이터 생성에 사용하는 sql 문 생성
        :param table_name: 데이터를 저장할 테이블 명
        :param siteId: 데이터의 사이트 아이디 - 걍 data에 넣어서 관리하기 귀찮아서 인자를 하나 받음
        :param data: DB에 저장할 데이터
        :param data_format: 데이터 포멧 설정 미설정시 문자열이라고 판단하여 ''을 추가
        :return: 작성된 sql 문
        """
        # sql 문 frame 생성
        sql_col = f"INSERT INTO {table_name} " \
                  f"(siteId"
        sql_val = f") VALUES( '{siteId}'"

        # sql문에 데이터 삽입
        for key, val in data.items():
            # 칼럼 입력
            sql_col += f", {key}"
            if data_format[key] == 'str':
                # 포멧이 없거나 문자열인 경우 '' 추가
                sql_val += f", '{val}'"
            else:
                # 문자열이 아닌 경우 ''제거
                sql_val += f", {val}"

        # sql문 완성
        sql = sql_col + sql_val + f")"
        return sql

    def get_select_sql(self, table_name, select_list=None, condition=None) -> str:
        """
        데이터 read에 사용하는 sql문 생성
        :param table_name:
        :param select_list:
        :param where_list:
        :return:
        """
        sql = f"SELECT "

        # 가져올 데이터 선택
        if select_list is None:
            sql += f" * "
        else:
            # 가져올 데이터 입력
            for i in select_list:
                sql += f" {i},"
            # 끝에 , 제거
            sql = sql[:-1] + " "

        # 테이블 정보 입력
        sql += f"FROM {table_name} "

        # 조건식 입력
        if condition is not None:
            sql += f" WHERE {condition}"

        return sql

    def get_update_sql(self, table_name, select_list=None, where_list: dict = None) -> str:
        """
        데이터를 update하는데 사용하는 sql문 생성
        :param table_name:
        :param select_list:
        :param where_list:
        :return:
        """
        sql = f"UPDATE "

        # 테이블 정보 입력
        sql += f"{table_name} "

        # 조건식 입력
        if where_list is not None:
            for key, val in where_list:
                sql += f"{key}={val}"

        return sql


class DBAdapterELEC(DBAdapter):

    def insert_api_raw(self, siteId, data: dict):
        """
        데이터를 하나씩 받아와 sql문을 작성하여 DB에 저장
        :param siteId:
        :param data:
        :return:
        """
        # 데이터 포멧 생성 - raw 데이터 이므로 모든 데이터를 str 으로 저장
        data_format = {}
        for key in data.keys():
            data_format[key] = "str"

        # sql 생성
        sql = self.get_insert_sql(elec_table_name, siteId, data=data, data_format=data_format)
        print(sql, flush=True)

        # sql 실행
        self.db_connect.runSQL(sql)


class DBAdapterEQPS(DBAdapter):

    def select_api_data(self, empty=False):


        # 조건 설정
        if empty is False:
            condition = f" eqpCode != -1"
            # sql 생성
            sql = self.get_select_sql(eqps_table_name, condition=condition)
        else:
            # sql 생성
            sql = self.get_select_sql(eqps_table_name)
        print(sql, flush=True)

        # sql 실행
        data = self.db_connect.getSQL(sql)
        return data

    def insert_api_date(self, siteId, data: dict):
        # 데이터 포멧 생성 - 해당 형식에 맞게 변형해서 삽입
        # data_format = eqps_field # 알수 없는 오류로 변경 불가능

        data_format = {}
        for key in data.keys():
            data_format[key] = "str"

        # sql 생성
        sql = self.get_insert_sql(eqps_table_name, siteId, data=data, data_format=data_format)
        print(sql, flush=True)

        # sql 실행
        self.db_connect.runSQL(sql)

    def update_api_date(self, siteId, data: dict):
        pass
