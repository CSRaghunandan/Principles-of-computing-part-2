def slice(my_list, first, last):
    if first == last:
        return []
    else:
        if first != 0:
            my_list.pop(0)
            return slice(my_list, first - 1, last - 1)
        else:
            return [my_list.pop(0)] + slice(my_list, first, last - 1)


def Permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList
