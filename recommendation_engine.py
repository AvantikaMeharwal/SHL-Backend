import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_assessments(query, catalog_df):
    # Create synthetic description by combining 'key_skills' and 'suitable_roles'
    catalog_df["combined_text"] = (
        catalog_df["key_skills"].fillna("") + " " + catalog_df["suitable_roles"].fillna("")
    )

    # TF-IDF vectorization
    corpus = catalog_df["combined_text"].tolist()
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([query] + corpus)

    # Cosine similarity
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    top_indices = similarities.argsort()[-10:][::-1]

    # Return top assessments
    results = catalog_df.iloc[top_indices]
    return results[[
        "assessment_name",
        "category",
        "suitable_roles",
        "key_skills"
    ]]
