import uvicorn
from fastapi import FastAPI,Body
from schema import  User
#from config import setting
from DS.model import Model 



app = FastAPI()
model = Model()


@app.get("/drinks/{id}")
async def index(id:int):
    return f"jimmy {id}"

@app.get("/meals/{id}")
def index(id:int):
    return model.getx()


if __name__=="__main__":
        # uvicorn.run('main:app',reload=settings.DEBUG_MODE,host=settings.DOMAIN,port=settings.PORT)
        uvicorn.run('main:app',reload=True,host= "localhost" ,port=3000)

