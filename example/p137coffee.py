coffee = 3
while 1:
    money = int(input('돈 주세요: '))
    if money == 300:        
        coffee -= 1
        print(f'커피드릴께요. 남은 커피 개수:{coffee}')
    elif money > 300:
        coffee -= 1
        print('달라는데로 줄 것이지....아닙니다. 거스름돈 %d을 드릴께요. 남은 커피 개수:%d'%(money-300,coffee))
    else:
        print('나를 뭘로보고... 돈을 다시 돌려드리고 커피는 앙데요.')
        print('남은 커피 개수:{num}'.format(num=coffee))
    if not coffee:
        print("커피가 없어요. 없다니까요... 사람 불러주세요.ㅠ")
        break