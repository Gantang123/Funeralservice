from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage),
		path('home', views.home, name="home"),
	path('Traditional', views.Traditional, name="Traditional"),
	path('Traditional', views.Traditional, name="Traditional"),
	path('ProjectPage', views.TraditionalInput, name="ProjectPage"),
	path('Submit', views.Payment, name="Submit"),
	path('Direct', views.Cremation, name="Direct"),
	path('Flower', views.Flower, name="Flower"),
	path('Other', views.Suggestion, name="Other"),
	path('CRUD', views.Starling, name="CRUD"),
	path('isip', views.Bura, name="isip"),
	path('delete/<int:int', views.Deletes)

	# path('third.html', views.Details, name="third.html"),
	# path('sixth.html', views.Suggestion, name="sixth.html"),
	# path('seventh.html', views.Starling, name="seventh.html")
]










# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views. homepage),
#     path('ProjectPage/', views.homepage, name="ProjectPage"),
# ]