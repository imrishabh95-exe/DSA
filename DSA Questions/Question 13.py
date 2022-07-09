# Iterative python program to reverse an array
temp_list = [1,2,3,4,5]
def reverseAList(temp_list):
    reversed_list = []
    high_index = len(temp_list)-1
    while(high_index != -1):
        print(temp_list[high_index])
        reversed_list.append(temp_list[high_index])
        high_index -= 1

    return reversed_list

print(reverseAList(temp_list))