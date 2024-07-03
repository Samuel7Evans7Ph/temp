from typing import Annotated
import cv2

from fastapi import FastAPI,Path,Query,Form,File,UploadFile

app=FastAPI()

from meta_integrate import *


@app.get("/items/{item_id}")
async def read_items(item_id:Annotated[int, Path(title="testing?")],
                     q:str|None=None):
    results={"item_id":item_id}

    if q:
        results.update({"q":q})
    return results


#@app.post("/login/")
async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
    return {"username":username}

#@app.post("/uploadfile/")
#async def create_upload_file(file:UploadFile):
#    contents=await file.read()
#    return {contents}
#
db=[]

@app.post("/upload_file")
async def send_image(image_file:UploadFile):
    contents=await cv2.imread(image_file)
    meta_integrate(contents)

    return {}
    

    

