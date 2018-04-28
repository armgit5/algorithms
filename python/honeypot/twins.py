# https://www.hackerrank.com/tests/1jaj1jd66d5/questions/16jjpf1mcg2

def twins(a, b):

    # Check to see if elements in a and b are string
    for a_element in a:
        assert type(a_element) == str, "element in a is not string"
    for b_element in b:
        assert type(b_element) == str, "element in b is not string"

    # Make sure numbers of elements inside a and b are the same
    assert len(a) == len(b), "please make sure numbers of elements in a and b are equal"

    # Result array
    result = []

    # Loop to check each element one by one
    for i in range(len(a)):
        odd_a = []
        odd_b = []
        even_a = []
        even_b = []

        if len(a[i]) != len(b[i]):
            result.append("No")
            continue

        for j in range(len(a[i])):

            # even
            if j % 2 == 0:
                even_a.append(a[i][j])
                even_b.append(b[i][j])
            # odd
            if j % 2 != 0:
                odd_a.append(a[i][j])
                odd_b.append(b[i][j])

        odd_a.sort()
        odd_b.sort()
        even_a.sort()
        even_b.sort()

        if odd_a == odd_b and even_a == even_b:
            result.append("Yes")
        else:
            result.append("No")

    return result


a = ["cdab", "dcba", "abcd"]
b = ["abcd", "abcd", "abcdcd"]

print(twins(a, b))