readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]
clean_readings =[]
alerts =[]

for num in readings:
    if num is None:
        continue
    if num < 0 or num > 50:
        continue
    clean_readings.append(num)
    if num > 30:
        alerts.append(num)

average = sum(clean_readings) / len(clean_readings)

print("Clean readings:", clean_readings)
print("Average:", round(average, 2))
print("Alerts:", alerts)
