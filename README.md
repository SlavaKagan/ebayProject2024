# ebayProject2024

## Contact
**Email:** slava.kagan.ht@gmail.com

## General info about the task
**GitHub repository:** https://github.com/SlavaKagan/ebayProject2024 <br />
**Programming Language:** Python (3.11.9) version https://www.python.org/ <br />
**Testing Framework:** Selenium- https://www.selenium.dev/ <br />
Package- "pytest" https://docs.pytest.org/en/8.2.x/ <br/>
Page Object Model (POM)- A design pattern in Selenium that creates an object repository for storing all web elements. <br/>
WebDriver-Chrome

## Abstract
Automated test suite using Python, Selenium, PyTest and Page Object Model that tests the search functionality on eBay website (https://www.ebay.com/). <br/>

## How to Run?
1. pip install selenium pytest webdriver-manager OR pip install -r requirements.txt
2. pytest tests/testSearch.py

## Core Functionality
1. Verifying that the eBay homepage loads correctly.
2. Searching for a specific item ("laptop") and verifying that the search results page is displayed.
3. Verifying that the search results contain the search term and find at least 10 results.
4. Verifying that the search results include the search term and contain at least 10 items.
* Assertions in every step.