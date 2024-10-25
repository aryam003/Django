from django.urls import path
from . import views

urlpatterns=[
    path('a',views.fun1),
    path('disp_std',views.disp_std),
    path('add',views.add_std),
    path('edit_std/<id>',views.edit_std),
    path('delect/<id>',views.delete),
    
]