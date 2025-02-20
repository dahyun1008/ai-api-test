from typing import Union
from fastapi import FastAPI

# model.py
import model

# 그 안에 있는 AndModel 클래스의 인스턴스를 생성한다.
model = model.AndModel()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# item_id: 경로 매개 변수 (경로 파라미터)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 모델 학습도 api로 찌르기
@app.get("/train")
def train():
    model.train()
    return {"train": "ok"}

@app.get("/predict/left/{left}/right/{right}")
def predict(left: int, right: int):
    result = model.predict([left, right])
    return {"result": result}