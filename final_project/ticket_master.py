import ticketpy

# input api key

tm_client = ticketpy.ApiClient(consumer_key)

pages = tm_client.events.find(
    classification_name= 'Alternative Rock',
    city = 'San Diego',
    startDateTime = '2021-12-16T20:00:00Z',
    end_date_time= '2022-12-16T20:00:00Z'
).limit(10)

for event in pages:
    print(event.name, event.status, event.price_ranges, event.local_start_date, event.local_start_time)
