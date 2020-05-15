
# Find block of time within calendars
# Times:
# T: 10     11      12      13      14      15
# A:    | ---------         ---     -----   |
# B:  | ----        ----    ----        ----|

# Constraints:

# - Within block of calendar time
#   - Find higher bound for earliest time
#   - Find lower bound for highest time
def getTimeBound(bound_tuples):
    if len(bound_tuples) == 0:
        return None
    time_bound = bound_tuples[0]
    for bound in bound_tuples[1:]:
        if time_bound[0] < bound[0]:
            time_bound[0] = bound[0]
        if time_bound[1] > bound[1]:
            time_bound[1] = bound[1]
    if (time_bound[0] > time_bound[1]) or (time_bound[0] > time_bound[1]):
        return None
    return time_bound

if __name__ == "__main__":
    pass