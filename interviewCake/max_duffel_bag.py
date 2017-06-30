# https://www.interviewcake.com/question/python/cake-thief?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email

cake_tuples = [(1,30), (50,200)]
capacity    = 100


def max_duffel_bag_value_with_capacity_1(cake_tuples, capacity):

    max_value = 0

    for weight, value in cake_tuples:
        if weight == 1:
            max_value = max(max_value, value)

    return max_value

def max_duffel_bag_value(cake_tuples, capacity):

    max_values_at_capacities = [0] * (capacity + 1)

    for current_capacity in range(capacity + 1):

        current_max_value = 0

        for weight, value in cake_tuples:

           if weight <= current_capacity:
               max_value_using_this_cake = value + max_values_at_capacities[current_capacity - weight]
               current_max_value = max(max_value_using_this_cake, current_max_value)

        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[capacity]




print(max_duffel_bag_value(cake_tuples, capacity))