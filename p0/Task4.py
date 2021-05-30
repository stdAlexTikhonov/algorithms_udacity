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

sending_texts = []
receiving_texts = []
receiving_calls = []
hash = {}

for text in texts:
    sending_texts.append(text[0])
    receiving_texts.append(text[1])

for call in calls:
    receiving_calls.append(call[1])

for call in calls:
    if call[0] not in sending_texts and call[0] not in receiving_texts and call[0] not in receiving_calls:
        hash[call[0]] = ''

telemarketers = sorted(hash.keys())

print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
    print(telemarketer)