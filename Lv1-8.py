import statistics as s
data = [12, 45, 83, 52]
avg = (s.mean(data) + s.median(data) + s.mode(data)) / 3
print("Average of mean, median, mode:", avg)