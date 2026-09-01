#--> Web Scraper

# Http
# Ftp

#request
#httpx

#selenium
#playwright

#scrapy

#beautifulsoup - bs4
#re

# pandas
# pyspark

#-------------------------------------------------------------------------------------------------------
html_data = '''
<html>
<body>
<h1>Table title</h1>
<table class="Front-Page">
<tr>
<th>eno</th>
<th>ename</th>
<th>esal</th>
</tr>

<tr>
<td>100</td>
<td>sakeeb</td>
<td>10000</td>
</tr>

<tr>
<td>101</td>
<td>Sandesh</td>
<td>20000</td>
</tr>

<tr>
<td>102</td>
<td>Rahul</td>
<td>35000</td>
</tr>

</table>
</body>
</html>
'''

# from bs4 import BeautifulSoup
# import pandas as pd

# soup = BeautifulSoup(html_data, 'html.parser')
# # print(soup.find('table'))

# # print(soup.find_all('table'))
# heads = []
# for table in soup.find_all('table'):
#     all_rows = []
#     for tr in table.find_all('tr'):
#         # print(tr)
#         # print('---'*10)
#         row=[]
        
#         for th in tr.find_all('th'):
#             if th.get_text().strip():
#                 heads.append(th.get_text().strip())
#         # if row:
#         #     all_rows.append(row)
#         #     continue
        
#         for td in tr.find_all('td'):
#             # print(td.get_text(), end=', ')
#             if td.get_text().strip():
#                 row.append(td.get_text().strip())
#         if row:
#             all_rows.append(row)
#     print(all_rows)
# df = pd.DataFrame(all_rows, columns=heads)
# print(df)


# df = pd.read_html('data.html')[0]
# print(df)

# import io
# # BytesIO
# # StringIO

# df = pd.read_html(io.StringIO(html_data))[0]
# print(df)
#--------------------------------------------------------------

# import requests
# url = 'https://en.wikipedia.org/wiki/Wiki'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0'}
# response = requests.get(url, headers=headers)

# print(type(response.content))
# html_data = response.content.decode(encoding='utf-8')
# print(type(html_data))

# with open('wiki.html', 'wb') as fobj:
#     fobj.write(response.content)

# soup = BeautifulSoup(response.content.decode(), 'html.parser')
# print(soup.find('table', id="mwsg", attrs={"class":"wikitable noprint"}))



# soup = BeautifulSoup(html_data, 'html.parser')
# table  = soup.find('table')

# # print(table.get_text())
# print(table.get('class'))
# print(table['class'])

# import io
# df = pd.read_html(io.BytesIO(response.content))[0]
# print(df)
#===========================================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

# 1. Create options object
options = Options()

# 2. Add headless flags (use =new for modern Chrome)
options.add_argument("--headless=new")

# 1. Initialize the browser (Chrome in this example)
driver = webdriver.Chrome(options=options)

try:
    # 2. Open a website
    driver.get("https://en.wikipedia.org/wiki/Wiki")
    
    # 3. Locate an element (Google's search input box)
    search_box = driver.find_element(By.NAME, "search")
    
    # 4. Interact with the element
    search_box.send_keys("Python OOP")
    search_box.send_keys(Keys.RETURN)  # Simulates pressing Enter

    time.sleep(20)
    # 5. Extract data (Print the title of the new results page)
    print("Page Title is:", driver.title)

    # driver.page_source

finally:
    # 6. Always close the browser when finished
    driver.quit()