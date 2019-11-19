import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soap = BeautifulSoup(indeed_result.text,'html.parser')
#print(indeed_soap)

# print(indeed_soap.title)

pagination = indeed_soap.find("div", {"class":"pagination"})

#print(pagingation)

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
  pages.append(int(link.string))
  # print(page.find("span"))

max_pages = pages[-1]

#print(spans)
