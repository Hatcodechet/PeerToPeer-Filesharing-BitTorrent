import json

class Config:
    def __init__(self, directory, constants, tracker_requests_mode):
        self.directory = directory
        self.constants = constants
        self.tracker_requests_mode = tracker_requests_mode

    @classmethod
    def from_json(cls, cfg):
        params = json.loads(json.dumps(cfg), object_hook=JsonToObject)
        return cls(params.directory, params.constants, params.tracker_requests_mode)

class JsonToObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

CFG = {
    "directory": {
        "logs_dir": "logs/",
        "peer_files_dir": "peer_files/",
        "tracker_db_dir": "tracker_db/",
    },
    "constants": {
        "AVAILABLE_PORTS_RANGE": (1024, 65535),
        "TRACKER_ADDR": ('localhost', 8000),
        "MAX_HTTP_BODY_SIZE": 65536, # UDP usually use datagram (small) cannot exceed follow IPv4
        "BUFFER_SIZE": 8192,
        "CHUNK_PIECES_SIZE": 4096,
        "MAX_CONCURRENT_REQUESTS": 3,
        "PEER_TIME_INTERVAL": 20,
        "TRACKER_TIME_INTERVAL": 22,
    },
    "tracker_requests_mode": {
        "REGISTER": 0,
        "OWN": 1,
        "NEED": 2,
        "UPDATE": 3,
        "EXIT": 4,
        "SCRAPE": 5,
    }
}

