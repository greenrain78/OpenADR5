"""
정상 작동하는지 임시로 구현한 테스트 엔진
드라이버
"""

from datetime import datetime
from DataProcessing.API.data_receiver import API_Receiver
from Engine.data_engine import DataEngineELEC, DataEngineEQPS
from settings import siteId_list, recent_date_range


class TestEngine:
    """
    정상 작동하는지 임시로 구현한 테스트 엔진
    """

    def __init__(self):
        # DB 데이터 입출력
        self.data_ELEC = DataEngineELEC()
        self.data_EQPS = DataEngineEQPS()
        # api 사용
        self.api_receiver = API_Receiver()

    def test_hello(self):
        """
        간단 engine 동작 확인
        """
        print(f"hello {datetime.now()}", flush=True)

    def test_get_data(self):
        """
        api를 통해 요청받은 데이터를 DB까지 정상적으로 전달되는지 테스트
        """
        # 데이터를 읽어옴
        data = self.api_receiver.read_api_elec('ace', 300, api_time="20200309")
        # 데이터를 저장
        self.data_ELEC.save_by_api('ace', data)
        # 화면에 표시
        print(f"data : {data}", flush=True)

    def get_data_recent(self):
        """
        최근 데이터를 조회하여 빈 데이터를 삽입
        """
        # 장비들 갱신
        self.data_EQPS.auto_update()

        # 최근 데이터 생성
        for call_data in self.data_EQPS.read_all():
            # 최근 데이터 조회 - 오늘로부터 지정일 만큼 검색
            for days in range(recent_date_range):
                # 데이터 가져오기
                print(f"call : {call_data}", flush=True)

                data = self.api_receiver.read_api_elec(call_data[0], call_data[1], before_days=days)
                # 데이터 저장
                print(f"data : {data}", flush=True)
                if data.get('elecs'):
                    self.data_ELEC.save_by_api(call_data[0], data)
                # 화면에 표시
