from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("topic/<int:topic_id>", views.topic, name="topic"),
    path("teacher/<int:teacher_id>", views.teacher, name="teacher"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("topic/<int:topic_id>/students", views.students, name="students"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("reselect/<int:topic_id>", views.reselect, name="reselect"),
    path("myinfo/<int:person_id>", views.myinfo, name="myinfo"),
]
