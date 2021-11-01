# 문화로(가제)

문화로(가제)는 뮤지컬 산업에 대한 애정을 바탕으로 커뮤니티의 증대를 위해 각종 뮤지컬에 대한 정보를 제공합니다.

<hr>

## 와이어 프레임

카카오 오븐 url :
https://ovenapp.io/view/uOkYjqzUpKGSkqlaXpueFKzboCJihrJa/IizVu

<hr>

## 개발해야할 기능들(업데이트 예정)

| 기능                  | url  | Method     | Request                        | Response |
| --------------------- | ---- | ---------- | ------------------------------ | -------- |
| 로그인                | post | /login     | { id: id, password: password } |          |
| 게시물 리스트(게시판) | get  | /post_list | --                             | 게시물들 |
| 게시물 리스트(메인)   | get  | /main_list | --                             | 게시물들 |
| 마이페이지(후기)      | post | /myPage    | { id: id }                     | 게시물들 |
