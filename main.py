from fastapi import FastAPI
#from routers import scraper, wiki
from database import engine
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

