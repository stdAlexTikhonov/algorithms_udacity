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
    hash[row[0]] = hash.get(row[0], 0) + int(row[3])
    hash[row[1]] = hash.get(row[1], 0) + int(row[3])
    
leader = max(hash, key = lambda k: hash[k])
longest = hash[leader]


print(str(leader) + " spent the longest time, " + str(longest) + " seconds, on the phone during September 2016.")

