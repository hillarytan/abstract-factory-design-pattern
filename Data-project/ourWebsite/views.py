from django.shortcuts import render
from django.http import HttpResponse
from .models import LAU, USEK, UOB, NDU, MU, AUB


# Create your views here.


def index(request):
    return render(request, "mainpage/index.html")

def majorFound(self, list1, list2):
    input = get_queryset(self)
    
    list = input.split()
    x = len(list1)
    for i in range(0, x-1):
        counter=0
        for word in list:
            if word.casefold() in list1[i].casefold():
                counter = counter + 1
            else:
                break
        if counter == len(list):
            major1 = [list1[i], list2[i]]   
            return major1 
    return ["Not available", "Not available"]


def search(self):
    input = get_queryset(self)
    if len(input) == 0:
        return render(self, "mainpage/searchException.html", {
            "strSearch": 'Error, no input provided'})
    university1 = LAU
    list1 = university1.createMajors()
    list11 = university1.createTuitionFees()
    major1list = majorFound(self, list1, list11)
    major1 = major1list[0]
    price1 = major1list[1]
    if price1 != "Not available":
        price1 = "$"+price1

    university2 = USEK
    list2 = university2.createMajors()
    list22 = university2.createTuitionFees()
    major2list = majorFound(self, list2, list22)
    major2 = major2list[0]
    price2 = major2list[1]
    if price2 != "Not available":
        price2 = "$"+price2

    university3 = UOB
    list3 = university3.createMajors()
    list33 = ["Not available"]*len(list3)
    major3list = majorFound(self, list3, list33)
    major3 = major3list[0]
    price3 = major3list[1]

    university4 = NDU
    list4 = university4.createMajors()
    list44 = university4.createTuitionFees()
    major4list = majorFound(self, list4, list44)
    major4 = major4list[0]
    price4 = major4list[1]
    if price4 != "Not available":
        price4 = "$"+price4

    university5 = MU
    list5 = university5.createMajors()
    list55 = university5.createTuitionFees()
    major5list = majorFound(self, list5, list55)
    major5 = major5list[0]
    price5 = major5list[1]
    if price5 != "Not available":
        len5 = len(price5)
        price5 = "$"+price5[0:len5-2]

    university6 = AUB
    list6 = university6.createMajors()
    list66 = ["Not available"]*len(list6)
    major6list = majorFound(self, list6, list66)
    major6 = major6list[0]
    price6 = major6list[1]
    
    return render(self, "mainpage/search.html", {
        "strSearch": input,
        "major1": major1,
        "price1": price1,
        "major2": major2,
        "price2": price2,
        "major3": major3,
        "price3": price3,
        "major4": major4,
        "price4": price4,
        "major5": major5,
        "price5": price5,
        "major6": major6,
        "price6": price6
    })


def get_queryset(self):
    query = self.GET.get("q")
    return query


def universities(request):
    return render(request, "mainpage/universities.html")


def home(request):
    return render(request, "mainpage/index.html")