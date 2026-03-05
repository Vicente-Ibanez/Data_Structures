
def merge_two(U:list, V:list, S:list):
    """ Merge two subarrays U and V together onto S.
    Take the smaller of the two current items on either list
    and put it on S. When one list has no more items to compare,
    copy the remaining items from the other list to S.
    """
    u_len = len(U) # used to keep track of how many items we should copy from u
    v_len = len(V) # used to keep track of how many items we should copy from v
    
    u_current = 0 # keep track of current item to be copied next from u
    v_current = 0 # keep track of current item to be copied next from v

    # while there's still items to copy from both lists
    while (u_current < u_len) and (v_current < v_len): 

        # if the current U item is less than the current V item
        # copy U to the list and make u current the next item on u
        if U[u_current] < V[v_current]:
            S.append(U[u_current])
            u_current += 1
        # else the current U item is greater than (or equal to) the current V item
        # copy V to the list and make v current the next item on v
        else:
            S.append(V[v_current])
            v_current += 1

    # when either U or V are empty, copy the remaining items of the other
    # array onto S
    while u_current < u_len:
        S.append(U[u_current])
        u_current += 1
    while v_current < v_len:
        S.append(V[v_current])
        v_current += 1
    

def merge_sort(array: list, left:int, right:int):
    """ Standard merge sort that forms U and V from arr [ l .. m ] and arr [ m +1.. r ],
     then uses mergeTwo to merge into a temporary S and copies back.
    """
    
    if left >= right: # return if the array size/window is 0
        return 
    
    mid = left + (right - left) // 2 # get the midpoint to split the array as evenly as possible

    merge_sort(array, left, mid) # merge sort the left side of the array
    merge_sort(array, mid + 1, right) # merge sort the right side of the array

    # define the two subarrays that were just merge sorted
    # U is the left, V is the right
    U = array[left:mid+1] # python doesnt include the last item in splice, so add 1 to mid to include it
    V = array[mid + 1: right+1]
    S = [] # a temporary array used to merge the values from U and V together
    merge_two(U, V, S) # merge the two subarrays together onto S

    # copy the values from the temporary S array to the array
    placement = left # location where to copy the first value
    for i in S: # iterate over the values in the teporary array S
        array[placement] = i # place the value from S onto the array in the correct place
        placement += 1 # increment the placement 


if __name__ == "__main__":
    a = [6, 3, 8, 5, 2, 7]
    merge_sort(a, 0, len(a)-1)

    print(a)