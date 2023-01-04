
from django.urls import path
from . import views

urlpatterns = [
  path('',views.login,name='login'),
  path('signup',views.signup,name='signup'),
  path('home',views.home,name='home'),
  path('register',views.register,name='register'),
  path('ActionLogin',views.ActionLogin,name='ActionLogin'),
  path('logout',views.logout,name='logout'),
  path('admin_p',views.admin_p,name='admin_p'),
  path('adduser',views.adduser,name='adduser'),
  path('delete_user/<int:id>',views.delete_user,name='delete_user'),
  path ('adduserin',views.adduserin,name='adduserin'),
  path ('update_user/<int:id>',views.update_user,name='update_user'),
  path ('update_form/<int:id>',views.update_form,name='update_form'), 
  path('search_page', views.search_page, name='search_page'),
  path('search', views.search, name='search'),
]
