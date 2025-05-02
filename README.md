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
    - def read_item(item_id: str, q: str | None = None)   ... python3.10 부터 가능
    - def read_item_op(skip: int, limit: Optional[int] = None)

4. Requests/main_rbody.py
- pydantic으로 body를 받으면, 이를 application/json 형식으로 전달한다.
- main_rbody에 정의된 pydantic class 이름이 Item이라면, 클래스는 main_rbody.Item이 된다.
- optional 표기
    - tax: float | None = None
    - tax: Optional[float] = None
- model_dump: dict로 반환
    - 함수 내에서 pydantic을 바꾸긴 어려울 때, dict로 변환해서 업데이트 후 반환
- path params, request body, query params 을 넣어 PUT을 사용하는 실습

5. Requests/main_rbody_js.py
- JavaScript 를 통해 동적으로 값을 호출하는 방식
- http://localhost:8081/static/rbody.html