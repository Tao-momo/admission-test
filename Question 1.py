def find_max (numbers):
    list = numbers
    largest_number = list[0]
    for i in list:
      if i > largest_number:
            largest_number = i
    return largest_number


print(find_max([1, 2, 4, 5])); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7



def find_position(numbers,target):
  target_index = []
  for i in range(len(numbers)):
    if numbers[i] == target:
      target_index.append(i)  
  if target_index == []:
    return -1
  else:
    return target_index


print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1