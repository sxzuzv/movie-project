# kobis 모듈

KOBIS 오픈 API의 요청 주소를 만드는 모듈입니다. 요청은 하지 않고 **주소(문자열)만** 만듭니다. 요청은 `requests.get(주소)`로 직접 보냅니다.

```python
from kobis import URLMaker, load_key
```

| 이름 | 종류 | 무엇 |
| --- | --- | --- |
| [`load_key()`](#load_key) | 함수 | `.env`에서 내 키를 읽는다 |
| [`URLMaker`](#urlmaker) | 클래스 | 서비스마다 요청 주소를 만든다 |

## 빠르게 써 보기

```python
import requests

from kobis import URLMaker, load_key

url_maker = URLMaker(load_key())

url = url_maker.daily_boxoffice_url("20261001")
data = requests.get(url).json()
```

---

## load_key()

`.env` 파일의 `KOBIS_API_KEY` 값을 돌려줍니다.

돌려주는 값: `str`

`.env`가 없거나 값이 비어 있으면 `ValueError`가 납니다. README의 "키 넣기"를 다시 봅니다.

---

## URLMaker

### 만들기

#### `URLMaker(key)`

| 인자 | 타입 | 설명 |
| --- | --- | --- |
| `key` | `str` | KOBIS 키. 보통 `load_key()`의 결과를 넣는다 |

키는 만들 때 한 번만 넣습니다. 메서드마다 다시 넣지 않습니다.

### 속성

| 속성 | 타입 | 설명 |
| --- | --- | --- |
| `key` | `str` | 만들 때 넣은 키 |

### 메서드

메서드는 모두 **주소 문자열**을 돌려줍니다. 응답이 아닙니다.

#### `daily_boxoffice_url(target_dt, rep_nation_cd="")`

일별 박스오피스 TOP 10 주소.

| 인자 | 타입 | 기본값 | 설명 |
| --- | --- | --- | --- |
| `target_dt` | `str` | | 날짜. `"20261001"` 모양. 오늘 날짜는 아직 없다 |
| `rep_nation_cd` | `str` | `""` | `"K"` 한국 영화만 · `"F"` 외국 영화만 · `""` 전체 |

응답에서 영화 목록은 `["boxOfficeResult"]["dailyBoxOfficeList"]`에 있습니다. 숫자도 모두 문자열입니다.

| 필드 | 뜻 | 예 |
| --- | --- | --- |
| `rank` | 순위 | `"1"` |
| `rankInten` | 전날보다 오른 순위 (내리면 음수) | `"-2"` |
| `rankOldAndNew` | 새로 들어왔으면 `"NEW"` | `"OLD"` |
| `movieCd` | 영화 코드 | `"20261807"` |
| `movieNm` | 제목 | |
| `openDt` | 개봉일 | `"2026-09-30"` |
| `audiCnt` | 그날 관객 수 | `"31181"` |
| `audiAcc` | 누적 관객 수 | `"2393381"` |
| `salesAmt` | 그날 매출액 | `"331895400"` |
| `salesAcc` | 누적 매출액 | `"24665061050"` |
| `scrnCnt` · `showCnt` | 스크린 수 · 상영 횟수 | |

#### `movie_info_url(movie_cd)`

영화 상세정보 주소.

| 인자 | 타입 | 설명 |
| --- | --- | --- |
| `movie_cd` | `str` | 영화 코드. 박스오피스 목록의 `movieCd` |

응답에서 영화 정보는 `["movieInfoResult"]["movieInfo"]`에 있습니다.

| 필드 | 뜻 | 모양 |
| --- | --- | --- |
| `movieNm` | 제목 | 문자열 |
| `prdtYear` | 제작연도 | `"2026"` |
| `openDt` | 개봉일 | `"20260930"` (박스오피스와 모양이 다르다) |
| `showTm` | 상영시간(분) | `"98"`. 비어 있는 영화도 있다 |
| `nations` | 제작 국가 | `[{"nationNm": "한국"}, ...]` |
| `genres` | 장르 | `[{"genreNm": "드라마"}, ...]` |
| `directors` | 감독 | `[{"peopleNm": "...", "peopleNmEn": "..."}, ...]` |
| `actors` | 배우 | `[{"peopleNm": "...", "cast": "배역"}, ...]` |

감독 · 배우가 빈 리스트인 영화도 있습니다.

#### `people_list_url(people_nm)`

영화인 목록 주소. 이름으로 찾습니다.

| 인자 | 타입 | 설명 |
| --- | --- | --- |
| `people_nm` | `str` | 이름 |

응답 목록은 `["peopleListResult"]["peopleList"]`에 있습니다. 사람마다 `peopleCd` · `peopleNm` · `filmoNames`(`"작품1|작품2|…"`)가 있습니다.

#### `people_info_url(people_cd)`

영화인 상세정보 주소.

| 인자 | 타입 | 설명 |
| --- | --- | --- |
| `people_cd` | `str` | 영화인 코드. 영화인 목록의 `peopleCd` |

응답 목록은 `["peopleInfoResult"]["peopleInfo"]["filmos"]`에 있습니다. 작품마다 `movieCd` · `movieNm` · `moviePartNm`(`"배우"` · `"감독"` …)이 있습니다.

#### `weekly_boxoffice_url(target_dt)`

주간(월~일) 박스오피스 주소. `target_dt`가 들어 있는 주. 응답 목록은 `["boxOfficeResult"]["weeklyBoxOfficeList"]`.
