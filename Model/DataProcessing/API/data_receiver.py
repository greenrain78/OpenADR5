"""
api를 사용하여 데이터를 가져오는 객체
지정된 형식에 맞게 api를 요쳥
"""

from datetime import datetime, timedelta
from typing import Dict

from DataProcessing.API.adr_api_client import ADR_API_Client


class API_Receiver(object):
    """
    api를 사용하여 데이터를 가져오는 객체
    지정된 형식에 맞게 api를 요쳥
    """

    def __init__(self):
        self.adr_api = ADR_API_Client()

    def read_api_elec(self, siteId, perfId, before_days: int = None, api_time: str = None) -> Dict:
        """
        api를 사용하기 위해 인자를 받음
        :param before_days:
        :param siteId:
        :param perfId:
        :param api_time:
        :return:
        """

        # 날짜가 정해져서 해당 날짜만큼 이전 날짜를 조회
        if before_days is not None:
            req_time = datetime.now() - timedelta(days=before_days)
            req_time = req_time.strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
            data = self.adr_api.fetch_elec(siteId, perfId, req_time)
            return data

        # api_time으로 지정된 날짜가 있으면 해당 날짜로 요청
        if api_time is not None:
            data = self.adr_api.fetch_elec(siteId, perfId, api_time)
            return data

    def read_api_eqps(self, siteId) -> Dict:
        """
        site id을 입력받아 설비 정보를 가져온다
        :param siteId:
        :return:
        """
        data = self.adr_api.fetch_eqps(siteId)
        return data
