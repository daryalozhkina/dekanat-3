from django.shortcuts import render

from mainapp.models import Group


def index(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
        'page_title': 'Группы'
    }
    return render(request, 'mainapp/index.html', context)
