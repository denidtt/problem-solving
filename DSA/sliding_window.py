def sliding_window(st):
    # find no-repeating characters in a string
    left = 0
    visited = set()
    max_len = 0
    max_string = ""
    for right in range(len(st)):
        while st[right] in visited:
            visited.remove(st[left])
            left = left + 1

        visited.add(st[right])
        print(visited)
        max_len = max(max_len, len(visited))
        if len(max_string) < right - left + 1:
            max_string = max(max_string, st[left:right + 1])
        print(max_string, " is the max now ")

    return max_len, max_string


# find the largest sum in the window of size k
def sum_of_k(arr, k):
    n = len(arr) - k + 1
    print(n)
    max_sum = 0
    for i in range(n):
        sum(arr[:n])
        max_sum = max(max_sum, sum(arr[i:n]))
        n += 1

    return max_sum


def min_len_of_sum(arr, target):
    left = 0
    curr_sum = 0
    min_len = float('inf')
    n = len(arr)
    for right in range(n):
        curr_sum+=arr[right]
        print(f"Left :{arr[left]} , Right : {arr[right]} , current sum : {curr_sum}")
        while curr_sum >= target:
            min_len=min(min_len,len(arr[left:right+1]))
            curr_sum-=arr[left]
            left+=1


    return min_len , curr_sum


print(min_len_of_sum([2, 3, 1, 2, 4,3], 7))
