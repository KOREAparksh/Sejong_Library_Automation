# Sejong_Library_Automation
세종대학교 학술정보원 근로장학생을 위한 초록목차 업무자동화 레포지토리

## 사용방법
- 크롬 브라우저를 기준으로 작성된 프로그램입니다.
- 크롬드라이버는 각자 버전에 맞는 드라이버를 다운받으셔서, 프로젝트 파일에 넣으셔야 합니다.

## 기능구현목록
- [ ] window처리
  - [ ] 전체검색 카테고리 "등록번호"로 변경
  - [ ] 등록번호 범위 입력
  - [ ] 결과리스트 체크박스 선택
  - [ ] 상세정보 창 띄우기
  - [ ] 관계정보 탭 열기 (1번만)
  - [ ] ISBN 포함 문자열 추출
  - [ ] 초록, 목차 입력 및 저장
  - [ ] 다음 책 정보 넘어가기
- [ ] 웹 크롤링
  - [x] 책 상세정보 페이지 넘어가기
  - [x] 책 초록, 목차 크롤링
- [ ] 메세지 출력
  - [x] 데이터 입력
    - [x] 등록번호 입력
  - [ ] 데이터 출력
    - [ ] 완료되지 않은, 처리하지 않은 등록번호 출력
- [ ] 기타 예외처리
  - [ ] 등록번호가 총 12자리인지
  - [ ] 등록번호 앞 6자리가 0으로 채워져 있는지
  - [ ] 통합작업환경 창(IWS)이 열려있지 않을 때
  - [ ] 등록번호 검색이 제대로 이루어지지 않을 때
  - [ ] 등록번호의 체크박스를 전부 체크하지 않았을 때
  - [ ] 이미 초록목차가 저장된 책일 때
  - [ ] ISBN검색이 되지 않을 때 (네이버책에 책 정보가 뜨지 않을 때)
  - [ ] 웹크롤링 시 초록 혹은 목차가 존재하지 않을 때



## 코드 작성중
파이썬으로 처음 진행하는 소규모 프로젝트입니다.

파이썬을 제대로 배워보지도, 사용해본적도 없습니다.

디자인패턴 등 아무것도 모르니 답답하시거나 도움을 주실 분은 PR이나 피드백 주시면 감사하겠습니다.

## 기술스택
파이썬, beautifulsoup4, selenium, pyautogui