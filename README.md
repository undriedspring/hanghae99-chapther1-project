# 문화로

문화로는 뮤지컬 산업에 대한 애정을 바탕으로 커뮤니티의 증대를 위해 각종 뮤지컬에 대한 정보를 제공합니다.

<hr>

## 와이어 프레임

카카오 오븐 url :
https://ovenapp.io/view/LOQUfroHiJEaz5RXfAEHMp6d4e6ectIb/

<hr>

## 웹사이트 링크
http://taesukang.shop/

<hr>

## 데모영상 유튜브 링크
<hr>

## 개발해야할 기능들(업데이트 예정)

| 기능                  | Method  | url     | Request                        | Response |
| --------------------- | ---- | ---------- | ------------------------------ | -------- |
| 로그인                | post | /login     | { userId: id, userPw: password } | JWT token         |
| 회원가입 | post | /sign_up/save | { userId: id, userPw: pw } | |
| 게시물 리스트(메인)   | get  | / | --                             | 전체 게시글 |
| 뮤지컬 세부 정보 | get | /details | { { id: id } } | 세부 게시글 정보 |
| 마이페이지(후기)      | get | /myPage    | { token: mytoken }                     | 내가 작성한 리뷰 목록 |
