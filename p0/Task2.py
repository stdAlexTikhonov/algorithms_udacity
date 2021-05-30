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
hash = {}


for row in calls:
    if row[0] in hash.keys():
        hash[row[0]] += int(row[3])
    else:
        hash[row[0]] = int(row[3])

    if row[1] in hash.keys():
        hash[row[1]] += int(row[3])
    else:
        hash[row[1]] = int(row[3])
    
longest = 0
leader = ''
for key, value in hash.items():
    if value > longest:
        longest = value
        leader = key


print(str(leader) + " spent the longest time, " + str(longest) + " seconds, on the phone during September 2016.")

