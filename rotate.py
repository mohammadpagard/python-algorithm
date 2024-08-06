def rotate_string(sequence: str, value: int) -> str:
    result = sequence + sequence

    if value <= len(sequence):
        return result[value:value+len(sequence)]
    else:
        return resut[value-len(sequence):value]

