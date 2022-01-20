from django.db.models import query
from django.shortcuts import render
from . models import todoModel


def home(request):
    todo = todoModel.objects.all()

    context = {
        'todo':todo
    }

    return render(request, 'core/index.html', context)