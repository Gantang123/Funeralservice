from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage),
	path('ProjectPage', views.Item, name="ProjectPage"),
	path('second.html', views.Item, name="second.html"),
	path('third.html', views.Details, name="third.html"),
	path('fourth.html', views.Bayad, name="fourth.html"),
	path('fifth.html', views.Bagahe, name="fifth.html"),
	path('sixth.html', views.Suggestion, name="sixth.html")
]










# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views. homepage),
#     path('ProjectPage/', views.homepage, name="ProjectPage"),
# ]