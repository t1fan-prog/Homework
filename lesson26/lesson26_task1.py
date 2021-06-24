def bin_search_recur(array, first_index, last_index, val):

    if last_index < first_index:
        return False
    else:
        midpoint = first_index + ((last_index - first_index) // 2)

        if array[midpoint] > val:
            return bin_search_recur(array, first_index, midpoint - 1, val)
        elif array[midpoint] < val:
            return bin_search_recur(array, midpoint + 1, last_index, val)
        else:
            return True


a = [-100, -1.5, 2, 3, 4, 6, 31, 101]

print(bin_search_recur(a, 0, len(a) - 1, 31))
