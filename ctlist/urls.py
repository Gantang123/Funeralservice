from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage),
	path('ProjectPage', views.Stores, name="ProjectPage"),
	path('Path', views.Item, name="Path"),
]










# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views. homepage),
#     path('ProjectPage/', views.homepage, name="ProjectPage"),
# ]