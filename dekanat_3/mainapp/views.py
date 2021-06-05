from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from mainapp.models import Group, Student
from mainapp.forms import GroupForm


def index(request):
    context = {
        'page_title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def group_list(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
        'page_title': 'Группы'
    }
    return render(request, 'mainapp/groups.html', context)


def student_page(request, groups_pk):
    students = Student.objects.filter(groups_id=groups_pk)
    context = {
        'students': students,
        'page_title': 'Студенты'
    }
    return render(request, 'mainapp/student_page.html', context)


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            # form.save()
            return HttpResponseRedirect(reverse('mainapp:groups'))
    else:
        form = GroupForm()
    context = {
        'title': 'Добавить группу',
        'form': form,
    }
    return render(request, 'mainapp/group_add.html', context)
