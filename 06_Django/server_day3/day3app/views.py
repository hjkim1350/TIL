from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "day3app/index.html")


def is_odd_even(request, num):
    result = ""

    if num == 0:
        result = str(num) + "은(는) 0입니다."
    else:
        if num % 2 == 1:
            result = str(num) + "은(는) 홀수입니다."
        elif num % 2 == 0:
            result = str(num) + "은(는) 짝수입니다."

    context = {
        "num": num,
        "result": result,
    }

    return render(request, "day3app/is-odd-even.html", context)


def calculate(request, num1, num2):
    result = ""
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = round(num1 / num2, 1)

    context = {
        "num1": num1,
        "num2": num2,
        "sum": sum,
        "sub": sub,
        "mul": mul,
        "div": div,
    }

    return render(request, "day3app/calculate.html", context)


def pastlife(request):
    return render(request, "day3app/pastlife.html")


def pastlife_result(request):
    name = request.GET.get("name")
    animals = ["개", "고양이", "앵무새", "낙타", "말", "용", "쥐", "이구아나"]
    animal = random.choice(animals)
    context = {
        "name": name,
        "animal": animal,
    }
    return render(request, "day3app/pastlife_result.html", context)


def ko_lipsum(request):
    return render(request, "day3app/ko_lipsum.html")


def ko_lipsum_result(request):
    nums = int(request.GET.get("nums"))
    word_nums = int(request.GET.get("word_nums"))

    words = ["사과", "바나나", "멜론", "포도", "망고", "파인애플", "망고스틴", "배", "자두", "블루베리", "라즈베리"]
    result = [[] for _ in range(nums)]

    for i in range(nums):
        for j in range(word_nums):
            word = random.choice(words)
            result[i].append(word)

    context = {
        "result": result,
    }

    return render(request, "day3app/ko_lipsum_result.html", context)
