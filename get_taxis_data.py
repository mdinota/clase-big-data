import requests

YEAR = 2015
TAXIS_BASE_URL = 'https://d37ci6vzurychx.cloudfront.net/trip-data'

for month in range(1, 13):
    month_str = str(month).zfill(2)
    month_file_name = f'yellow_tripdata_{YEAR}-{month_str}.parquet'
    month_url = f'{TAXIS_BASE_URL}/{month_file_name}'
    response = requests.get(month_url)
    with open(month_file_name, 'wb') as f:
        f.write(response.content)
    print(f'Downloaded {month_file_name}')
