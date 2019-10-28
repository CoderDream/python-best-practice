from pandas import DataFrame
from dataapiclient import Client
import json
client = Client()
client.init('cae5c4acc4ad4ccb93a8aaac4b8adb04363feaa9852c34d14ddd2248613b09b3')
url='/api/equity/getEqu.json?field=ticker,secShortName,listDate,delistDate&listStatusCD=L,S,DE,UN&secID=&ticker=&equTypeCD=A'
code, result = client.getData(url)
j = json.loads(result.decode())
d = DataFrame(j['data'])
d = d.set_index('ticker')
d = d[['secShortName','listDate','delistDate']]
d.to_csv('data/ticker_and _day_of_(de)list_date.csv')