def parking_lot_function(plate_records):
    parking_lot = set()
    for record in plate_number_records:
        command, car_plate = record.split(', ')

        if command == COMMAND_IN:
            parking_lot.add(car_plate)

        elif command == COMMAND_OUT:
            parking_lot.remove(car_plate)
    return parking_lot


def print_function(parking_lot_func):
    if parking_lot:
        for car in parking_lot:
            print(car)
    else:
        print('Parking Lot is Empty')


n = int(input())
plate_number_records = [input() for _ in range(n)]

COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

parking_lot = parking_lot_function(plate_number_records)
print_function(parking_lot)

# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU
