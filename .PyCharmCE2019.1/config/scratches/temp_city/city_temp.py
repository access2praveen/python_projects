import requests

api_address='http://api.openweathermap.org/data/2.5/weather?q='
city = 'Mumbai'
url = api_address + city
app_id='&appid=0c42f7f6b53b244c78a418f4f181282a'
main_url=api_address + city + app_id
print(main_url)
json_data = requests.get(url).json()
format_add = json_data['temp']
print(format_add)