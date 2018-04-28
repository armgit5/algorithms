# https://www.hackerrank.com/challenges/strong-password/problem

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def minimumNumber(n, password):
    numbers_count = 0
    lower_case_count = 0
    upper_case_count = 0
    special_characters_count = 0

    for p in password:
        if p in upper_case:
            upper_case_count = 1
        if p in numbers:
            numbers_count = 1
        if p in lower_case:
            lower_case_count = 1
        if p in special_characters:
            special_characters_count = 1

    cases_count = numbers_count + lower_case_count + upper_case_count + special_characters_count
    cases_left = 4 - cases_count

    # print(cases_left)

    if n < 6:
        return max(cases_left, 6-n)

    if n >= 6:
        return cases_left

print(minimumNumber(3, "Ab1"))
print(minimumNumber(11, "#HackerRank"))
print(minimumNumber(2, "fe"))
print(minimumNumber(4, "4700"))
print(minimumNumber(6, "995606"))