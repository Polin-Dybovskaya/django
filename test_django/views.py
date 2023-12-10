from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from test_django.models import Student, Lab, Tutor, Extra_Lessons
from test_django.forms import LabForm, EditLabForm
from django.views.generic import UpdateView

class Edit(UpdateView):
    model = Lab
    template_name = 'edit.html'
    fields = ['name', 'student', 'tutor','mark']
def show_extra_lessons(request, id):
    user = request.user
    try:
        (user.is_authenticated)
    except:
        return redirect("/error")
    try:
        if user.groups.get(name="Students"):
            student = Student.objects.get(id=id)
            extra_lessons = Extra_Lessons.objects.filter(student=student.id)
            return render(request, 'extra_classes.html', {'extra_lessons': extra_lessons})
    except:
        if user.groups.get(name="Tutors"):
            tutor = Tutor.objects.get(id=id)
            extra_lessons = Extra_Lessons.objects.filter(tutor=tutor.id)
            return render(request, 'extra_classes.html', {'extra_lessons': extra_lessons})
        else:
            return redirect("/error")


def show_info_student(request, id):
    user = request.user
    if user.is_authenticated:
        student = Student.objects.get(id=id)
        labs = Lab.objects.filter(student=student.id)
        labs = list(labs)
        extra_lessons = Extra_Lessons.objects.filter(student=student.id)
        try:
            if user == student.id_user or user.groups.get(name="Tutors"):
                return render(request, 'studentInfo.html',
                              {"student": student, "labs": labs, "extra_lessons": extra_lessons})
        except:
            return render(request, 'studentInfoNo.html',
                          {"student": student, "labs": labs, "extra_lessons": extra_lessons})
    else:
        return render(request, 'error.html')


def show_tutor(request, id):
    user = request.user
    try:
        (user.is_authenticated and user.groups.get(name="Tutors"))
    except:
        return redirect("/error")
    tutor = Tutor.objects.get(id=id)
    labs = Lab.objects.filter(tutor=tutor.id)
    labs = list(labs)
    extra_lessons = Extra_Lessons.objects.filter(tutor=tutor.id)
    if user.is_superuser or user == tutor.id_user:
        return render(request, 'tutorInfo.html', {"tutor": tutor, "labs": labs, "extra_lessons": extra_lessons})
    else:
        return render(request, 'tutorInfoNo.html', {"tutor": tutor, "labs": labs, "extra_lessons": extra_lessons})


def create_form(request, id):
    if request.method == "GET":
        labForm = LabForm()
        return render(request, "form.html", {"form": labForm})
    else:
        form = LabForm(request.POST)
        if form.is_valid():
            lab = form.save(commit=False)
            lab.tutor = Tutor.objects.get(id=id)

            lab.save()

            return redirect(f"/showt/{id}")
        else:
            print("NO")
            pass


def delete_form(request, tutor_id, lab_id):
    if request.method == 'GET':
        lab = Lab.objects.filter(id=lab_id).first()
        lab.delete()
    return redirect(f"/showt/{tutor_id}")


def edit_form(request, tutor_id, lab_id):
    if request.method == "GET":
        labForm = EditLabForm()
        return render(request, "edit.html", {"form": labForm})
    else:
        form = LabForm(request.POST)
        if form.is_valid():
            lab = form.save(commit=False)
            lab.tutor = Tutor.objects.get(id=tutor_id)
            lab.save()

            return redirect(f"/showt/{tutor_id}")
        else:
            print("NO")
            pass


def all_labs(request):
    if request.method == "GET":
        '''
        tutor = Tutor.objects.get(tutor)
        student = Student.objects.get(id=lab.student)
        labs = Lab.objects.filter(tutor=tutor.id, student=student.id)
        labs = list(labs)
        
        labs = Lab.objects.all().values()
        student_id = Student.objects.get()
        tutor_id = Tutor.objects.get()
        

        tutors=[]
        students=[]
        for lab in labs:
            tutor=Tutor.objects.get(tutor)

        labs = Lab.objects.all().values()
        tutor=Tutor.objects.get(labs.)
        labs = list(labs)
        return render(request, 'all_labs.html', {"labs": labs})

'''


# РЕГИСТРАЦИЯ
def show_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        if (request.POST.get("s_password_again") == None):  # login
            print("log")
            username = request.POST.get("l_login")
            password = request.POST.get("l_password")
            user = authenticate(username=username, password=password)
            try:
                login(request, user)
            except:
                return redirect("/error")
            return redirect("/home")
        else:  # registration
            first_name = request.POST.get("s_login_name")
            last_name = request.POST.get("s_login_surname")
            username = request.POST.get("s_username")
            password = request.POST.get("s_password")
            user = User.objects.create_user(first_name=first_name, username=username, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("/home")


# ИЗИ КОМАНДЫ

def error(request):
    return render(request, 'error.html')


def go_home_page(request):
    if request.method == "GET":
        return render(request, 'home.html')
