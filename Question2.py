def count(input):
    mySet = set(input) #myset = {a,b,c,x}
    result = {}
    for element in mySet:
        count_char = 0
        for char in input:
            if char == element:
                count_char += 1 #count_chart = count_char+1
        result[element] = count_char
  
    return (result)


def count1(input):
    result = {}
    for char in input:
        if char in result:
            result[char] += 1 #result[key] = result[key]+1
        else:
            result[char] = 1 #result[key] = 1
    return ("count1",result)

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']

print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}
print(count1(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

print ("======我是分隔線======")

def group_by_key(input):
    result = {}
    for item in input:
        key = item['key']
        value = item['value']
        if key in result:
            result[key] += value #result[key] = result[key]+value
        else:
            result[key] = value #result[key] = value
    return result

    
input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2}, 
{'key': 'a', 'value': 3}, 
{'key': 'c', 'value': 5}
]


print(group_by_key(input2)) # should print {'a': 6, 'b': 1, 'c': 7}