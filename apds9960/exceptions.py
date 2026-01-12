class ADPS9960InvalidDevId(ValueError):
    def __init__(self, id, valid_ids):
        super().__init__("Device id 0x{:02x} is not a valid one (valid: {})!".format(id, ', '.join(["0x{:02x}".format(i) for i in valid_ids])))

class ADPS9960InvalidMode(ValueError):
    def __init__(self, mode):
        super().__init__("Feature mode {} is invalid!".format(mode))
