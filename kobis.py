"""KOBIS(영화관입장권통합전산망) 오픈 API 주소를 만드는 모듈"""

import os

from dotenv import load_dotenv

BASE_URL = "https://www.kobis.or.kr/kobisopenapi/webservice/rest"


def load_key() -> str:
    """.env 파일에서 KOBIS_API_KEY를 읽어 돌려준다."""
    load_dotenv()
    key = os.getenv("KOBIS_API_KEY", "")
    if not key:
        raise ValueError(".env 파일에 KOBIS_API_KEY를 넣어 주세요 (README의 '키 넣기')")
    return key


class URLMaker:
    """서비스마다 요청 주소를 만든다. 키는 만들 때 한 번만 넣는다."""

    def __init__(self, key: str):
        self.key = key

    def daily_boxoffice_url(self, target_dt: str, rep_nation_cd: str = "") -> str:
        """일별 박스오피스. target_dt는 "20261026" 모양, rep_nation_cd는 "K"(한국) · "F"(외국)"""
        return f"{BASE_URL}/boxoffice/searchDailyBoxOfficeList.json?key={self.key}&targetDt={target_dt}&repNationCd={rep_nation_cd}"

    def weekly_boxoffice_url(self, target_dt: str) -> str:
        """주간(월~일) 박스오피스. target_dt가 들어 있는 주"""
        return f"{BASE_URL}/boxoffice/searchWeeklyBoxOfficeList.json?key={self.key}&targetDt={target_dt}&weekGb=0"

    def movie_info_url(self, movie_cd: str) -> str:
        """영화 상세정보. movie_cd는 박스오피스 결과의 movieCd"""
        return f"{BASE_URL}/movie/searchMovieInfo.json?key={self.key}&movieCd={movie_cd}"

    def people_list_url(self, people_nm: str) -> str:
        """영화인 목록. 이름으로 찾는다"""
        return f"{BASE_URL}/people/searchPeopleList.json?key={self.key}&peopleNm={people_nm}"

    def people_info_url(self, people_cd: str) -> str:
        """영화인 상세정보. people_cd는 영화인 목록 결과의 peopleCd"""
        return f"{BASE_URL}/people/searchPeopleInfo.json?key={self.key}&peopleCd={people_cd}"
