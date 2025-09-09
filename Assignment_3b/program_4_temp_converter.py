
class TemperatureConverter:

    """returns the temperature to fahrenheit"""
    @staticmethod
    def celsius_to_fahrenheit(temp):
        return (1.8 * temp) + 32


    """returns the temperature in celsius"""
    @staticmethod
    def fahrenheit_to_celsius(temp):
        return (temp - 32) / 1.8


def main():

    t = TemperatureConverter()

    print("32^c in fahrenheit: ", t.celsius_to_fahrenheit(32))
    print("132^f in celsius: ", t.fahrenheit_to_celsius(132))

if __name__ == "__main__":
    main()