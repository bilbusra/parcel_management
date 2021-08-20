class Department:
    def __init__(self, name):
        self.name = name
        self.parcel_count = 0

    def coming_parcel(self):
        self.parcel_count += 1

