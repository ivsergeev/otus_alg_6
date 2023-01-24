
def bubble_sort(items):
    last_idx = len(items)
    temp_val = None
    for j in range(len(items)):
        temp_idx = 0
        for i in range(1, last_idx):
            if items[i - 1] > items[i]:
                temp_val = items[i - 1]
                items[i-1] = items[i]
                items[i] = temp_val
                temp_idx = i
        last_idx = temp_idx
    return items
            
  
def insertion_sort(items):
    def binary_search(items, val, start, end):
        if start == end:
            if items[start] > val:
                return start
            else:
                return start+1
        if start > end:
            return start
    
        mid = (start + end)//2
        if items[mid] < val:
            return binary_search(items, val, mid+1, end)
        elif items[mid] > val:
            return binary_search(items, val, start, mid-1)
        else:
            return mid
    for i in range(1, len(items)):
        val = items[i]
        j = binary_search(items, val, 0, i-1)
        items = items[:j] + [val] + items[j:i] + items[i+1:]
    return items


def shell_sort(items):
    n = len(items)
    gap = n//2
    while gap > 0:  
        for i in range(gap,n):
            temp = items[i]
            j = i
            while  j >= gap and items[j-gap] >temp:
                items[j] = items[j-gap]
                j -= gap
            items[j] = temp
        gap //= 2       
    return items
