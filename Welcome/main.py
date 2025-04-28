from fastapi import FastAPI

# FastAPI instance 생성
app = FastAPI()

# Path 오퍼레이션 생성. Path는 도메인명을 제외하고 / 로 시작하는 URL 부분
# 만약 url이 https://example.com/items/foo 라면 path는 /items/foo 
# Operation은 GET, POST, PUT/PATCH, DELETE등의 HTTP 메소드임. 
@app.get("/", summary="간단한 API",
    tags=["Simple"],
    # description="간단한 메시지를 반환하는 API" # docstring으로 대체 가능
    )
async def root():
    '''
    이것은 간단한 API 입니다. 아래는 인자값 입니다.

    - **인자값1**은 이거고요.
    - **인자값2**는 이거 입니다.
    '''
    return {"message": "Hello World"}

# uvicorn main:app --port 8081 --reload