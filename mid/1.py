def rotate_element(list1, n):
    length = len(list1)
    n = n % length
    new_list = list1[-n:] + list1[:-n]
    return new_list


list1 = []

n_elements = int(input("Enter number of elements: "))
print("Enter Elements")

for i in range(n_elements):
    ele = int(input())
    list1.append(ele)

rotation = int(input("Enter your rotation: "))
result = rotate_element(list1, rotation)
print(f"The list after rotating {rotation} times is {result}")
