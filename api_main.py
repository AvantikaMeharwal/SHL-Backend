from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from recommendation_engine import recommend_assessments

app = FastAPI()

# CORS for frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the SHL Assessment Recommendation API"}

# Load dataset
catalog_df = pd.read_csv("shl_product_catalogue.csv")

# Input model
class QueryInput(BaseModel):
    query: str

# Recommend route
@app.post("/recommend")
def recommend(data: QueryInput):
    try:
        recommendations = recommend_assessments(data.query, catalog_df)
        return recommendations.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
