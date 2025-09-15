num_input = float(input('Give me a number: '))
# round up to nearest integer
print(int(num_input) + (num_input % 1 > 0))