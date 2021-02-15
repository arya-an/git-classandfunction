from django.contrib import admin
from django.urls import path
from classbasedAPP.views import *
# from functionbasedAPP import views
from myapp import views
from myapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about/',MyView.as_view()),
    # path('create',GeekCreate.as_view(),name="home"),
    # path('list/',GeeksList.as_view()),
    # path('<int:pk>/',GeeksDetailView.as_view()),
    # path('<int:pk>/update',GeeksUpadateView.as_view()),
    # path('<int:pk>/delete',GeeksDeleteView.as_view()),
    # path('',GeeksFormView.as_view()),
    # path('',views.createview,name="createview")
    path('',views.createview,name="createview"),
   
    

]
