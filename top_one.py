"""Top one algorithm
    :variable counter: This dictionary count the repeated elements in the array.
    :variable max_reapeat: The value of this variable is the maximum repetition of the `counter`.
    :variable result: The elements of this array save the repetitions of the `array` parameter.

    e.g:
    [1, 2, 1, 3, 4, 2, 2, 2]
        counter = {'1': 2, '2': 4, '3': 1, '4': 1}
        max_repeat = 4
        result = [1, 2]
"""

def top_one(array: list) -> list:
    result = []
    counter = {}
    max_repeat = 0

    try:
        for val in array:
            if val not in counter:
                counter[val] = 1
            else:
                counter[val] += 1
                if val not in result:
                    result.append(val)

        max_repeat = max(counter.values())

        return result, max_repeat
    except ValueError:
        return ()
