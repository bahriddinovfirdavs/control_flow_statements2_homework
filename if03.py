def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if b>a>c:
        return a
    elif a>b>c:
        return b
    elif a>c>b:
        return c
print(main(8,6,4))