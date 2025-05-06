from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from recommendation_engine import recommend_assessments

app = FastAPI()

# Load dataset once at startup
catalog_df = pd.read_csv("shl_product_catalogue.csv")

class QueryInput(BaseModel):
    query: str

@app.post("/recommend")
def recommend(data: QueryInput):
    try:
        recommendations = recommend_assessments(data.query, catalog_df)
        return recommendations.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
