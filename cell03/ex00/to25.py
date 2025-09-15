num_input = int(input('Enter a number less than 25\n'))
if num_input < 25:
    while True:
        print('Inside the loop, my variable is', num_input)
        num_input += 1
        if num_input == 25:
            break
else:
    print('Error')