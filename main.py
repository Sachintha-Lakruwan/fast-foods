from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/foods", response_model=List[str])
def get_foods():
    return ["Pizza", "Burger", "Sushi", "Pasta", "Salad"]
