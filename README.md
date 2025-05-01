# Router Scrape

## Description and Initial Goals:

- Create a simple a table (.csv) containing the MAC, IP, and hostname of all network clients from the router's admin webpage

- Beautiful Soup can't handle this task since the router admin page requires authentication, and the content is dynamically generated on a tab'ed page. So I did a quick study on selenium to scrape the data, save the found elements to a pandas dataframe, and then export to a .csv. This router uses classes for each of the three desired elements, so the app simple finds each element based on the class name.

- This was a fun little learning experiment which has turned out to be pretty useful since my current DNS server (pi-hole) doesn't allow fpr the labeling of devices that don't report a hostname, or the reported hostname is meaningless

## Skills and Tech Used:

- Selenium, Pandas, Windows Chrome Selenium webdriver

## Results and Key Learnings:

- The code works as desired, probably a little better considering this one-time webscrape has become quite useful over time

- This was a fun way to learn Selenium and more advance web scraping concepts

## Roadmap:

- Nothing else planned for this project, but, the authentication and navigation to the dynamic content should be automated. Maybe some day...

## How to run:

- This simple app works with a tp-link BE9300 Router, but presumably should also work with any router by updating the names of the classes used to identify MAC, IP, and hostname (or divs or anything else unique to identify the desired elements).
- After creating a virtual environment, cloning the repo, and installing dependancies via requirements.txt, simply run 'python app.py'. 
- You will need to enter a password each time (if using admin page authentication), then manually navigate to the page with the desired content. You can adjust the sleeptime if required.

## Team Members
Mark Bercow
