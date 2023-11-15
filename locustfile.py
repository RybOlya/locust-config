import locust

endpoints = [
    '/api/cities',
    '/api/clients',
    '/api/counties',
    '/api/ipaddresses',
    '/api/solarBatteries',
    '/api/solarPanels',
    '/api/solarSystems',
]

class UserPool(locust.FastHttpUser):
    @locust.task
    def flood_requests(self):
        for endpoint in endpoints:
            self.client.get(endpoint)
