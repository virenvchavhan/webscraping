from bs4 import BeautifulSoup, Tag
import requests
import mysql.connector

year = [2020,2021,2022,2023]
for yr in year:
  url = f'http://www.gameinformer.com/{yr}'
  
  response = requests.get(url)
  html_content = response.content

  soup = BeautifulSoup(html_content, 'html.parser')

  data = soup.find_all("span", class_="calendar_entry")

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Virenc@232",
    database="python"
  )

  cursor = mydb.cursor()

  for d in data:
      if type(d.em) == Tag:
        console = d.em.text
      else:
        console = "data unavailable"

      date = f'{d.time.text} {yr}'
      sql = "INSERT INTO gi_videogame (game, console, release_date) VALUES (%s, %s, %s)"
      values = (d.a.text, console, date)
      cursor.execute(sql, values)
      mydb.commit()

mydb.close()




