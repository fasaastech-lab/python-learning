numbers = {
    "Hafsah": [7054193512, 9092783080],
    "Abdulrahman": [9065405249],
    "Maryam": [7064588280],
    "Abdullateef": [7068657863, 9164689730],
    "Abdulraheem": [9012981955, 9034076786],
}

for name, number in numbers.items():
    print(f"\n{name}'s favourite number(s):")
    for num in number:
        print(f"\t{num}")
