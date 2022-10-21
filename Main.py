from typing import List

def insertionSort(array) -> List[int]:
  for index in range(1, len(array)):
    key = array[index]    
    indexo = index - 1
    while indexo >= 0 and key < array[indexo]:
      array[indexo + 1] =  array[indexo]
      indexo -= 1
    array[indexo + 1] = key
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
