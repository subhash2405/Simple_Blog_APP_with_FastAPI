from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def fund():
    return {"message":
                {
                "msg" : "Hello, World!"
                }
            }

@app.get("/health/{id}")
def health(id):
    return {"message": {"id": id, "status": "healthy"}}