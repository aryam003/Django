from django.urls import path
from . import views

urlpatterns=[
    path('a',views.fun1),
    path('b',views.fun2),
    path('fun3/<a>/<b>',views.fun3),
    path('fun4/<int:a>',views.fun4),
    path('fun5/<int:a>/<int:b>/<int:c>',views.fun5),
    path('index',views.index_page),
    path('demo',views.demo),
    path('snd',views.snd),
    path('form',views.form),
]