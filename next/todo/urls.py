from django.urls import path , include
from .views import signupfunc ,loginfunc,listfunc, detailfunc, taskfunc
#  taskfuncCreate

urlpatterns = [
    path("signup/", signupfunc, name="signup" ),
    path("login/", loginfunc, name="login"),
    path("list/", listfunc , name="list"),
    path("detail/<int:pk>", detailfunc , name="detail"),
    # path("task/", taskfuncCreate.as_view() , name="task"),
    path("task/",taskfunc,name="task")
]
