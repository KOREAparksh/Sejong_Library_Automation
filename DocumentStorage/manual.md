# 사용설명서

## 설치방법
### 코드 받아오기
해당 프로젝트는 학술정보원 5층 사무실 내부 컴퓨터를 기준으로 작성되어 있습니다.
exe파일만 따로 가져가 실행할 경우 실행이 원할하지 않을 수 있으니, 코드를 다운받아 직접 exe파일로 변환하는 것을 권고합니다.

- 해당 컴퓨터에 python3 이상의 버전이 필요합니다. 아래의 링크에서 파이썬을 다운받아주세요.
[파이썬 다운로드 링크](https://www.python.org/downloads/)
- 컴퓨터 내 git을 설치하여 해당 코드를 복제하여야 합니다. 아래의 링크를 통해 깃을 설치합니다.
[git 다운로드 링크](https://git-scm.com/downloads)


- cmd를 열어, 파일을 다운로드 받고싶은 폴더로 이동합니다.
```
cd "원하는 폴더 경로"
```

- cmd를 열어 아래의 명령어를 입력합니다.
```
git clone https://github.com/KOREAparksh/Sejong_Library_Automation
```

### 폴더 옮기기
- 다운받은 코드 내 Sejong Library Automation 폴더를 복사합니다.
- 경로 : C드라이드 > Program Files (x86) 내에 붙혀넣습니다.
`C:/Program Files (x86)/Sejong Library Automation/`

### 드라이버 파일 설치하기
- 크롬을 열어 아래의 주소로 이동하여, 현재의 크롬 버전을 확인합니다.
```
chrome://version/
```
- 화면 최상단에서 아래와 같은 크롬버전을 확인합니다.
맨 앞자리 두개만 알면 됩니다. (아래의 경우 88)
```
Chrome	88.0.4324.146 (공식 빌드) (x86_64)
```
- 아래의 경로에서 자신의 버전과 맞는 드라이버를 설치합니다.
[크롬 드라이버 다운로드](https://chromedriver.chromium.org/downloads)

- 아래의 경로에 드라이버 파일을 붙혀넣습니다.
(`여기에....`로 시작하는 폴더에 넣으면 안됩니다.)
`C:/Program Files (x86)/Sejong Library Automation/driver/`


### 코드 실행하기
#### exe파일 만들어 실행하기
- cmd에서, 다운받은 폴더 내 `main.py`가 있는 폴더로 이동합니다.
cmd를 종료하지 않았다면, 위 경로에 바로 `main.py`가 존재합니다.
```
cd "main.py가 있는 경로"
```
- cmd에서 아래의 명령어를 입력하여, 파이썬을 exe파일로 변환시키는 pyinstaller를 설치합니다.
```
pip install pyinstaller
```
- 아래의 명령어를 입력하여 exe파일을 만듭니다. 해당 파일은 현재 경로의 `dist폴더`에 생성됩니다.
```
pyinstaller -w -F main.py
```
- dist 내 exe파일을 실행하여 프로그램을 사용합니다. 더블 클릭 후, 약간의 딜레이가 존재합니다.

#### exe파일 없이 진행하기
- 파이썬을 구동시킬 수 있는 IDE를 설치하여 `main.py`를 실행합니다.

<br>
## 사용방법
- IWS(통합작업환경)을 실행하여 활성화합니다.
- `윈도우키` + `→`키를 눌러, IWS 화면을 오른쪽 반으로 분할합니다.

- `main.py` 혹은 `exe파일`을 실행합니다.
- 
