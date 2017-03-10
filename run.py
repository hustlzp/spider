from lxml import html
import requests

r = requests.get("")
tree = html.fromstring(r.text)

# do the parse work
