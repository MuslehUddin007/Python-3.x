import urllib.request
from urllib.parse import *

request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
# print(request_url.read())

parse_url = urlparse('https://www.geeksforgeeks.org/')
print(parse_url)
print("\n")
unparse_url = urlunparse(parse_url)
print(unparse_url)