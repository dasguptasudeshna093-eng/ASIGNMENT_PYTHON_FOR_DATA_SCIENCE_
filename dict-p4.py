
words = ["model", "data", "python", "data", "model", "analysis", "data"]
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1
repeated = []

for word in frequency:
    if frequency[word] > 1:
        repeated.append(word)

print("Frequency:", frequency)
print("Repeated words:", repeated)
