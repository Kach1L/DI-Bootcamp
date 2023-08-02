def binary_search(array, value_to_search):

    middle = array[len(array) // 2]
    right = len(array)
    left = 0
    iteration = 0

    while True:
        iteration += 1

        if middle == value_to_search:
            print(f"FOUND SEARCH VALUE - {value_to_search}!")
            print(f"Iterations", iteration)
            break
        
        elif middle > value_to_search:
            right = middle
            middle = (left + right) // 2
            
        elif value_to_search > right or value_to_search < left:
            print('Value NOT IN RANGE')
            break
        
        elif middle > value_to_search:
            right = middle
            middle = (left + right) // 2

        else:
            print("NO SUCH VALUE")
            break

some_array = list(range(1000))
value = 1500

binary_search(some_array, value)

