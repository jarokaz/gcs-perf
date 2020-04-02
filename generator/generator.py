import random

filename = 'bigfile.dat'

with open(filename, 'wb') as binary_file:
    for i in range(2**32):
        number = random.randint(0, 255)
        binary_file.write(number.to_bytes(1, 'big'))