import random

first = ['andy', 'pete', 'tiger', 'cow', 'chicken']
second = ['jumps', 'jogs', 'plays', 'flys', 'drives']
third = ['slowly', 'happily', 'lazily', 'reluctantly']
chats = {

    "hello": "hello to you too.",
    "bye": "goodbye",
    "date": "now"
}
# for _ in range(10):
#     actions = f"{random.choice(first)} {random.choice(second)} {random.choice(third)}"
#     print(actions)
turn = "user"
while True:
    if turn == 'user':
        turn = 'computer'
        text = input("? ")
        for key in chats:
            if key in text:
                print(chats[key])
                break
        else:
            print('sorry I dont understand')
        if 'bye' in text:
            print('goodbye')
            break

    else:
        turn = 'user'
        actions = f"{random.choice(first)} {random.choice(second)} {random.choice(third)}"
        print(actions)
