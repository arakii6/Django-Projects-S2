"""
URL configuration for DjangoProjects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Food.views import *
from University.views import *

urlpatterns = [

    # Food App
    path('',home,name = 'home_page'),
    path('add-recipe/',add_recipe,name = 'add_recipe_page'),
    path('show-recipe/',show_recipe,name = 'show_recipe_page'),
    path('update-recipe/<url_slug>/',update_recipe,name = 'update_recipe'),
    path('delete-recipe/<ID>/',delete_recipe,name = 'delete_recipe'),
    ## Auth
    path('register', register, name = 'register_page'),     
    path('sign-in', sign_in, name = 'sign_in_page'),
    path('sign-out', sign_out, name='sign_out_page'),

    # Univesity App
    path('student-details',student_list,name='student_details_page'),
    path('report-card/<student_id>',report_card,name='report_card_page'),

    # Django Admin
    path('admin/', admin.site.urls),
]


# Serve media files during development
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()