#percentages
def evaporator(content, evap_per_day, threshold):
    days = 0 
    amount = content 
    while amount > content*(threshold/100):
        amount = amount*(1-evap_per_day/100)
        days += 1
    return days
print (evaporator(10, 10, 10))
