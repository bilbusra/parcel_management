import itertools

class Parcel:
    id_iter = itertools.count()

    def __init__(self, weight, value, recipient):
        if weight <= 0:
            raise ValueError("Weight must be bigger than 0")

        self.id = next(Parcel.id_iter)
        self.weight = weight
        self.value = value
        self.recipient = recipient


