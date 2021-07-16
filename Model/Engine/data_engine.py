"""
데이터를 관리하는 엔진
데이터를 사용할때 해당 객체를 이용해서 사용
해당 함수의 의미를 가지는 기능을 포괄적으로 담당
개념적인 기능을 수행

"""

from logging import getLogger

from DataProcessing.API.data_receiver import API_Receiver
from DataProcessing.DB.data_manager import DBAdapterELEC, DBAdapterEQPS
from settings import siteId_list

log = getLogger(__name__)


class DataEngine:
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """


class DataEngineELEC(DataEngine):
    """
    ELEC 데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self):
        self.db = DBAdapterELEC()

    def save_by_api(self, siteId, data):
        """
        api로 부터 받아온 데이터를 그대로 DB에 저장
        :param siteId:
        :param data: 데이터
        :return:
        """
        data_list = data.get('elecs')
        for data in data_list:
            # 데이터 전처리 필요
            self.db.insert_api_raw(siteId, data)
        pass

    def read(self):
        pass

    def update(self):
        pass


class DataEngineEQPS(DataEngine):
    """
    EQPS 데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self):
        self.db = DBAdapterEQPS()
        self.api_receiver = API_Receiver()

    def save(self):
        pass

    def read(self, siteId):
        condition = {
            "not eqpCode": -1
        }

        data = self.db.select_api_data(siteId, condition)
        return data

    def read_all(self):
        data = self.db.select_api_data()
        print(f"data : {data}", flush=True)
        return data

    def update(self):
        pass

    def auto_update(self):
        print(f"auto_update", flush=True)

        for siteId in siteId_list:
            # 데이터를 받아와 가공
            raw_data = self.api_receiver.read_api_eqps(siteId)
            datalist = raw_data.get('eqps')
            for data in datalist:
                print(f"data : {data}", flush=True)
                self.db.insert_api_date(siteId, data)


