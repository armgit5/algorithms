
delivery_ids = [1,2,3,4,5,6,7,8,9,1,2,3,4,6,7,8,9]


def find_unique_delivery_id(delivery_ids):
    ids_occurences = {}

    for id in delivery_ids:
        if id not in ids_occurences:
            ids_occurences[id] = 1
        else:
            ids_occurences[id] += 1

    for id, occurences in ids_occurences.items():
        if occurences == 1:
            return id


def find_unique_delivery_id_xor(delivery_ids):
    unique_id = 0

    for id in delivery_ids:
        unique_id ^= id

    return unique_id

# print find_unique_delivery_id(delivery_ids)
print((find_unique_delivery_id_xor(delivery_ids)))