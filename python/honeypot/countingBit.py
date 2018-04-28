# https://www.hackerrank.com/tests/1jaj1jd66d5/questions/bepl8kr7

# Complete the function below.

def getOneBits(n):
    # Check to see if n is integer
    assert type(n) == int, "input is not an integer"

    # Convert Dec to Binary
    n_bin_str_array = bin(n)[2:]
    # Cast n_bin_str string array to array of int
    n_bin_array = list(map(int, n_bin_str_array))

    # Keep track of how many 1's are in the array
    count = 0
    # Result array where the first element is count number of 1
    result_array = [count]

    # Loop n_bin integer array to see how many 1's and
    # the position of 1's
    for i in range(len(n_bin_array)):
        # Check to see if element in the array is 1
        # If so count increases by 1
        # and append index + 1 to the result array
        if n_bin_array[i] == 1:
            count += 1
            result_array.append(i + 1)

    result_array[0] = count

    return result_array


print(getOneBits(161))
