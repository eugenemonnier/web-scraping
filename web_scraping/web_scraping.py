import requests
from bs4 import BeautifulSoup

def get_citation_needed(url):
  response = requests.get(url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  results = soup.find_all(title = 'Wikipedia:Citation needed')
  return results

def get_citation_needed_count(url):
  return len(get_citation_needed(url))

def  get_citation_needed_report(url):
  citation_report = list()
  for citation_needed in get_citation_needed(url):
    citation = citation_needed.parent.parent.parent.text.strip()
    citation_report.append(citation)
  return citation_report