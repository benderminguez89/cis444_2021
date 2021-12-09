import ticketpy

# input api key
consumer_key = 'Scjv74PwIErH2jthOFDmmAZPE8f0OWGq'
consumer_secret = 'UqaDZZHtGLAQtIOV'
tm_client = ticketpy.ApiClient(consumer_key)

pages = tm_client.events.find(
    classification_name= 'Alternative Rock',
    city = 'San Diego',
    startDateTime = '2021-12-16T20:00:00Z',
    end_date_time= '2022-12-16T20:00:00Z'
).limit(10)

events = '{"concerts":['
for event in pages:
    if event[0] < len(pages):
        events += 'name' +str(event.name) + 
    print(event.name, event.status, event.price_ranges, event.local_start_date, event.local_start_time)
