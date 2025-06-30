def merge_sorted_arrays(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums2[p2] >= nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
    print(nums1[:p2 + 1], nums2[:p2 + 1])
    nums1[:p2 + 1] = nums2[:p2 + 1]
    print(nums1)


def removeElement(nums, val):
    result = 0
    i = 0
    n = len(nums)

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            nums.append('*')
            result += 1
        else:
            i += 1
    return n - result, nums


def removeDuplicates(nums):
    i = 0
    result = 0
    check = set()
    new_list = []
    while i < len(nums):
        print(nums[i])
        if nums[i] not in check:
            check.add(nums[i])
            new_list.append(nums[i])

        nums = new_list
    return nums


def strStr(haystack, needle):
    l = 0
    r = len(needle)

    while r <= len(haystack):
        if haystack[l:r] == needle:
            return l
        else:
            l += 1
            r += 1
    return -1


def majorityElement(nums):
    counter_map = {}
    n = len(nums) // 2
    for i in nums:
        counter_map[i]=counter_map.get(i,0) +1
        if counter_map[i] > n:
            print(counter_map[i])
            return i
    return -1

print(majorityElement([3, 2, 2]))
