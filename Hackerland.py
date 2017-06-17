x = [1, 2, 3, 4, 5]
x = [7, 2, 4, 6, 5, 9, 12, 11 ]
x = [9, 5, 4, 2, 6, 15, 12]

n = 7
k = 2

transmitters = 0
index = 0


def place_next_transmitter(index, transmitters):
    ''' given the index of a house ('h_a') in 
    the list, find the index of the furthest 
    house to the right ('h_b') where placing a 
    transmitter would reach 'h_a'.  Drop the 
    transmitter then return the next house to
    the right that is out of range of that transmitter
    '''
    h_a = x[index]
    boundary = h_a + k

    # Scan right in the list of houses until we've
    # gone just out of range or off the edge of the list,
    # then return to the previous house in the list,
    # which should be in range. Drop the transmitter there
    while x[index] <= boundary:
        index += 1
        # Avoid index error on next loop
        if index >= len(x):
            break
    index -= 1
    h_b = x[index]
    transmitters += 1

    # Reset the index to the first house to the right that
    # is not within range of the transmitter.
    new_boundary = x[index] + k
    if new_boundary >= x[-1]:
        return -100, transmitters

    while x[index] <= new_boundary:
        index += 1
        # Again, avoid index error on next loop
        if index > len(x):
            break

    return index, transmitters


while index != -100:
    index, transmitters = place_next_transmitter(index, transmitters)

print(transmitters)
