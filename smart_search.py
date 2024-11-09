# smart_search.py

import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load course data
with open('courses.json', 'r') as f:
    courses = json.load(f)

# Load the language model
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
course_embeddings = model.encode([course['description'] for course in courses])

def search_courses(query):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, course_embeddings)[0]
    top_index = np.argmax(similarities)
    return courses[top_index]

# Test the function
if __name__ == "__main__":
    query = input("Enter your search query: ")
    result = search_courses(query)
    print("Top result:")
    print("Title:", result['title'])
    print("Description:", result['description'])
