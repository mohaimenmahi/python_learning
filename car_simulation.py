status = 'stop'
while 1:
    text = input("> ")

    if text.lower() == 'help':
        print('start - start the car')
        print('stop - stop the car')
        print('quit - quit the program')
    elif text.lower() == 'start':
        if status != text.lower():
            print('Car Started!!')
            status = 'start'
        else:
            print('Car is started already. type "help" for more info')
    elif text.lower() == 'stop':
        if status != text.lower():
            print('Car stopped')
            status = 'stop'
        else:
            print('Car is stopped already. type "help" for more info')
    elif text.lower() == 'quit':
        break
    else:
        print('Invalid command. type "help" for more info')
