def getParkingMinute(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(":"))
    out_hour, out_minute = map(int, out_time.split(":"))
    in_minute += in_hour * 60
    out_minute += out_hour * 60
    return out_minute - in_minute


def getUnit(parkingTime, defaultMinute, unitMinute):
    if (parkingTime - defaultMinute) % unitMinute:
        return (parkingTime - defaultMinute) // unitMinute + 1
    return (parkingTime - defaultMinute) // unitMinute


def solution(fees, records):
    answer = []
    parking_info = {}
    parking_fee = {}
    cars = []
    defaultMinute, defaultFee, unitMinute, unitFee = fees

    for record in records:
        time, carNum, info = record.split(" ")
        cars.append(carNum)
        if info == "IN":
            parking_info[carNum] = time
        elif info == "OUT":
            in_time = parking_info[carNum]
            parking_info[carNum] = ""
            parkingTime = getParkingMinute(in_time, time)
            if parking_fee.get(carNum):
                parking_fee[carNum] += parkingTime
            else:
                parking_fee[carNum] = parkingTime

    for key, value in parking_info.items():
        if value:
            parkingTime = getParkingMinute(value, "23:59")
            if parking_fee.get(key):
                parking_fee[key] += parkingTime
            else:
                parking_fee[key] = parkingTime

    cars = list(set(cars))
    cars.sort()
    for car in cars:
        if parking_fee[car] <= defaultMinute:
            answer.append(defaultFee)
        else:
            unit = getUnit(parking_fee[car], defaultMinute, unitMinute)
            answer.append(defaultFee + unit * unitFee)

    return answer