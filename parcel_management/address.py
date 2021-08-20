class Address:
    def __init__(self, street, house_number, postal_code, city):

        if len(street) * len(house_number) * len(postal_code) * len(city) == 0:
            raise ValueError("All string values ")

        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city
