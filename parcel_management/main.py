from parcel_management.xml_handler import file_reader
from parcel_management.route import Route, dep_array

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]

    parcels = file_reader.reader(filename)
    routes = [Route(i) for i in parcels]
    department_list = [route.departments for route in routes]

    for route in routes:
        print(
            "Parcel route id: {0} , Parcel id: {1} , Value: {2} , Weight: {3} , Recipient: {4} \n PARCEL ROUTE IS: {5}  ".format(
                route.id,
                route.parcel.id,
                route.parcel.value,
                route.parcel.weight,
                route.parcel.recipient.name,
                [str(dep.name) for dep in route.departments],
            )
        )

    print("\n\n\n PARCEL COUNTS IN THE DEPARTMENTS ")
    for dep in dep_array:
        print(
            "{0} parcels are handled in the {1} Department".format(
                dep.parcel_count, dep.name
            )
        )
