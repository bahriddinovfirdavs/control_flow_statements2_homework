def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000 
    b=(n/1000)%10
    c=(n//100)%10
    d=(n//10)%10
    e=n%10
    m=a
    if b>m:
        m=b
    if c>m:
        m=c
    if d>m:
        m=d

    if e>m:
        m=e
    if m==a:
        return 5
    if m==b:
        return 4
    if m==c:
        return 3
    if m==d:
        return 2
    if m==e:
        return 1
print(main(int(input())))