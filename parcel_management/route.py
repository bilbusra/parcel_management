import itertools
from parcel_management.department import Department

dep_array = [Department("Insurance"), Department("Heavy"), Department("Mail"), Department("Regular")]

class Route:
    id_iter = itertools.count()

    def __init__(self, parcel):
        self.id = next(Route.id_iter)
        self.parcel = parcel
        self.departments = []

        if parcel.value >1000:
            self.departments.append(dep_array[0])
            dep_array[0].coming_parcel()
        if parcel.weight > 10:
            self.departments.append(dep_array[1])
            dep_array[1].coming_parcel()
        if parcel.weight <= 1:
            self.departments.append(dep_array[2])
            dep_array[2].coming_parcel()
        if parcel.weight <= 10 and parcel.weight > 1:
            self.departments.append(dep_array[3])
            dep_array[3].coming_parcel()

