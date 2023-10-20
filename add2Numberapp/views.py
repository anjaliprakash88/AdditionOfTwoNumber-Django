from django.shortcuts import render
from django.http import HttpResponse
def sum(request):
    return render(request, 'sum.html')


def findsum(request):
    value1 = request.GET['number1']
    value2 = request.GET['number2']
    result = int(value1) + int(value2)
    return render(request, 'sum.html', {'res': result})



