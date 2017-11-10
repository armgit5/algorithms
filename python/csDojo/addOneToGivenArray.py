# https://www.youtube.com/watch?v=uQdy914JRKQ&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=2

arr = [1,9,9]
arr2 = [9,9,9]



def add_one(given_array):
    carry = 1
    result = [0] * len(given_array)

    for i in range(len(given_array)-1, -1, -1):
        sum = given_array[i] + carry
        if sum == 10:
            carry = 1
        else:
            carry = 0
            result[i] = sum % 10

    if carry == 1:
        result = [0] * (len(given_array) + 1)
        result[0] = 1

    return result


print(add_one(arr))
print(add_one(arr2))
