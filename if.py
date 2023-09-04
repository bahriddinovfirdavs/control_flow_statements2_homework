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
    s=a
    if b>s:
        s=b
    if c>s:
        s=c
    return s
print(main(2,5,4))