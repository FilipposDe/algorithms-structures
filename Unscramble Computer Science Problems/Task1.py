"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

num_counts_dict = {}

def increment_num_count(num):
    num_counts_dict[num] = num_counts_dict.get(num, 0) + 1
    
def check_row(data_row):
    increment_num_count(data_row[0])
    increment_num_count(data_row[1])
    

for texts_row in texts:
    check_row(texts_row)
    
for calls_row in calls:
    check_row(calls_row)

print(f"There are {len(num_counts_dict)} different telephone numbers in the records.")