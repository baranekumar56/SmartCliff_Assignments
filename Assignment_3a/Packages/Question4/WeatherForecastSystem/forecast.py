
import random

def get_forecast():

    temp = random.randint(0, 100)
    rain = random.randint(0, 100)

    return {"temp": temp, "rain": rain}

