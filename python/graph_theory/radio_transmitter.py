with open('radio_transmitter') as f:
    n, k = list(map(int, next(f).split()))

    houses = list(map(int, next(f).split()))
    houses.sort()

    i = 1
    ans = 0

    while i <= n:

        ans += 1

        max_radius = houses[i-1] + k
        j = i

        while j <= n and houses[j-1] <= max_radius:
            i = j
            j += 1

        max_radius = houses[i - 1] + k
        j = i

        while j <= n and houses[j-1] <= max_radius:
            i = j
            j += 1

        i += 1

    print(ans)

