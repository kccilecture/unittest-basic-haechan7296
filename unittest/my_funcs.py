def is_even(n):
    return n % 2 == 0

def get_average(num_list):
    if not num_list:
        return 0
    return sum(num_list) / len(num_list)

def get_max(num_list):
    if not num_list:
        return None
    return max(num_list)

def get_min(num_list):
    if not num_list:
        return None
    return min(num_list)