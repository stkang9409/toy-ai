# toy-ai

toy projects

# 백엔드

## 버전정보
python 3.9.1

## 패키지 설치
`pip install requirements.txt`

## 로컬 실행 방식
1. `.env`파일이 필요합니다. 개발자에게 문의하세요
2. docker기반 mysql 실행

```bash
docker run -itd --name openai_mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_USER=openai -e MYSQL_PASSWORD=secret -e MYSQL_DATABASE=openai -v {YOUR_PATH}/toy-ai/backend/mysql/initdb.d:/docker-entrypoint-initdb.d -p 3306:3306 mysql:latest
```

    - -v 옵션에서 YOUR_PATH에 절대경로를 맞춰서 입력해야합니다.
3. FLASK 실행
```bash
python app.py
```
