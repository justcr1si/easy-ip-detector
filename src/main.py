import uvicorn
from fastapi import FastAPI

from router import ip_router

app = FastAPI()
app.include_router(ip_router)

if __name__ == '__main__':
    config = uvicorn.Config(app, port=8080)
    server = uvicorn.Server(config)
    server.run()
