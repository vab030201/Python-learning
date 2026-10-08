
from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    # Load data from a file or database
    with open("patients.json", "r") as f:
        json_data = json.load(f)
    return json_data

@app.get("/")
def hello():
    return {"message": "Patients management system is running!"}

@app.get("/about")
def about():
    return {"message": "This is a simple patients management system."}
   
@app.get("/view")
def view():
    data = load_data()
    return data
   