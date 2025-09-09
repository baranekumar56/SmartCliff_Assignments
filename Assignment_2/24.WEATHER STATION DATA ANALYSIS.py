

def get_maxmin_temperature_and_humidity(hourly_temperatures, hourly_humidity):
    # we cant go beyond 275 deg fahrenheit or -100 deg celcius
    max_temperature = -500
    min_temperature = 1000

    max_humidity = -101
    min_humidity = 101

    for i in hourly_temperatures:
        max_temperature = max(i, max_temperature)
        min_temperature = min(i, min_temperature)

    for i in hourly_humidity:
        max_humidity = max(i, max_humidity)
        min_humidity = min(i, min_humidity)


    return max_temperature, min_temperature, max_humidity, min_humidity

def get_avg_temperature_and_humidity(hourly_temperature, hourly_humidity):

    return (sum(hourly_temperature) / len(hourly_temperature) ,  sum(hourly_humidity) / len(hourly_humidity) )

def get_exceeding_datapoints(hourly_temperature, hourly_humidity, temperature_threshold, humidity_threshold):

    exceeded_temperatures = []
    exceeded_humidity = []

    for i in hourly_temperature:
        if i > temperature_threshold: exceeded_temperatures.append(i)

    for i in hourly_humidity
        if i > humidity_threshold: exceeded_humidity.append(i)

    return exceeded_humidity, exceeded_temperatures


def main():
    temp_readings = list(map(int, input().split()))
    humi_readings = list(map(int, input().split()))

    temp_threshold = int(input())
    humi_threshold = int(input())

    print(get_maxmin_temperature_and_humidity(temp_readings, humi_readings))
    print(get_avg_temperature_and_humidity(temp_readings, humi_readings))
    print(get_exceeding_datapoints(temp_readings, humi_readings, temp_threshold, humi_threshold))



if __name__ == "__main__":
    main()


