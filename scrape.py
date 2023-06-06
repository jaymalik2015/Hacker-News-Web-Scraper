import requests
from bs4 import BeautifulSoup
import pprint

#"get" request to grab information from url page 
res = requests.get("https://news.ycombinator.com")
res2 = requests.get("https://news.ycombinator.com/?p=2")
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

#uses "select" to get both title and subtext 
links = soup.select(".titleline")
subtext= soup.select(".subtext")

links2 = soup2.select(".titleline")
subtext2 = soup2.select(".subtext")

#adds both links and subtext together from both pages for clearer code
mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k["votes"], reverse=True)



def create_custom_hn(links,subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get("href", None)
		vote = subtext[idx].select(".score")
		if len(vote):
			points = int(vote[0].getText().replace(" points", ''))
			if points > 99:
				hn.append({"title": title, "link": href, "votes": points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links,mega_subtext))