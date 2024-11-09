# scrape_data.py

import requests
from bs4 import BeautifulSoup
import json

def scrape_courses():
    url = "https://courses.analyticsvidhya.com/pages/all-free-courses"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    courses = []
    for course in soup.find_all('div', class_='course-card'):
        title = course.find('h3').get_text(strip=True)
        description = course.find('p', class_='course-desc').get_text(strip=True)
        courses.append({'title': title, 'description': description})

    with open('courses.json', 'w') as f:
        json.dump(courses, f, indent=4)

    print("Data saved to courses.json")

if __name__ == "__main__":
    scrape_courses()

