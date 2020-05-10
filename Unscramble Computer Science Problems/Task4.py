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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_tele = {}

for call_row in calls:
    caller = call_row[0]
    called = call_row[1]

    if (possible_tele.get(caller) is None):
        possible_tele[caller] = True

    possible_tele[called] = False


for text_row in texts:
    texter = text_row[0]
    texted = text_row[1]

    possible_tele[texter] = False
    possible_tele[texted] = False

possible_list = []

for num in possible_tele:
    if (possible_tele[num] == True):
        possible_list.append(num)

final_possible_list = sorted(possible_list)

print("These numbers could be telemarketers: \n" + '\n'.join(final_possible_list) )