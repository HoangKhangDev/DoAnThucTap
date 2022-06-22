from re import I
from django.urls import path, include
import hello.views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()




# To add a new path, first import the hello:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", include('hello.urls')),
<<<<<<< HEAD
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
=======
    path('admin/', admin.site.urls),


>>>>>>> 843860894f1f6e547d14ca5d1c62d731cda7b58f
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

