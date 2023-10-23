from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='classes/')),
    path('classes/', views.class_list, name='class_list'),
    path('enroll/<str:class_code>/', views.enroll_class, name='enroll_class'),
    path('enrolled-classes/', views.enrolled_classes, name='enrolled_classes'),
    path('unenroll/<str:class_code>/', views.unenroll_class, name='unenroll_class'),
    path('login/', auth_views.LoginView.as_view(template_name='enrollment/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/enrollment/login'), name='logout'),
    path('register/', views.register, name='register'),
]
