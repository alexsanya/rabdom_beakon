from fastapi import FastAPI

app = FastAPI()

@app.post("/getPayload/{size:int}")
def get_payload(size: int):
    one_megabyte = 'x'*10**6
    return {"data": one_megabyte*size}
