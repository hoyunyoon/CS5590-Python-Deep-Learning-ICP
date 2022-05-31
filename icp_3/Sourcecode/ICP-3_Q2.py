
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Machine_learning'

req = requests.get(url)

content = BeautifulSoup(req.content, 'html.parser')


# Print out the title of the page

print('Print out the title of the page : ', content.title.string)

# Find all the images links in the page (‘???’ tag) ->  ('img' tag)
images = content.find_all('img')
print('Find all the images links in the page ','\n')
print(images)

# Iterate over each tag(above) then return the link using attribute "???"(src) using get method
img_lst = []
for img in images:
    img_lst.append(img.get('src'))

print('\n')
print(img_lst)


