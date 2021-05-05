import requests
from bs4 import BeautifulSoup
import os


url = "https://lecturenotes.in/notes/10913-notes-for-programming-in-c-c-by-bibhuprasad-sahu"
sess = requests.Session()
r = sess.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
csrf_token = soup.find('meta', attrs={'name': 'csrf-token'})['content']
api_url = "https://lecturenotes.in/material/10913/page-{}?noOfItems=30"
headers = {
    'x-csrf-token': csrf_token
}
r = sess.get(api_url.format(31), headers=headers)
data = []
for x in range(1, 101, 30):
    r = sess.get(api_url.format(x), headers=headers)
    data.extend(r.json()['page'])

os.mkdir("lecture")
for row in data:
    image_url = "https://lecturenotes.in" + row['path']
    r = requests.get(image_url)
    
    with open("lecture/{}.jpg".format(row['pageNum']), 'wb') as f:
        f.write(r.content)

