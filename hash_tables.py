from itertools import count
import string
print(string.ascii_uppercase)

text = 'A'*100_000
print(len(text))

'''print(hash('A'))
print(hash('A'))
print(hash('A'))'''

print(string.printable.strip())

from collections import Counter

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")

plot(distribute(string.printable, num_containers=2))
print(distribute(string.printable, num_containers=2))   

print(Counter([hash(item) % 2 for item in string.printable]))
print([hash(item) % 2 for item in string.printable])

dict = Counter([hash(item) % 5 for item in string.printable])
for key, value in dict.items():
    print(key,"■"*value, ' '*(max(dict.values()) - value), "(", value, ")")
    #print(hash(42))

print(ord(str(4)))

assert 2 + 2 == 5, "Houston we've got a problem"