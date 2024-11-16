def chef_points(T):
    points=[]
    for _ in range(T):
        X,N=map(int,input().split())
        points.append(X//10*N)
    return points
if __name__ ==  "__main__":
    T=int(input())
    result=chef_points(T)
    for point in result:
        print(point)
