# https://www.youtube.com/watch?v=kHWy5nEfRIQ&index=11&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev

towers = [4,2,0,0,2,0]
towers2 = [1,3,5,3,1,0]

def next_step(current, towers):
    max_index = 0
    max_val = 0

    for i in range(current + 1, current + towers[current] + 1):
        if i >= len(towers):
            return i
        if towers[i] >= max_val:
            max_val = towers[i]
            max_index = i

    return max_index

# print(next_step(4, towers))
# print(next_step(0, towers))
# print(next_step(1, towers2))

def towerHopper(towers):
    current = 0
    while True:
        if current >= len(towers):
            return True
        if towers[current] == 0:
            return False
        current = next_step(current, towers)
        print(current)

print(towerHopper(towers))
print(towerHopper(towers2))
