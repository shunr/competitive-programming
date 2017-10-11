input()

memes = input().split()
s = 0
for meme in memes:
    if len(meme) <= 10:
        s += 1
print(s)