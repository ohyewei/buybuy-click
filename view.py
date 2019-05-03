from django.shortcuts import render_to_response


def homePage(request):
    return render_to_response('home.html')

def loginPage(request):
    return render_to_response('login.html')


def requirementPage(request):
    return render_to_response('requirement.html')


def orderPage(request):
    return render_to_response('order.html')
