class Recipient:
    def __init__(self, name, addr):
        if len(name) == 0:
            raise ValueError("Name must not be empty")
        self.addr = addr
        self.name = name