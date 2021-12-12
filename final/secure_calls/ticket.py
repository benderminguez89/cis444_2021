import ticketpy
from datetime import date
import os

now = date.today()

key = os.environ.get('TIX_API')


tm_client = ticketpy.ApiClient(key)

pages = tm_client.events.find(
    city='San Diego',
    startDateTime= str(now) +'T20:00:00Z',
    end_date_time='2022-12-16T20:00:00Z'
).limit(2)

print("\nUpcoming Events in San Diego:")
for p in pages:
    print(p.name)
