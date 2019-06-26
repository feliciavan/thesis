from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Topic, Teacher, Student, TeacherImage
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.models import User, Group
import datetime
from django.db.models import Q
import csv, traceback, os
from django.contrib import messages
from PIL import Image, ExifTags

Group.objects.get_or_create(name="student")
Group.objects.get_or_create(name="teacher")
stuno = 1
with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        obj, created = User.objects.get_or_create(username=row['username'],
            first_name=row['first_name'], last_name=row['last_name'],
            email=row['email'], is_staff=row['is_staff'], is_active=row['is_active'])
        my_group = Group.objects.get(name=row['group'])
        my_group.user_set.add(obj)
        obj.set_password(row['password'])
        obj.save()
        if row['group']=="student":
            Student.objects.get_or_create(person=obj,number=str(stuno).zfill(3), class_name="Commun. Eng.", gpa = row['gpa'])
            stuno += 1
        else:
            Teacher.objects.get_or_create(person=obj)

def index(request):
    # wrong user login info
    if not request.user.is_authenticated:
        context = {
            "time": datetime.datetime.now(),
        }
        return render(request, "selection/login.html", context)
    # user is student
    if request.user.groups.filter(name="student").count():
        if request.method == "GET":
            student = Student.objects.get(person=request.user)
            # this student has no topic
            if not student.author.first():
                context = {
                    "user": request.user,
                    "topics": Topic.objects.all(),
                    "time": datetime.datetime.now(),
                    "teachers": Teacher.objects.all(),
                    "flag": None,
                }
                return render(request, "selection/list.html", context)
            else:
                #this student has chosen one topic
                topic_id = student.author.first().id
                return HttpResponseRedirect(reverse("topic", args=[topic_id]))
        else:
            title = request.POST["topic"]
            topic = Topic.objects.get(title=title)
            student = Student.objects.get(person=request.user)
            topic.taker.add(student)
            topic.save()
            return HttpResponseRedirect(reverse("topic", args=[topic.id]))
    #user is teacher
    if request.user.groups.filter(name="teacher").count():
        teacher = Teacher.objects.get(person=request.user)
        context = {
            "topics": teacher.supervisor.all(),
            "time": datetime.datetime.now(),
            "user": request.user,
            "teacher_id": request.user.id,
        }
        return render(request, "selection/teacher_list.html", context)

def search(request):
    search = request.POST["search"]
    results =Topic.objects.filter(Q(title__contains=search)|Q(req__contains=search)|
        Q(output__contains=search)|Q(tool__contains=search)|Q(giver__person__username__contains=search))
    if len(results)==0:
        context = {
            "user": request.user,
            "topics": Topic.objects.all(),
            "time": datetime.datetime.now(),
            "teachers": Teacher.objects.all(),
            "message": "No such topic.",
        }
    else:
        context = {
            "topics": Topic.objects.all(),
            "user": request.user,
            "time": datetime.datetime.now(),
            "results": results,
            "teachers": Teacher.objects.all(),
        }
    return render(request,"selection/list.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        context = {
            "time": datetime.datetime.now(),
            "message": "Invalid credentials",
        }
        return render(request, "selection/login.html", context)

def logout_view(request):
    logout(request)
    context = {
        "time": datetime.datetime.now(),
    }
    return render(request, "selection/login.html", context)

def topic(request, topic_id):
    if request.method == "GET":
        try:
            topic = Topic.objects.get(pk=topic_id)
        except Topic.DoesNotExist:
            raise Http404("Topic does not exsit.")

        if request.user.groups.filter(name="student").count():
            student = Student.objects.get(person=request.user)
            # this student has no topic
            if not student.author.first():
                context = {
                    "topic": topic,
                    "user": request.user,
                    "time": datetime.datetime.now(),
                    "flag": None,
                }
                return render(request, "selection/topic.html", context)
            else:
                #this student has chosen one topic
                choose = student.author.first()
                if choose == topic:
                    messages.info(request, 'This is the thesis topic you have chosen.')
                context = {
                    "topic": topic,
                    "user": request.user,
                    "time": datetime.datetime.now(),
                    "flag": 0,
                }
                return render(request, "selection/topic.html", context)
        if request.user.groups.filter(name="teacher").count():
            teacher = Teacher.objects.get(person=request.user)
            context = {
                "topic": topic,
                "user": request.user,
                "time": datetime.datetime.now(),
                "flag": 1,
            }
            return render(request, "selection/topic.html", context)
    else:
        topic = Topic.objects.get(pk=topic_id)
        if request.user.groups.filter(name="student").count():
            student = Student.objects.get(person=request.user)
            topic.taker.add(student)
            topic.save()
        else:
            topic.delete()
        return HttpResponseRedirect(reverse("index"))

def reselect(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exsit.")

    student = Student.objects.get(person=request.user)
    topic.taker.remove(student)
    return HttpResponseRedirect(reverse("index"))

def teacher(request, teacher_id):
    try:
        user = User.objects.get(pk=teacher_id)
        teacher = Teacher.objects.get(person=user)
    except Teacher.DoesNotExist:
        raise Http404("Teacher does not exsit.")

    if request.user.groups.filter(name="student").count():
        student = Student.objects.get(person=request.user)
        if not student.author.first():
            context = {
                "teacher": teacher,
                "time": datetime.datetime.now(),
                "user": request.user,
                "flag": None,   #student, no topic
            }
        else:
            context = {
                "teacher": teacher,
                "time": datetime.datetime.now(),
                "user": request.user,
                "flag": 0,  #student, selected topic
            }
    else:
        context = {
            "teacher": teacher,
            "time": datetime.datetime.now(),
            "user": request.user,
            "flag": 1,  #teacher
        }
    return render(request, "selection/teacher.html", context)

def students(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
        student_num = request.POST["student"]
    except Topic.DoesNotExist:
        raise Http404("Topic does not exsit.")
    except KeyError:
        teacher = Teacher.objects.get(person=request.user)
        context = {
            "topics": teacher.supervisor.all(),
            "time": datetime.datetime.now(),
            "message": "No selection.",
            "user": request.user,
            "teacher_id": request.user.id,
        }
        return render(request, "selection/teacher_list.html", context)

    student = Student.objects.get(number=student_num)
    #send the chosen student an email
    subject, from_email, to = 'Here IS Your Thesis Topic', 'SOTT<sottbyfelicia@qq.com>', student.person.email
    html_content = render_to_string('selection/congrats_template.html', {'student':student, 'topic':topic.title, 'teacher':topic.giver}) # render with dynamic value
    text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
    # create the email, and attach the HTML version as well.
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    for one in topic.taker.all():
        if one != student:
            subject, from_email, to = 'Please Reselect Your Thesis Topic', 'SOTT<sottbyfelicia@qq.com>', one.person.email

            html_content = render_to_string('selection/email_template.html', {'student':one, 'topic':topic.title}) # render with dynamic value
            text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

            # create the email, and attach the HTML version as well.
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            topic.taker.remove(one)
    return HttpResponseRedirect(reverse("index"))

def add(request):
    title = request.POST["title"]
    req = request.POST["req"]
    output = request.POST["output"]
    tool = request.POST["tool"]
    teacher = Teacher.objects.get(person=request.user)
    topic = Topic(title=title,req=req,output=output,tool=tool,giver=teacher)
    topic.save()
    return HttpResponseRedirect(reverse("index"))


def myinfo(request, person_id):
    if request.user.groups.filter(name="student").count():
        student = Student.objects.get(person=request.user)
        topic = student.author.first()
        if request.method == "POST":
            try:
                uname = request.POST["uname"]
                pwd = request.POST["pwd"]
                email = request.POST["email"]
                if uname != '':
                    request.user.username = uname
                    request.user.save()
                if email != '':
                    request.user.email = email
                    request.user.save()
                if pwd != '':
                    request.user.set_password(pwd)
                    request.user.save()
                    return HttpResponseRedirect(reverse("login"))
            except:
                traceback.print_exc()
        if not topic:
            context = {
                "user": request.user,
                "time": datetime.datetime.now(),
                "flag": None,
                "student": student,
            }
        else:
            context = {
                "topic": topic,
                "user": request.user,
                "time": datetime.datetime.now(),
                "flag": 0,
                "student": student,
            }
        return render(request, "selection/infostudent.html", context)
    else:
        teacher = Teacher.objects.get(person=request.user)
        if request.method == "POST":
            old_degree = teacher.degree
            old_title = teacher.title
            old_major = teacher.major
            old_uni = teacher.uni

            form = TeacherImage(request.POST or None, request.FILES or None, instance=teacher)
            if form.is_valid():
                newform = form.save(commit=False)
                email = request.POST["email"]
                uname = request.POST["uname"]
                pwd = request.POST["pwd"]

                if newform.degree == '':
                    newform.degree = old_degree
                    newform.save()
                if newform.title == '':
                    newform.title = old_title
                    newform.save()
                if newform.major == '':
                    newform.major = old_major
                    newform.save()
                if newform.uni == '':
                    newform.uni = old_uni
                    newform.save()
                if email != '':
                    request.user.email = email
                    request.user.save()
                if uname != '':
                    request.user.username = uname
                    request.user.save()
                if pwd != '':
                    request.user.set_password(pwd)
                    request.user.save()
                    return HttpResponseRedirect(reverse("login"))
                newform.person = request.user
                newform.save()
                try:
                    image=Image.open(os.path.join(os.path.dirname(settings.PROJECT_DIR)) + newform.image.url)
                    if hasattr(image, '_getexif'): # only present in JPEGs
                        for orientation in ExifTags.TAGS.keys():
                            if ExifTags.TAGS[orientation]=='Orientation':
                                break
                        e = image._getexif()       # returns None if no EXIF data
                        if e is not None:
                            exif=dict(e.items())
                            orientation = exif[orientation]

                            if orientation == 3:   image = image.transpose(Image.ROTATE_180)
                            elif orientation == 6: image = image.transpose(Image.ROTATE_270)
                            elif orientation == 8: image = image.transpose(Image.ROTATE_90)

                    image.thumbnail((500, 500), Image.ANTIALIAS)
                    image.save(os.path.join(os.path.dirname(settings.PROJECT_DIR)) + newform.image.url)
                    print("hello")
                except:
                    traceback.print_exc()
        person = User.objects.get(pk=person_id)
        if person.groups.filter(name="teacher").count():
            context = {
                "teacher": teacher,
                "topics": teacher.supervisor.all(),
                "time": datetime.datetime.now(),
                "user": request.user,
                "flag": 1,
            }
            return render(request, "selection/infoteacher.html", context)
        else:
            context = {
                "user": request.user,
                "time": datetime.datetime.now(),
                "flag": 1,
                "student": Student.objects.get(person=person),
            }
            return render(request, "selection/infostudent.html", context)
