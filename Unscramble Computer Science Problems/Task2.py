"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


num_durations_dict = {}

def increment_num_duration(num, duration):
    if (num not in num_durations_dict):
        num_durations_dict[num] = int(duration)
    else:
        num_durations_dict[num] += int(duration)
    
def check_row(data_row):
    increment_num_duration(data_row[0], data_row[3])
    increment_num_duration(data_row[1], data_row[3])
    
for calls_row in calls:
    check_row(calls_row)

num_with_max_duration = calls[0][0]
max_duration = num_durations_dict[num_with_max_duration]

num_with_max_duration = max(num_durations_dict, key = num_durations_dict.get)      
max_duration = num_durations_dict[num_with_max_duration]

print(f"{num_with_max_duration} spent the longest time, {max_duration} seconds, on the phone during September 2016.")