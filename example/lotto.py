def lotto():
    from random import randint
    lotto=[]
    while (len(lotto)<6):
        pick = randint(1,45)
        if pick not in lotto:lotto.append(pick)
    lotto.sort()
    return lotto
print(lotto())
print('에러체크를 시도하겠습니다.')
def ck(cycle):
    str = '■'      
    per = cycle // 100
    for k in range(cycle):
        out = lotto()
        ck = len(set(out))
        pr = (k+1)//per
        print(f'{pr:>3}% |{str * (pr):<100}|' ,end="\r")
        if ck != 6:
            print('\n',k+1,'번째 중복발생',out)            
            break
        if ck==6 and (k+1) == cycle:
            print('\n',k+1,'번 이상없이 체크완료')
ck(int(input('몇 회 검증할까요? 기본:100000')or 100000) )