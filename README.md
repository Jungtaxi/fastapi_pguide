1. Welcome/main.py
- `uvicorn main:app --port 8081 --reload` 실행
- SwaggerUI 동작 확인

2. Requests/main_path.py
- path parameter 실습
- endpoint가 정적일 때는, 동적인 것에 앞서 써줘야함.
    - 순서대로 주소와 HTTP Method가 매핑되기 때문

3. Requests/main_query.py
- query parameter 실습
- default 있으면, 변수 잘못 넣어도 default 반영되어서 에러 안남
- optional 준다고 해서 default를 안줘도 되는건 아니다.