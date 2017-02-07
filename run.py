import lxml
import requests

r = requests.get("")
tree = html.fromstring(r.text)

# do the parse work
