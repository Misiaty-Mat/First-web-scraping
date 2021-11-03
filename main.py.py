from bs4 import BeautifulSoup
import requests

URL = "https://stacker.com/stories/1587/100-best-movies-all-time"

# Request a HTML file from URL
response = requests.get(URL)
response.raise_for_status()

# Getting readable code from requests object
top_movies_webside_code = response.text

# Making soup / Create object soup for web scraping
soup = BeautifulSoup(top_movies_webside_code, "html.parser")

# Select all tags with given selectors
title_tags = soup.select(".ct-slideshow__slide__text-container__caption > div")

# Reversing list for easier readability and getting rid of main title
title_tags.reverse()
title_tags.pop()

# Saving data to top_movies.txt
with open("top_movies.txt", "w") as file:
    for title in title_tags:
        # Deleting tags from text
        tagless_title = title.get_text()
        file.write(str(tagless_title) + "\n\n")
