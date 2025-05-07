from rest_adapter import RestAdapter
from models.result import Result
from models.server import Server

screenScraper = RestAdapter(hostname='api.screenscraper.fr',ver='api2',ssl_verify=True)
params = {
    "devid": "***REMOVED***",
    "devpassword": "***REMOVED***",
    "softname": "Curatroid",
    "output": "json"
}
result = screenScraper.get(endpoint="ssinfraInfos.php", params=params)
# resultData = ScreenscraperServer(**result.data['response']['serveurs'])
server = Server.from_dict(result.data['response']['serveurs'])
print(server)