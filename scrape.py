import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

class Scrape:

  def get_soup(self, url):

    try: 
      html = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
      print("URLError", e.reason)
      html = "<html></html>"

    soup = BeautifulSoup(html, "lxml")

    return soup

  def get_dfs(self, soup):

    dfs = [pd.DataFrame()]
    if soup.find("table") == None:
      print("get_dfs: a table is not found.")
    else:
      dfs = pd.io.html.read_html(soup.prettify())

    return dfs

  def is_num(self, str_num):
    try:
      float(str_num)
    except ValueError:
      return False
    else:
      return Tru

if __name__ == '__main__':

  url = "https://db.netkeiba.com/race/200805040811/"
  s = Scrape()
  soup = s.get_soup(url)
  dfs = s.get_dfs(soup)

  print(dfs[0])