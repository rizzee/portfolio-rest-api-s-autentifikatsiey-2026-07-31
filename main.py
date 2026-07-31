from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import auth, products
from middleware.rate_limiter import RateLimiterMiddleware
import models
from database import engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow all origins for dev (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Apply rate limiting
app.add_middleware(RateLimiterMiddleware)

# Include routers
app.include_router(auth.router)
app.include_router(products.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)