def FindFirstNonRepeatingIndex(string):    index = -1    fnc = ""    if len(string) == 0 :      print("EMTPY STRING");         for i in string:        if string.count(i) == 1:            fnc += i            break        else:            index += 1    if index == len(string)-1 :        return -1    return string.index(fnc)        string='aafbbc'print(FindFirstNonRepeatingIndex(string))#Time Conmplexity - O(n*2)#Space Complexity - O(1)