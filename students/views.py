from django.shortcuts import render,redirect
# Create your views here.
from .models import Student
from .forms import StudentsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def student_list(request):
    stduents1 = Student.objects.filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(stduents1, 2)
    try:
        stduents = paginator.page(page)
    except PageNotAnInteger:
        stduents = paginator.page(1)
    except EmptyPage:
        stduents = paginator.page(paginator.num_pages)
    context ={'students':stduents}

    return render(request,'student/index.html',context)

def add_student(request):
    form = StudentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student')

    context = {'form': form}
    return render(request,'student/addstu.html',context)

def edit_student(request,sid=None):
    student = Student.objects.get(pk=sid)
    form = StudentsForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student')

    context ={'form':form}

    return render(request, 'student/editstu.html',context)


def view_student(request):
    sid =request.GET.get('sid')
    student = Student.objects.get(pk=sid)
    context = {'student': student}

    return render(request, 'student/viewstu.html',context)


