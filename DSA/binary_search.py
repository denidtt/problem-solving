def binary_search(arr, k):
    if arr==[]:
        return "Its an empty Array"
    low =0
    high =len(arr)-1
    while low < high :
        mid= low+(high-low) //2
        if k==arr[mid]:
            return "Element Found !"
        elif k<arr[mid]:
            high =mid
        else :
            low =mid

    return "element not in Array !"



print(binary_search([1,2,3,4],28))