import re
def validate_pin(pin):
    if (len(pin) > 6) or (len(pin) == 5): #too many or wrong number
        return False
    else:
        return bool(re.match("^\d{4}$|^\d{6}$",pin)) #4 or 6 digits
