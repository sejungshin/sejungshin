T = int(input())
for _ in range(T) :
    string = input()
    answer = 'YES'
    cnt = 0

    for i in range(len(string)) :       
        if string[i] == '(' :    
            cnt = cnt + 1      
        else:
            cnt = cnt - 1
        if cnt < 0:
            answer = 'NO'
            break
    if cnt != 0 : answer = 'NO'
    print(answer)