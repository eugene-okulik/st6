temperatures = [
    20, 15, 32, 34, 21, 19,
    25, 27, 30, 32, 34, 30,
    29, 25, 27, 22, 22, 23,
    25, 29, 29, 31, 33, 31,
    30, 32, 30, 28, 24, 23
]
hot_temperatures = list(filter(lambda t: t if t > 28 else None, temperatures))  # ругается на отсутствие else
print(hot_temperatures)
print("The highest temperature is:", max(hot_temperatures))
print("The lowest temperature is:", min(hot_temperatures))
print("The middle temperature is:", (max(hot_temperatures) + min(hot_temperatures)) / 2)
