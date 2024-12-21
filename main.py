import os
from pydantic import BaseModel
from fastapi import FastAPI
from googlesearch import search
from starlette.middleware.cors import CORSMiddleware

username = "geonode_WRVJYKoq40"
password = "59eb5a54-bbf9-4096-9385-5323b360079f"


# Set proxies as environment variables


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    query: str
    num: int = 10

@app.post("/")
def search_google(item: Item) -> list[str]:
    import random

    GEONODE_DNS = f"us.premium-residential.geonode.com:{random.randint(9002, 9008)}"

    os.environ["http_proxy"] = f"http://{username}:{password}@{GEONODE_DNS}"
    os.environ["https_proxy"] = f"https://{username}:{password}@{GEONODE_DNS}"
    
    results = search(item.query, num=item.num, stop=item.num)
    return results
