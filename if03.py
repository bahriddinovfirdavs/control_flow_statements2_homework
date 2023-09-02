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
    if b>a<c:
        return "First number."
    elif a>b<c:
        return "Second number."
    elif a>c<b:
        return "Third number."
print(main(8,6,4))