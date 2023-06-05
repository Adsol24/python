temperature = int(input("what is the temperature of the water: "))

if temperature >= 0 and temperature <= 32:
    print("it is freezing")
elif temperature < 0:
    print("it is arctic")
elif temperature >= 50 and temperature <= 80:
    print("it is warm")
elif temperature >= 100 and temperature <= 140:
    print("it is hot but safe")
elif temperature >= 212:
    print("it is boiling")
elif temperature >= 140:
    print("it is hot and unsafe")
