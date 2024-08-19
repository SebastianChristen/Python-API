from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        "data": 
            {
                "name": "Sebu"
            }
    } 



   
    # def index():
    #     return {'data': {'name': 'Sebu'}}





@app.get('/about')
def about():
    return {
        "data": 
            {
                "site": "about"
            }
    } 