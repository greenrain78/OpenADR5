"""
Schedule DB SchedulerManager
실질적인 스캐줄 객체
"""
import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


class MainScheduler:

    def __init__(self):
        # 스캐줄 생성
        self.schedule = BackgroundScheduler()
        log.debug("SchedulerManager init schedule")

    def create_job(self, method, schedule_id: str, **schedule_time):
        """
        :param method: 실행할 함수
        :param schedule_id: 스캐줄 id
        :param schedule_time: 반복할 시간
        :return:
        """
        self.schedule.add_job(method, 'cron', id=schedule_id, **schedule_time)

    def delete_schedule(self, schedule_id: str):
        self.schedule.resume_job(schedule_id)

    def run(self):
        self.schedule.start()
