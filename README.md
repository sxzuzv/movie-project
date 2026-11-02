# movie-project

KOBIS(영화관입장권통합전산망) 오픈 API로 올해 박스오피스 데이터를 모으고, 보고 싶은 정보를 코드로 만들어 보는 Python 복습 과제입니다.

## 내 저장소 만들기

1. 이 저장소 위쪽의 **Use this template → Create a new repository**
2. Owner는 내 계정, 이름은 `movie-project`, **Private**를 고르고 만듭니다
3. 내 저장소를 받습니다

```
git clone https://github.com/내아이디/movie-project.git
cd movie-project
uv sync
```

## KOBIS 키 받기

1. [KOBIS 오픈 API](https://www.kobis.or.kr/kobisopenapi/homepg/main/main.do)에 회원가입하고 로그인합니다
2. 위쪽 메뉴 **키 발급/관리 → 키 발급받기**
3. 서비스 사용 URL에는 `localhost`를 적습니다
4. 목록에 생긴 **발급키**를 복사합니다. 발급하면 바로 쓸 수 있습니다(하루 3,000회)

키는 나만 씁니다. 다른 사람과 나누지 않습니다.

## 키 넣기

```
cp .env.example .env
```

`.env`를 VS Code로 열어(`code .env`) `KOBIS_API_KEY=` 뒤에 키를 붙여 넣고 저장합니다.

- JupyterLab 파일 목록에는 `.env`가 보이지 않습니다. 점으로 시작하는 파일이라 숨겨집니다
- Windows 메모장으로 저장하면 이름이 `.env.txt`가 되기 쉽습니다. VS Code로 엽니다
- `.env`는 `.gitignore`에 들어 있어 git에 올라가지 않습니다
- 키를 코드(`.py` · `.ipynb`)에 직접 쓰지 않습니다. 코드는 `kobis.py`의 `load_key()`로 `.env`에서 읽습니다

## 실행

```
uv run jupyter lab
```

`tasks.ipynb`를 열고 위에서부터 실행합니다.

## 파일

| 파일 | 내용 |
| --- | --- |
| `tasks.ipynb` | 과제 노트북 |
| `kobis.py` | 키 읽기(`load_key`) · 요청 주소 만들기(`URLMaker`) |
| `docs/kobis.md` | `kobis.py` 사용 문서. 코드 대신 이 문서를 보고 씁니다 |
| `CLAUDE.md` | Claude Code가 이 과제에서 지킬 것 |
| `.env.example` | `.env`의 모양 |
| `data/` | 모은 데이터를 저장하는 폴더(`data/daily/날짜.json`). git에 올라가지 않습니다 |

## 데이터

KOBIS 이용약관에 따라 받은 결과를 다른 곳에 올리거나 보내지 않습니다. `data/`의 파일은 프로젝트가 끝나면 지웁니다.
