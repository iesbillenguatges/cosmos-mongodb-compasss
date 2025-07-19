from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["tasques"]
collection = db["tots"]

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    tasques = list(collection.find())
    return templates.TemplateResponse("index.html", {"request": request, "tasques": tasques})

@app.post("/add")
def add_tasca(nom: str = Form(...)):
    collection.insert_one({"nom": nom})
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{tasca_id}")
def delete_tasca(tasca_id: str):
    collection.delete_one({"_id": ObjectId(tasca_id)})
    return RedirectResponse("/", status_code=303)
