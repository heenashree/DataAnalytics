from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage = 'https://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'
page = urllib.request.urlopen(urlpage)
soup=BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'class': 'tableSorter2'})
print(table)
results = table.find_all('tr')
print(results)