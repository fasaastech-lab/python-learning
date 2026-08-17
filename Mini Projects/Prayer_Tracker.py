"""
Daily Prayer Tracker

Requirements:
1. List of 5 daily prayers
2. Track which prayers are completed (use separate list)
3. Features:
   - Mark prayer as completed
   - Show remaining prayers
   - Show completion percentage
   - Print summary at end of day

Expected Output:
==========================================
DAILY PRAYER TRACKER
==========================================
1. Fajr     - ✓ Completed
2. Dhuhr    - ✗ Not completed
3. Asr      - ✓ Completed
4. Maghrib  - ✗ Not completed
5. Isha     - ✗ Not completed
------------------------------------------
Completed: 2/5 (40%)
Remaining: Dhuhr, Maghrib, Isha
==========================================
"""

# Create border and print title
print("="*40)
print('DAILY PRAYER TRACKER')
print("="*40)

# List containing all prayers and completed prayers
prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
completed_prayers = ['Fajr', 'Dhuhr', 'Asr']

# Empty list to store non-completed prayers
not_completed = []

# Loop to check and flag completed and non-completed prayers
for prayer in range(len(prayers)):
    if prayers[prayer] in completed_prayers:
        status = "✓ Completed"

    else:
        status = "✗ Not completed"
        not_completed.append(prayers[prayer])
    print(f"{prayer+1}. {prayers[prayer]} - {status}")

# print seperator line
print('-'*40)

# Display completed and remaining prayers
print(f'Completed: {len(completed_prayers)}/{len(prayers)} ' 
      f'({int(len(completed_prayers)/len(prayers)*100)}%)')
print(f"Remaining: {', '.join(not_completed)}")
print("="*40)