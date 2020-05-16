from django.conf.urls import url
from django.urls import path
from login_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
app_name = "login_app"
urlpatterns =[
   path('',views.index,name='index'),
   path('login/',views.login_page,name='login'),
   path('register/',views.register,name='register'),
   path('user_login/',views.user_login,name='user_login'),
   path('logout/',views.user_logout,name='logout'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
