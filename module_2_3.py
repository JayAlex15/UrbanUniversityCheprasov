my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = 0
listLen = len(my_list)
while counter < listLen:
    if my_list[counter] == 0:
        counter = counter + 1
        continue
    elif my_list[counter] > 0:
        print(my_list[counter])
        counter = counter + 1
    else:
        break
