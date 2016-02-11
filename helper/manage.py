from random import shuffle

with open("picAssets.txt", 'r') as assets:
    pics = ["Photos/" + l.strip() for l in assets]
    shuffle(pics)
    after = str(pics).replace("'", '"')
    print(after)