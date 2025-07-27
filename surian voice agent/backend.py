from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import json
import uuid
from datetime import datetime, timedelta
import os

app = FastAPI()
ORDERS_FILE = os.path.join('data', 'orders.json')

class OrderRequest(BaseModel):
    name: str
    order: List[str]

class OrderResponse(BaseModel):
    order_id: str
    eta: str

@app.post('/submit-order', response_model=OrderResponse)
def submit_order(order: OrderRequest):
    order_id = str(uuid.uuid4())
    eta = (datetime.now() + timedelta(minutes=30)).strftime('%H:%M')
    order_data = {
        'order_id': order_id,
        'name': order.name,
        'order': order.order,
        'eta': eta,
        'timestamp': datetime.now().isoformat()
    }
    # Store order in JSON file
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, 'r', encoding='utf-8') as f:
            orders = json.load(f)
    else:
        orders = []
    orders.append(order_data)
    with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)
    return OrderResponse(order_id=order_id, eta=eta) 