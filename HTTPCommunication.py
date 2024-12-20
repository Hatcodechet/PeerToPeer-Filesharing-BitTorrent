import pickle # decode (deserialize), encode (serialize) byte string to send via network
import hashlib

class Message: #base class
    def __init__(self):
        pass
    def encode(self):
        return pickle.dumps(self.__dict__)
    
    @staticmethod
    def decode(data):
        return pickle.loads(data)
    
class ChunkSharing(Message): # data chunk: a small part of file
    def __init__(self, src_peer_id, dest_peer_id, filename, range, idx=-1, chunk=None):
        super().__init__()
        self.src_peer_id = src_peer_id
        self.dest_peer_id = dest_peer_id
        self.filename = filename
        self.range = range # range byte of chunk in a file
        self.idx = idx
        self.chunk = chunk

class Peer2Peer(Message):# data of file between 2 peer 
    def __init__(self, src_peer_id, dest_peer_id, filename, size=-1):
        super().__init__()
        self.src_peer_id = src_peer_id
        self.dest_peer_id = dest_peer_id
        self.filename = filename
        self.size = size

class Peer2Tracker(Message): # from peer to tracker
    def __init__(self, peer_id, mode, filename=""):
        super().__init__()
        self.peer_id = peer_id
        self.mode = mode
        self.filename = filename

class Tracker2Peer(Message):
    def __init__(self, dest_peer_id, search_results, filename):
        super().__init__()
        self.dest_peer_id = dest_peer_id
        self.search_results = search_results
        self.filename = filename
