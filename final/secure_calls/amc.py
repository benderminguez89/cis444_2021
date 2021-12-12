import requests as req
import json
import os

key = os.environ.get('AMC_API')

now_playing = 'https://api.amctheatres.com/v2/movies/views/now-playing'
coming_soon = 'https://api.amctheatres.com/v2/movies/views/coming-soon'
local = 'https://api.amctheatres.com/v2/theatres?state=california&city=sandiego'
headers={'X-AMC-Vendor-Key': key}
response = req.get(now_playing, headers)
c_response = req.get(coming_soon, headers)

textResponse = response.text

data = json.loads(textResponse)
d = data["_embedded"]["movies"]

print("\nNOW PLAYING:")
for a in d:
    movie = a.get("sortableName")
    print(movie)

txtResponse = c_response.text

c_data = json.loads(txtResponse)
c_d = c_data["_embedded"]["movies"]

print("\nCOMING SOON:")
for b in c_d:
    c_movie = b.get("sortableName")
    print(c_movie)
