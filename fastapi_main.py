#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/demo1")
async def root():
    return {"message": "demo1"}

@app.get("/demo2")
async def root():
    return {"message": "demo2"}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="fastapi_main:app", host="127.0.0.1", port=8888)