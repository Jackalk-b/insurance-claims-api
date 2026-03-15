from fastapi import FastAPI

app = FastAPI(
    title="Insurance Claims API",
    description="A backend API for managing insurance claims",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Insurance Claims API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}