class MaxMin():
    def __init__(self):
        self.maxVal = 0
        self.minVal = 0

def calculateMaxMin(temp_lst: list) -> MaxMin:
    max_min_obj = MaxMin()
    if len(temp_lst) == 0:
        max_min_obj.maxVal = 0
        max_min_obj.minVal = 0
        return max_min_obj
    elif len(temp_lst) == 1:
        max_min_obj.maxVal = temp_lst[0]
        max_min_obj.minVal = temp_lst[0]
        return max_min_obj
    else:
        if temp_lst[0]>temp_lst[1]:
            max_min_obj.maxVal = temp_lst[0]
            max_min_obj.minVal = temp_lst[1]
        else:
            max_min_obj.maxVal = temp_lst[1]
            max_min_obj.minVal = temp_lst[0]
        for i in range(2, len(temp_lst)):
            if max_min_obj.maxVal < temp_lst[i]:
                max_min_obj.maxVal = temp_lst[i]
            if max_min_obj.minVal > temp_lst[i]:
                max_min_obj.minVal = temp_lst[i]
    return max_min_obj


temp_list = [1,2,3,4,5,6,10,7,13,35,2]
print(calculateMaxMin(temp_list).maxVal)
print(calculateMaxMin(temp_list).minVal)