def is_on_time(x):
    if x>=30:
        return "YES"
    else:
        return "NO"
T=int(input())
for _ in range(T):
    x=int(input())
    result=is_on_time(x)
    print(result)
