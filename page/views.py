from django.shortcuts import render
import random
# Create your views here.

# 메인 페이지 뷰 작성하기! 
# home에서 로또 번호 입력하는 것은 templates home.html 에서 완료했기 때문에 여기서 다뤄줄 필요가 없다.
def home(request):
    return render(request, 'home.html')


# 결과 값 뷰 작성하기:

# 추가할 기능 :
# 1. 유저가 입력한 값들 리스트화 시키기.
# 2. 랜덤으로 6숫자 만들기(크기:45제한)
# 3. 유저 입력한 값과 추첨한 값 일치해서 몇개 맞췄는지 만들기.

def result(request): 

    # 1. 유저가 입력한 값 리스트화
    # cf] number_list는 result.html에 있는 input 집단 사용한 것 (24번째 줄)

    number_list = list()

    for a in range(6):
        number = request.GET['number' + str(a+1)]
        # append 함수를 사용해서 리스트에 input된 숫자들을 리스트에 첨가하기 #
        number_list.append(int(number))

 # 2. 랜덤으로 7숫자 만들기(보너스 때문에 7개)

    random_list = list()

    for b in range(7):
        number = random.randint(1,45)
        random_list.append(int(number))
         

 # 3. 일치 몇개 되나

    count = 0 

    for a in range (6):
        for b in range (7):
            if(number_list[a] == random_list[b]):
                count = count + 1


    return render(request, "result.html" , {'number_list':number_list, 'random_list':random_list, 'count':count})