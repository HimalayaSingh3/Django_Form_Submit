from django.contrib import admin
from django.urls import path
from Details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.form_view, name='form'),  # main form view
    path('success/', views.success_view, name='success'),
# redirect after form is saved
]
