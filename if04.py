def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a>b:
        return "First number."
    elif a==b :
        return 0
    else:
        return "Second number."
print(main(int(input()),int(input())))
    