
def get_alert(dic):

    alert = {}
    if dic['temp'] > 36:
        alert['temp'] = "Heat Wave alert"

    if dic['rain'] > 60:
        alert['rain'] = "Heavy Rain alert"

    return alert