from fastapi import FastAPI, UploadFile, File
from utils.match_image import match_island
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s :%(levelname)s:%(funcName)s:%(lineno)d %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

app = FastAPI()

@app.post("/match-island/")
async def match_island_endpoint(input_image: bytes = File(...)):
    result = match_island(input_image)
    return {"result": result}