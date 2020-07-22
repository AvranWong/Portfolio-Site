from django.urls import path
from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('contact/',views.ContactView.as_view(), name= 'contact'),
    path('about/',views.AboutView.as_view(), name = 'about'),
    path('photography/',views.PhotographyView.as_view(), name = 'photography'),
    path('programming/',views.ProgrammingView.as_view(), name='programming'),
    path('',views.IndexView.as_view(), name = 'index'),
    path('thankyou/',views.ThankYouView.as_view(), name = 'thankyou'),
]
