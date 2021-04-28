
# Ship class
class Ship:
    def __init__(self):
        self.start_row = 0
        self.end_row = 0
        self.start_col = 0
        self.end_col = 0
        self.ship_number = ""
        self.ship_area = 0

# Make ships from string
def make_ships(S):
    ship_one_string = S.split(",")[0]
    ship_one_string_1 = ship_one_string.split(' ')[0]
    ship_one_string_2 = ship_one_string.split(' ')[1]

    ship_one = Ship()
    ship_one.start_row = int(ship_one_string_1[:-1]) - 1
    ship_one.end_row = int(ship_one_string_2[:-1]) - 1
    ship_one.start_col = int(convert_char_to_num_helper(ship_one_string_1[-1]))
    ship_one.end_col = int(convert_char_to_num_helper(ship_one_string_2[-1]))
    ship_one.ship_number = "one"
    ship_one.ship_area = (ship_one.end_row - ship_one.start_row + 1) * (ship_one.end_col - ship_one.start_col + 1)

    if (len(S.split(",")) == 2):
        ship_two_string = S.split(",")[1]
        ship_two_string_1 = ship_two_string.split(' ')[0]
        ship_two_string_2 = ship_two_string.split(' ')[1]

        ship_two = Ship()
        ship_two.start_row = int(ship_two_string_1[:-1]) - 1
        ship_two.end_row = int(ship_two_string_2[:-1]) - 1
        ship_two.start_col = int(convert_char_to_num_helper(ship_two_string_1[-1]))
        ship_two.end_col = int(convert_char_to_num_helper(ship_two_string_2[-1]))
        ship_two.ship_number = "two"
        ship_two.ship_area = (ship_two.end_row - ship_two.start_row + 1) * (ship_two.end_col - ship_two.start_col + 1)

    else:
        ship_two = Ship()

    return ship_one, ship_two

# Fill maxtrix by ship
def fill_matrix(ship, M):
    for i in range(ship.start_row, ship.end_row + 1):
        for j in range(ship.start_col, ship.end_col + 1):
            M[i][j] = ship.ship_number

# Shoot ships by T
def shoot_ships(T, M):
    shooting_points = convert_T_to_maxtrix_points_helper(T)
    ship_one_shot_count = 0
    ship_two_shot_count = 0

    for p in shooting_points:
        point = M[p[0]][p[1]]
        if point == 'one':
            ship_one_shot_count += 1
            point = 'x'
        if point == 'two':
            ship_two_shot_count += 1
            point = 'x'

    return ship_one_shot_count, ship_two_shot_count

def convert_char_to_num_helper(char):
    if char == 'A':
        return 0
    if char == 'B':
        return 1
    if char == 'C':
        return 2
    if char == 'D':
        return 3

def convert_T_to_maxtrix_points_helper(T):
    output = []
    points_string = T.split(" ")
    for p in points_string:
        row = int(p[:-1]) - 1
        col = convert_char_to_num_helper(p[-1])
        output.append((row, col))
    return output

def solution(N, S, T):
    # Init matrix
    M = [[0 for i in range(4)] for i in range(N)]
    ship_one, ship_two = make_ships(S)

    # Fill matrix with ships
    fill_matrix(ship_one, M)
    fill_matrix(ship_two, M)

    # Start shooting
    ship_one_shot_count, ship_two_shot_count = shoot_ships(T, M)

    print(M)

    # Check if ships hit or sunk
    sunks = 0
    hits = 0
    if ship_one_shot_count > 0:
        if ship_one_shot_count == ship_one.ship_area:
            sunks += 1
        else:
            hits += 1

    if ship_two_shot_count > 0:
        if ship_two_shot_count == ship_two.ship_area:
            sunks += 1
        else:
            hits += 1

    return str(sunks) + ',' + str(hits)

# N = 4
# S = "1B 2C,2D 4D"
# T = "2B 2D 3D 4D 4A"
# solution(N, S, T)
#
# # Test making ships
# ship_one, ship_two = make_ships(S)
# assert (ship_one.start_row, ship_one.end_row, ship_one.start_col, ship_one.end_col) == (0, 1, 1, 2)
# assert (ship_two.start_row, ship_two.end_row, ship_two.start_col, ship_two.end_col) == (1, 3, 3, 3)
# assert ship_one.ship_area == 4
# assert ship_two.ship_area == 3
#
# # Test points
# points = convert_T_to_maxtrix_points_helper(T)
# assert points == [(1, 1), (1, 3), (2, 3), (3, 3), (3, 0)]
#
# # print(solution(N,S,T))
#
# N = 3
# S = "1A 1B,2C 2C"
# T = "1B"
# expected = "0,1"
# assert solution(N,S,T) == expected
#
N = 12
S = "1A 2A,12A 12A"
T = "12A"
expected = "1,0"
# print(solution(N,S,T))
assert solution(N,S,T) == expected

print(solution(1, "1A 1A", "1A"))