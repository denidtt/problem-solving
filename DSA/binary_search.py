def binary_search(arr, k):
    if arr==[]:
        return "Its an empty Array"
    low =0
    high =len(arr)-1
    while low <=high :
        mid= low+(high-low) //2
        if k==arr[mid]:
            return "Element Found !"
        elif k<arr[mid]:
            high =mid-1
        else :
            low =mid+1

    else:
        return "element not in Array !"



print(binary_search([],28))