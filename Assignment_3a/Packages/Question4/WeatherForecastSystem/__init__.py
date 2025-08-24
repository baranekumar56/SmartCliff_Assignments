
from forecast import get_forecast
from temperature import c_to_f, f_to_c
from alerts import get_alert

def main():
    city = input("Enter city:")
    forcast = get_forecast()

    print("City: ", city)
    print("Temperature: ", forcast['temp'])
    print("Rain Chance: ", forcast['rain'])

    alert = get_alert(forcast)

    if 'temp' in alert:
        print("ALERT: ", alert['temp'])

    elif 'rain' in alert:
        print("ALERT: ", alert['rain'])

    else:
        print("NO WEATHER ALERTS")

if  __name__ == "__main__":
    main()