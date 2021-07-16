

# DB 설정 파일 ./DB/.env 파일과 동일하게 설정
mariaDB_IP = 'mariaDB'
mariaDB_ID = 'user'
mariaDB_password = '1234'
mariaDB_DB_name = 'openadr'
mariaDB_port = 3306

# mariaDB_IP = '127.0.0.1'
# mariaDB_ID = 'user'
# mariaDB_password = '1234'
# mariaDB_DB_name = 'students'
# mariaDB_port = 4491


elec_table_name = "power_info"
elec_field = {
    "siteId": "str",
    "pnName": "str",
    "eqpName": "str",
    "perfId": "int",
    "ymdms": "str",
    "volTage": "double",
    "amPere": "double",
    "arPower": "int",
    "atvPower": "int",
    "ratPower": "int",
    "pwFactor": "int",
    "accruePower": "int",
    "voltagerS": "double",
    "voltagesT": "double",
    "voltagetR": "double",
    "temperature": "double",
    "data_time": "datetime",
}
eqps_table_name = "equipments_info"
eqps_field = {
    "siteId": "str",
    "eqpCode": "str",
    "eqpName": "str",
    "eqpType": "str",
    "perfId": "int",
    "data_time": "datetime",
}
