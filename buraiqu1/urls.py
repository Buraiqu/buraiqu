from django.urls import path
from . import views
app_name='buraiqu1'
urlpatterns = [
    path('',views.buraiqu_web,name = 'web')
]