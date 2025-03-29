import os

import uvicorn
from fastapi import FastAPI

from app import routes
from app.routes import product_routes, order_routes

# FastAPI App
app = FastAPI()

# Include Routers
app.include_router(product_routes.router, tags=["Products"])
app.include_router(order_routes.router, tags=["Orders"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
