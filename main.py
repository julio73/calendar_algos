
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


# - Time passed in military hour as a string
#   - Convert it to integer for comparison
#   - Convert back for output
def getTimeParts(time_string):
    hour, minute = map(int, time_string.split(':'))
    return (hour, minute)


def getTimeDifference(time_string_a, time_string_b):
    if time_string_a == time_string_b:
        return (0, 0)
    else:
        hour_a, minute_a = getTimeParts(time_string_a)
        hour_b, minute_b = getTimeParts(time_string_b)
        time_diff = abs((hour_b * 60 + minute_b) - (hour_a * 60 + minute_a))
        diff_mins = time_diff % 60
        diff_hours = int((time_diff - diff_mins) / 60)
        return (diff_hours, diff_mins)

# - Time block should be within given bound
#   - Each bound is inclusive
def canContainDuration(time_a, time_b, duration):
    bound_hours, bound_minutes = getTimeDifference(time_a, time_b)
    duration_hours, duration_minutes = getTimeParts(duration)
    return (bound_hours * 60 + bound_minutes) >= (duration_hours * 60 + duration_minutes)




if __name__ == "__main__":
    pass