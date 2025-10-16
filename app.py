from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return {"status": "running"}

@app.route('/scrape')
def scrape():
    # Exemple : on va juste récupérer les titres d’offres depuis un site d’exemple
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job_elem in soup.find_all("div", class_="card-content"):
        title_elem = job_elem.find("h2", class_="title")
        company_elem = job_elem.find("h3", class_="company")
        location_elem = job_elem.find("p", class_="location")
        if None in (title_elem, company_elem, location_elem):
            continue
        jobs.append({
            "title": title_elem.text.strip(),
            "company": company_elem.text.strip(),
            "location": location_elem.text.strip(),
        })

    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
