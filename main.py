import random

Calls = [["snake eyes", "ace-deuce", "Little Joe", "Four Hoes and a pimp", "No fun", "Seven out"],
     ["ace-deuce", "Double deuce", "FIVE", "the lumber number", "Seven out", "EIGHT"],
     ["Little Joe", "FIVE", "SIX", "Seven out", "EIGHT", "Center field"],
     ["Four Hoes and a pimp", "the lumber number", "Seven out", "A square pair", "Jesse James", "sixty-four, out the door"],
     ["No fun", "Seven out", "EIGHT", "Jesse James", "Puppy paws", "Yo leven"],
     ["Seven out", "EIGHT", "Center field", "sixty-four, out the door", "Yo leven", "all the spots we got"]]

d1 = random.randrange(0,6)
d2 = random.randrange(0,6)

dt = d1 + d2 + 2

print(d1 + 1, d2 + 1)
print("" if dt % 2 != 0 else "Hard" if d1 == d2 else "Easy", dt, Calls[d1][d2])
