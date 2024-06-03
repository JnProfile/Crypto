import abc


class APIExporter:
    def __init__(self, api_key):
        self.api_key = api_key
    
    @abc.abstractmethod 
    def make_request(self):
        pass
