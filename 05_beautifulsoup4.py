from bs4 import BeautifulSoup
import requests


url = "https://realpython.github.io/fake-jobs/"
page  = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# find by id
result = soup.find(id = "ResultsContainer")
#print(result.prettify())

# find_all return an iterable with all elements
job_elements= result.find_all("div", class_="card-content")

for el in job_elements:
    print(el.find("h2", class_="title").text.strip())

# find element by text content
python_jobs = result.find("h2", string="Python")

# pass a function to selector
python_jobs = result.find("h2", string=lambda text: "python" in text.lower())

python_jobs_grantparents = [h2_of_job.parent.parent.parent.parent for h2_of_job in python_jobs]

for el in python_jobs_grantparents:
    print(el["class"])