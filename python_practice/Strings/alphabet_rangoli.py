import string


def print_rangoli(size):
    # your code goes here
    chars = list(string.ascii_lowercase[0:size])
    reverse_chars = chars[::-1]
    counter = 1
    change = 1
    width = 4*size-3
    while counter >=1:
        line_chars = "-".join(reverse_chars[:counter] + chars[size-counter+1:])
        if counter == size:
            change = -1
        counter += change
        print(line_chars.center(width, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
