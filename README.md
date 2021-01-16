# Spotiary

---

[TOC]

---



## Intro

> 자신이 방문했던 장소 `spot`, 방문했던 맛집 `spot`을 이미지, 지도 위치, 평점 등 `diary`의 형태로 관리할 수 있는 `Spotiary`의 웹사이트를 제작한다.

### Service

- 자신이 방문했던 장소/맛집을 `지도`와 `캘린더`의 형식으로 관리할 수 있는 서비스를 제공한다.
- In this service, users can keep their records of place/restaurant in the form of map and calendar.

### Compatibility

- Python 3.9, Vue 4.5, Django 3.1 버전에서 테스트되었다.
- We tested the code using Python 3.9, Vue 4.5, Django 3.1.

### Requirements

```markdown
asgiref==3.3.1
certifi==2020.12.5
chardet==4.0.0
Django==3.1.5
django-cors-headers==3.6.0
djangorestframework==3.12.2
djangorestframework-jwt==1.11.0
idna==2.10
Pillow==8.1.0
PyJWT==1.7.1
pytz==2020.5
requests==2.25.1
sqlparse==0.4.1
urllib3==1.26.2
```



![Main Page](img/main_page.png)



## Development Log

**0116**

- 프론트엔드와 백엔드 프레임을 개발하였다.

**과제**

- `jwt_token`을 서버에 요청하면 `404 Errror`가 발생한다.





***Copyright* © 2021 Song_Artish**