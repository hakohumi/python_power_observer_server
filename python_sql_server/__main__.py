

from fastapi import FastAPI

# from train_sql import train_sql


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


if __name__ == "__main__":
    def _main():
        pass
    # train_sql()
    _main()
