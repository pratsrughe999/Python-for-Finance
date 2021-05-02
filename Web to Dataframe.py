import bs4 as bs
import urllib.request

src = urllib.request.urlopen("https://www.nba.com/stats/players/passing/").read()
bsoup=bs.BeautifulSoup(src, 'lxml')

print (bsoup.title.text)

for link in bsoup.find_all('a'):
  print(link.get('href'))

print(bsoup.p)

print(bsoup.find_all('p'))

#print(bsoup.find('p').get_text())

ptags =bsoup.find_all('p')
for p in ptags:
  print(p.text)   #NLP processing, sentiment analysis

tbl =bsoup.find('table')
tbl_rows = tbl.find_all('tr')
for tr in tbl_rows:
  td = tr.find_all('td')
  row = [i.text for i in td]
  print(row)
type(row)

#Creating the dataframe of data
import pandas as pd
data = pd.read_html("Link")
for df in data:
  print(df)