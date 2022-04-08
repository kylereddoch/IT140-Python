user_input = input()
hourly_temperature = user_input.split()

ordered_temps = []
for temp in hourly_temperature:
    ordered_temps.append(temp)
    if not temp == hourly_temperature[-1]:
        ordered_temps.append(" -> ")
    else:
        ordered_temps.append(" ")
print("".join(map(str, ordered_temps)))
