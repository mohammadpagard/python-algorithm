"""This algorithm return the minimum or maximum of your min or max choice
    :param array: That array you're going to through on it.
    :param min: The minimum integer you gave.
    :param max: The maximum integer you gave.

    It's through on array and returns items that you gave in min or max. e.g:

    [1, 2, 3, 4, 5]
        min 3   =>  [3, 4, 5]
        max 3   =>  [1, 2, 3]
        max, min 3  =>  [3]

"""

def limit_struct(array: list[int], min: int=None, max: int=None):
    result = []

    if (min != max) and (min or max):
        for val in array:
            if (min) and val >= min:
                result.append(val)
            elif (max) and val <= max:
                result.append(val)
    elif min is None:
        result = []
    else:
        result.append(min)

    return result

def limit_python(array: list[int], min: int=None, max: int=None):
    """
        Write a limit function with Python abilities.
        -lambda, list comprehensions-
    """

    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else (val <= max)
    return [val for val in array if min_check(val) and max_check(val)]


print(limit_struct([]))
