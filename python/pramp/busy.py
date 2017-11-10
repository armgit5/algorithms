route = [[1487799425, 14, 1],  # 14
        [1487799425, 4, 0],  # 10
        [1487799425, 2, 0],  # 8 x
        [1487800378, 10, 1],  # 18 x
        [1487801478, 18, 0],  # 0
        [1487801478, 18, 1],  # 18 x
        [1487901013, 1, 0],  # 17 x
        [1487901211, 7, 1],  # 24
        [1487901211, 7, 0]]  # 17 x

def findBusiestPeriod(data):
    # your code goes here
    count = 0
    max = 0
    time = 0

    for i in range(len(data)):
        if data[i][2] == 1:
            count += data[i][1]
        elif data[i][2] == 0:
            count -= data[i][1]

        if i < len(data)-1 and data[i][0] == data[i+1][0]:
            continue

        if count > max:
            max = count
            time = data[i][0]

        print(data[i][0], count)

    return time


print(findBusiestPeriod(route))
