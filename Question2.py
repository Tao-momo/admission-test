def count(input):
    mySet = set(input)
    countOfChars = {}
    for element in mySet:
        countOfChar = 0
        for character in input:
            if character == element:
                countOfChar += 1
        countOfChars[element] = countOfChar
  
    return ("Count of characters is:",countOfChars)

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}



def group_by_key(input):
    result = {}
    for item in input:
        key = item['key']
        value = item['value']
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

    
input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2}, 
{'key': 'a', 'value': 3}, 
{'key': 'c', 'value': 5}
]


print(group_by_key(input2)) # should print {'a': 6, 'b': 1, 'c': 7}