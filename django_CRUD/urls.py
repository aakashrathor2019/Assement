from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
     path('',Login.as_view(),name='login'),
     path('show_emp',Show_Emp.as_view(),name='show_emp'),
     path('add_emp/',Add_Emp.as_view(),name='add_emp'),
     path('do_update/<int:emp_id>/',Do_Update.as_view(),name='do_update'),
     path('delete_emp/<int:emp_id>/',Delete_Emp.as_view(),name='delete_emp'),
     path('logout/',Logout.as_view(),name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
