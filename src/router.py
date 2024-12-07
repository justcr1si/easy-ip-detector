from typing import Annotated, Union

import requests
from fastapi import APIRouter, Depends, HTTPException

from schemas import IPRequest

ip_router = APIRouter(prefix='/ip')


@ip_router.post('')
def get_ip_info(request: Annotated[IPRequest, Depends()]) -> dict[str, Union[str, float]]:
    ip = request.ip
    response = requests.get(f"http://ip-api.com/json/{ip}")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail='Error while requesting')

    data = response.json()

    if data.get('status') != 'success':
        raise HTTPException(status_code=400, detail='Invalid IP-address')

    return data
