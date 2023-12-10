from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from test_django import views


urlpatterns = [
    path('error', views.error),
    path('', views.show_login, name='registration'),
    path('admin/', admin.site.urls),
    path('home', views.go_home_page, name='home'),
    path('infos/<int:id>', views.show_info_student),
    path('showt/<int:id>', views.show_tutor),
    path('showt/<int:tutor_id>/<int:lab_id>/deletelab', views.delete_form, name='delete_lab'),
    path('showt/<int:id>/addlab/', views.create_form, name='create_lab'),
    path('showt/<int:tutor_id>/<int:lab_id>/editlab', views.edit_form, name='edit_lab'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('registration')), name='logout'),
    path('labs/', views.all_labs),
    path('extra/<int:id>', views.show_extra_lessons, name='extra_classes'),
]
