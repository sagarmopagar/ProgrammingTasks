str = input('Enter a sentence!: ')

search = input('Enter a search string: ')
listStr = []
len_of_str = len(str)

i = 0

while 0 <= i < len_of_str - 1:
    substr = ''
    for j in range(i, len_of_str, 1):
        lv_char = str[j]
        if lv_char == ' ':
            i = j+1
            break
        else:
            substr = substr + lv_char

    listStr.append(substr)

    if j == len_of_str - 1:
        break

if search in listStr:
    print(search, ' is found in ', str)
else:
    print(search, ' is not found in ', str)
