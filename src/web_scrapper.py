import requests
from bs4 import BeautifulSoup
import mysql.connector

url = 'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                                                    "(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"})
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', id="ContentPlaceHolder1_gvbulk_deals")
rows = table.find_all('tr')

db = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="password@123",
    database="mydb"
)
cursor = db.cursor()
for row in rows[1:]:
    cells = row.find_all('td')
    data = [cell.text.strip() for cell in cells]

    query = "insert into bse_bulkdeals values (NULL, %s, %s, %s, %s, %s, %s, %s)"
    values = tuple(data)

    cursor.execute(query, values)
    db.commit()

db.close()
