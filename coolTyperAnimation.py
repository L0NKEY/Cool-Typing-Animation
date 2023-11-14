import time
word = input()
i = int(0)
poop = len(word) - 1
while i <= poop:
    print(word[i], end='')
    i += 1
    time.sleep(0.3)