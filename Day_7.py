if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    k=1
    for i in arr:
        print(arr[-k],end=" ")
        k+=1

