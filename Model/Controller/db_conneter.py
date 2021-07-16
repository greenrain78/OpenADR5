"""
DB에 직접적인 역활을 수행
- 커서를 생성하여 sql문을 실행
"""

from logging import getLogger

import pymysql

from db_settings import mariaDB_IP, mariaDB_ID, mariaDB_password, mariaDB_DB_name, mariaDB_port

log = getLogger(__name__)


class mariaDB_connect:
    """
    maria db와 직접적으로 연결
    """

    def getConn(self):
        # 커서 생성
        conn = pymysql.connect(
            host=mariaDB_IP,
            user=mariaDB_ID,
            password=mariaDB_password,
            db=mariaDB_DB_name,
            charset='utf8',
            port=mariaDB_port
        )
        return conn

    def runSQL(self, sql):
        try:
            conn = self.getConn()
            # 커서 생성
            cur = conn.cursor()
            # sql문 실행
            cur.execute(sql)
            result = cur.fetchall()

            # DB에 반영
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            log.error(e)

    def getSQL(self, sql):
        try:
            conn = self.getConn()
            cur = conn.cursor()

            cur.execute(sql)
            result = cur.fetchall()

            conn.commit()
            conn.close()

            log.debug("(get): %s \n \t %s", sql, result)
            return result
        except Exception as e:
            log.exception("get error: %s", sql)