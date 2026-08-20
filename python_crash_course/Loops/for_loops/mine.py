# Exercise 21: Prayer Time Loop
# prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
# Print: "Time for [prayer] prayer" for each
# Your code here:
prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
times = ['5:40 am', '1:00 pm', '4:00 pm', '6:40 pm', '7:45 pm']
# Method 1

prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
times = ['5:40 am', '1:00 pm', '4:00 pm', '6:40 pm', '7:45 pm']

for i in range(len(prayers)):
    print(f"{prayers[i]} time is {times[i]}")

for prayer, time in zip(prayers, times):
    print(f"{prayer} time is {time}")
