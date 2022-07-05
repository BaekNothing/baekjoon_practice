while True :
    first, second = input().split()
    first = int(first)
    second = int(second)
    if(first == 0 and second == 0) :
        break
    if first > second and first % second == 0 :
        print("multiple")
    elif second > first and second % first == 0 :
            print("factor")
    else :
        print("neither") 
