'''Counting sort'''

nums = [9,4,2,5,7,23,56,69,72,59,45,12,58,78,26,35,15,49,76,16,34,5]

def counting_sort(nums):
    minVal = min(nums)
    maxVal = max(nums)
    counts = []
    for i in range(minVal,maxVal+1):
        counts.append(0)
    for i in nums:
        counts[i-minVal]+=1
    new_nums = []
    for i in range(0,len(counts)):
        t = counts[i];
        if(t==0):
            continue
        else:
            while(t!=0):
                new_nums.append(i+minVal)
                t-=1
    return new_nums


nums = counting_sort(nums)
print(nums)