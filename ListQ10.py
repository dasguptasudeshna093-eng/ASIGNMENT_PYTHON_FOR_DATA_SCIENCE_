temperatures = [29.5, 31.0, None, 33.5, 34.0, 32.0, 35.5, 36.0, None, 30.5, 28.0, 37.0, 38.0, 34.5]
clean = []
missing_indices = []

for i in range(len(temperatures)):

    if temperatures[i] is None:
        missing_indices.append(i)
        continue
    clean.append(temperatures[i])


mean = sum(clean) / len(clean)
minimum = min(clean)
maximum = max(clean)
above_mean = []

for temp in clean:
    if temp > mean:
        above_mean.append(temp)

hot_days = 0

for temp in clean:
    if temp >= 35:
        hot_days += 1

current_run = 0
longest_run = 0

for temp in temperatures:
    if temp is not None and temp >= 35:
        current_run += 1
        if current_run > longest_run:
            longest_run = current_run
    else:
        current_run = 0


print("Clean temperatures:", clean)
print("Mean:", format(mean, ".2f"))
print("Minimum:", format(minimum, ".2f"))
print("Maximum:", format(maximum, ".2f"))

print("Above mean:", above_mean)
print("Hot days:", hot_days)
print("Longest consecutive hot run:", longest_run)
print("Missing indices:", missing_indices)
