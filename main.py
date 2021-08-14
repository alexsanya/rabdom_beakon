from fastapi import FastAPI

app = FastAPI()

@app.post("/getPayload/{size:int}")
def get_payload(size: int):
    return {"data": 'z'*size}
