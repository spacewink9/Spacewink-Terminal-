import requests
from bs4 import BeautifulSoup

def get_job_openings(company):
    """
    Returns a list of job openings for the given company
    """
    url = f"https://www.careersite.com/company/{company}-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    job_openings = []
    for job in soup.find_all("div", class_="job-tile"):
        title = job.find("h3").text.strip()
        location = job.find("div", class_="job-location").text.strip()
        description = job.find("div", class_="job-description").text.strip()
        job_openings.append({
            "title": title,
            "location": location,
            "description": description
        })
    return job_openings
