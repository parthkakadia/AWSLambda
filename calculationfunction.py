# Breakpoint concentration Table(http://www.arthapedia.in/index.php?title=National_Air_Quality_Index)
# ozone - 8 hourly, for concentration greater than 300 use 1 hourly data unit- microgram/m3
# pm10 24-hour, unit- microgram/m3
# pm2.5 24-hour, unit- microgram/m3
# no2 24 hour, unit- microgram/m3
# co 8 hour, unit- miligram/m3
# so2 24 hour, unit- microgram/m3


low = {'ozone': {1: 0, 2: 51, 3: 101, 4: 169, 5: 209},
       'pm10': {1: 0, 2: 51, 3: 101, 4: 251, 5: 351},
       'pm25': {1: 0, 2: 31, 3: 61, 4: 90, 5: 121},
       'no2': {1: 0, 2: 41, 3: 81, 4: 181, 5: 281},
       'co': {1: 0, 2: 1.1, 3: 2.1, 4: 10, 5: 17},
       'so2': {1: 0, 2: 41, 3: 81, 4: 381, 5: 801}}

high = {'ozone': {1: 50, 2: 100, 3: 168, 4: 208, 5: 748},
        'pm10': {1: 50, 2: 100, 3: 250, 4: 350, 5: 430},
        'pm25': {1: 30, 2: 60, 3: 90, 4: 120, 5: 250},
        'no2': {1: 40, 2: 80, 3: 180, 4: 280, 5: 400},
        'co': {1: 1.0, 2: 2.0, 3: 10, 4: 17, 5: 34},
        'so2': {1: 40, 2: 80, 3: 380, 4: 800, 5: 1600}}

aqilow = {1: 0, 2: 51, 3: 101, 4: 201, 5: 301}
aqihigh = {1: 50, 2: 100, 3: 200, 4: 300, 5: 400}


def calc(gas, key, conc):
    aqi = ((aqihigh[key] - aqilow[key]) / (high[gas][key] - low[gas][key])) * (conc - low[gas][key]) + aqilow[key]
    return aqi


def key(gas, conc):
    if gas == "ozone":
        if conc >= 0 and conc <= 50:
            key=1
        elif conc >= 51 and conc <= 100:
            key=2
        elif conc >= 101 and conc <= 168:
            key=3
        elif conc >= 169 and conc <= 208:
            key=4
        elif conc >= 209 and conc <= 748:
            key=5
        else:
            key=0
        aqi = calc(gas, key, conc)

    elif gas == "pm10":
        if conc >= 0 and conc <= 50:
            key=1
        elif conc >= 51 and conc <= 100:
            key=2
        elif conc >= 101 and conc <= 250:
            key=3
        elif conc >= 251 and conc <= 350:
            key=4
        elif conc >= 351 and conc <= 430:
            key=5
        else:
            key=0
        aqi = calc(gas, key, conc)

    elif gas == "pm25":
        if conc >= 0 and conc <= 30:
            key=1
        elif conc >= 31 and conc <= 60:
            key=2
        elif conc >= 61 and conc <= 90:
            key=3
        elif conc >= 91 and conc <= 120:
            key=4
        elif conc >= 121 and conc <= 250:
            key=5
        else:
            key=0
        aqi = calc(gas, key, conc)

    elif gas == "no2":
        if conc >= 0 and conc <= 40:
            key=1
        elif conc >= 41 and conc <= 80:
            key=2
        elif conc >= 81 and conc <= 180:
            key=3
        elif conc >= 181 and conc <= 280:
            key=4
        elif conc >= 281 and conc <= 400:
            key=5
        else:
            key=0
        aqi = calc(gas, key, conc)

    elif gas == "co":
        if conc >= 0 and conc <= 1.0:
            key=1
        elif conc >= 1.1 and conc <= 2.0:
            key=2
        elif conc >= 2.1 and conc <= 10:
            key=3
        elif conc >= 10 and conc <= 17:
            key=4
        elif conc >= 17 and conc <= 34:
            key=5
        else:
            key=0
        aqi = calc(gas, key, conc)

    else: #so2
        if conc >= 0 and conc <= 40:
            key=1
        elif conc >= 41 and conc <= 80:
            key=2
        elif conc >= 81 and conc <= 380:
            key=3
        elif conc >= 381 and conc <= 800:
            key=4
        elif conc >= 801 and conc <= 1600:
            key=5
        else:
            key=0
        aqi = calc(gas, key, conc)

    return aqi


#gas = input()
#conc = input()
#aqifinal = key(gas, float(conc))
#print("AQI= ", round(aqifinal))
