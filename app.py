# app.py

import gradio as gr
from smart_search import search_courses

def smart_search_interface(query):
    result = search_courses(query)
    return result['title'], result['description']

interface = gr.Interface(
    fn=smart_search_interface,
    inputs="text",
    outputs=["text", "text"],
    title="Smart Course Search",
    description="Search for free courses on Analytics Vidhya."
)

if __name__ == "__main__":
    interface.launch()
