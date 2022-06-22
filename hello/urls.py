<<<<<<< HEAD
import hello.views
from django.urls import path, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("info_score/", hello.views.info_score, name="info_score"),
    path("score_training/", hello.views.score_training, name="score_training"),
    path("view_scoretraining/<str:Ma_CTPD>/", hello.views.view_scoretraining,
         name="view_scoretraining"),
    path("edit_scoretraining/<str:Ma_CTPD>/", hello.views.edit_scoretraining,
         name="edit_scoretraining"),
    path("delete_scoretraining/<str:Ma_CTPD>/",
         hello.views.delete_scoretraining, name="delete_scoretraining"),

    path("add_score/", hello.views.add_score, name="add_score"),
    path("search_score/", hello.views.search_score, name="search_score"),
    path("filter_lop/<str:malop>/", hello.views.filter_lop, name="filter_lop"),
    path("filter/<str:keyfilter>/", hello.views.filter, name="filter"),


    path("contact/", hello.views.contact, name="contact"),
    path("info_student/", hello.views.info_student, name="info_student"),
    path("change_password/", hello.views.change_password, name="change_password"),
    path("logout/", hello.views.logout, name="logout"),
    path("login/", hello.views.login, name="login"),
    path("change_password/", hello.views.change_password, name="change_password"),
    path("export_to_csv/", hello.views.export_to_csv, name="export_to_csv"),
    
    path('pdf_view/',hello.views.pdf_view, name="pdf_view"),
#     path('write_pdf_view/', hello.views.write_pdf_view, name="write_pdf_view"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
=======
from django.urls import path, include
import hello.views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("", hello.views.index, name='home'),
    path("test/", hello.views.test, name='test'),
    path("svm_imoc/", hello.views.svm_imoc, name='svm_imoc'),
    path("login/", hello.views.login, name='login'),
    path("logout/", hello.views.logout, name='logout'),
    path("process_test/", hello.views.process_test, name='process_test'),
]
>>>>>>> 843860894f1f6e547d14ca5d1c62d731cda7b58f
