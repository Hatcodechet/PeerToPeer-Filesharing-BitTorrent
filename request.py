from configs import CFG, Config
config = Config.from_json(CFG)

class DataPacket: #http request, #ensure data which is given, no exceed max size
    def __init__(self, src_port, dest_port, data):

        max_size = config.constants.MAX_HTTP_BODY_SIZE
        if len(data) > max_size:
            raise ValueError(
                f"Payload size {len(data)} exceeds maximum allowed size ({max_size})."
            )
        self.src_port = src_port
        self.dest_port = dest_port
        self.length = len(data)
        self.data = data
