number = 23
running = True

while running:
    guess = int(input('Enter a integer : '))

    if guess == number:
        print('yes')
        running = False
    elif guess < number:
        print('less')
    else:
        print('bigger')
else:
    print('over')

print('done')
