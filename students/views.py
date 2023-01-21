from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import StudentForm
from .models import Student

def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/index.html', context)

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:index')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form, 'student': student})

def delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('students:index')
