# https://www.hackerrank.com/challenges/contacts/problem

queries = [['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']]


def contacts(queries):
    contacts_dict = {}
    output_list = []

    # Make dict iterating through all char in word
    def add(word):
        for i in range(1, len(word) + 1):
            key = word[:i]
            if key in contacts_dict:
                contacts_dict[key] += 1
            else:
                contacts_dict[key] = 1

    def find(word):
        if word in contacts_dict:
            return contacts_dict[word]
        else:
            return 0

    # Add contacts to list
    for q in queries:
        if q[0] == 'add':
            add(q[1])
        else:
            output_list.append(find(q[1]))

    return output_list

# print(contacts(queries))
# print('hack'[:4])
# hash = {'ck': 1}
# print(hash['ha'])
# print('hak' in 'hackker')

# h = {'acb': 1, 'b': 2}
# print('acb' in h)
#
# print('ABc'.lower())

print(5 % 5)