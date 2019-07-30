def hex_num_to_char(hex_digit):

    above_nine = {10: 'A',
                  11: 'B',
                  12: 'C',
                  13: 'D',
                  14: 'E',
                  15: 'F'}
    if int(hex_digit) in above_nine:
        return above_nine[int(hex_digit)]
    else:
        return str(hex_digit)


def decimal_conversion(dec_number, base):

    bases = {'octal' : 8,
             'hexa'  : 16,
             'binary': 2}
    base_number = bases[base]
    numbers = []
    while dec_number >= base_number:
        numbers.append(str(dec_number%base_number))
        dec_number = int(dec_number/base_number)
    numbers.append(str(dec_number))
    if base == 'hexa':
        return "".join(map(hex_num_to_char, numbers[::-1]))
    else:
        return "".join(numbers[::-1]) 


def print_formatted(number):
    # your code goes here
    output_numbers = []
    for i in range(1, number+1):
        decimal = str(i)
        octal = decimal_conversion(i, 'octal')
        hexa = decimal_conversion(i, 'hexa')
        binary = decimal_conversion(i, 'binary')
        output_numbers.append((decimal, octal, hexa, binary))
    bin_len = len(list(output_numbers[-1][3]))
    for num in output_numbers:
        print('{dec:{width}}{octa:{width}}{hexa:{width}}{binary:{width}}'.format(dec=num[0], octa=num[1], hexa=num[2], binary=num[3], width=bin_len))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
