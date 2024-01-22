from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return { "안녕하세요 반갑습니다" }