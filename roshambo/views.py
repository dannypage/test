from django.shortcuts import render, render_to_response, RequestContext
from .utils import game


def index(request):
    return render_to_response("index.html", RequestContext(request,{}))


def round(request):

    option = request.POST.get('option','')
    if option in ['rock','paper','scissors']:
        result = game(option)
        return render(request, "round.html", {'result': result})
    else:
        return render(request, "round.html", {'result': "Either no value or an incorrect value was entered."})
