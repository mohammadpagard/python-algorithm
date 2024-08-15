def rotate_string(sequence: str, value: int) -> str:
    result = sequence + sequence

    if value <= len(sequence):
        return result[value:value+len(sequence)]
    else:
        return result[value-len(sequence):value]
