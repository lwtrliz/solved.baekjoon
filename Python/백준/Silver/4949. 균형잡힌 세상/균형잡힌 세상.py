std = ['(', '[', ')', ']']

while True:
    string_input = str(input())

    it_false = False

    check = []

    if string_input == '.':
        break

    for i in range(len(string_input)):
        if string_input[i] not in std:
            pass
        else:
            if string_input[i] == ')':
                if len(check) == 0:
                    check.append(string_input[i])
                elif check[-1] == '(':
                    check.pop()
                else:
                    it_false = True
                    break
            elif string_input[i] == ']':
                if len(check) == 0:
                    check.append(']')
                elif check[-1] == '[':
                    check.pop()
                else:
                    it_false = True
                    break
            elif string_input[i] == '(':
                if len(check) == 0:
                    check.append('(')
                elif check[-1] == "(" or check[-1] == '[':
                    check.append('(')
                else:
                    it_false = True
                    break
            elif string_input[i] == '[':
                if len(check) == 0:
                    check.append('[')
                elif check[-1] == "(" or check[-1] == "[":
                    check.append('[')
                else:
                    it_false = True
                    break
        if it_false == True:
            break

    if check != []:
        if check[-1] == ")" or "]":
            it_false = True

    if it_false == True:
        print('no')
    else:
        print('yes')