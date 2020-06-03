from web_scraping import __version__
from web_scraping.web_scraping import get_citation_needed, get_citation_needed_count, get_citation_needed_report

def test_version():
    assert __version__ == '0.1.0'

def test_get_citation_needed_count():
  actual = get_citation_needed_count('https://en.wikipedia.org/wiki/Police_brutality')
  expected = 8
  assert actual == expected

def test_get_citation_needed_report():
  actual = get_citation_needed_report('https://en.wikipedia.org/wiki/Python_(programming_language)')
  expected = [
    'Double precision floating point number. The precision is machine dependent but in practice is 64 bits.[citation needed]',
    "Due to Python's user-friendly conventions and easy-to-understand language, it is commonly used as an intro language into computing sciences with students.[citation needed]",
    'Nim uses indentation and a similar syntax.[citation needed]'
  ]
  assert actual == expected

