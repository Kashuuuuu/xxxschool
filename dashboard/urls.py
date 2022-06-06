from django.contrib import admin
from django.urls import path,include
from dashboard import views

urlpatterns = [
   path('', views.ad_dash, name='ad_dash'),
   path('login',views.ad_login, name='login'),
   path('ad_logout',views.ad_logout, name='ad_logout'),
   path('event_management',views.event_man, name='event_man'),
   path('all_professors',views.all_prof, name='all_prof'),
   path('add_professor',views.add_prof, name='add_prof'),
   path('edit_professor/<int:myid>/',views.edit_prof, name='edit_prof'),

   path('professor_profile',views.prof_profile, name='prof_profile'),
   path('all_student',views.all_student, name='all_student'),
   path('add_student',views.add_student, name='add_student'),
   path('edit_student',views.edit_student, name='edit_student'),
   path('about_student',views.about_student, name='about_student'),
   path('all_course',views.all_course, name='all_course'),
   path('add_course',views.add_course, name='add_course'),
   path('edit_course',views.edit_course, name='edit_course'),
   path('about_course',views.about_course, name='about_course'),
   path('all_library',views.all_library, name='all_library'),
   path('add_library',views.add_library, name='add_library'),
   path('edit_library',views.edit_library, name='edit_library'),
   path('all_department',views.all_department, name='all_department'),
   path('add_department',views.add_department, name='add_department'),
   path('edit_department',views.edit_department, name='edit_department'),
   path('all_staff',views.all_staff, name='all_staff'),
   path('add_staff',views.add_staff, name='add_staff'),
   path('edit_staff',views.edit_staff, name='edit_staff'),
   path('staff_profile',views.staff_profile, name='staff_profile'),
   path('all_holiday',views.all_holiday, name='all_holiday'),
   path('add_holiday',views.add_holiday, name='add_holiday'),
   path('edit_holiday',views.edit_holiday, name='edit_holiday'),
   path('holiday_calender',views.holiday_calender, name='holiday_calender'),
   path('fees_collection',views.fees_collection, name='fees_collection'),
   path('add_fees',views.add_fees, name='add_fees'),
   path('fees_receipt',views.fees_receipt, name='fees_receipt'),
   path('app_profile',views.app_profile, name='app_profile'),
   path('email_compose',views.email_compose, name='email_compose'),
   path('email_inbox',views.email_inbox, name='email_inbox'),
   path('email_read',views.email_read, name='email_read'),
   path('forgot',views.forgot, name='forgot'),
   path('password_reset/<token>',views.password_reset, name='password_reset'),
   path('admin_profile',views.admin_prof, name='admin_profile'),
   path('edit_admin_profile/<int:pk>/',views.edit_admin_profile, name='edit_admin_profile'),













   
]
