

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    

    result = max(arr)
    countResult = arr.count(result)
    
    for i in range(countResult):
        arr.remove(result)
    print(max(arr))
