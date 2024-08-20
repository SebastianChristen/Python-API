from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()




@app.get('/blog')
# Hier sind "Bool" und "10" die Default values, falls der Parameter nicht mitgegeben wurde im request.
# Mit "Optional" kann mann angeben, wenn ein Parameter Optional ist, den Datentyp und default = None
def index(limit = 10, published: bool = True, sort: Optional[str] = None):

    if published:
        return {
            "data": 
            {
                    f"{limit} {sort} PUBLISHED blogs fetched from List",
                
        }}
    else:
      return {
            "data": 
            {
                    f"{limit} {sort}  unpublished blogs fetched from List",
                
        }
          
    } 



   
    # def index():
    #     return {'data': {'name': 'Sebu'}}



@app.get('/blog/unpublished')
def unpublished():
    return {
        "data": 
            
                "All unpublished blogs"
            
    } 






@app.get('/blog/{id}')
def show(id: int):
    return {
        "data": 
            {
                "data": id
            }
    } 






@app.get('/blog/{id}/comments')
def comments(id: int, limit = 10):
    return {
        "data": 
            {
                "data": f"id: {id}, limit: {limit}"
            }
    } 


# Blog ist eine Klasse, also ein Komplexer Datentyp mit vielen Attributen, die den blog Beschreiben.
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]





@app.post('/blog')
def create_blog(request: Blog):
    return {
        "data": 
            {
                "data": f"{request} blog was created succesfully"
            }
    } 


# das hier ist viel besser, macht alles local, ohne dass ich uvicorn starten muss.
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port = 9000)