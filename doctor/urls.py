from django.contrib import admin
from django.urls import path
from doctor.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('desbord', desbord,name="desbord"),
    path('error', error,name="error"),
    path('blog', blog,name="blog"),
    path('contact', contact,name="contact"),
    path('portfolio', portfolio,name="portfolio"),

]
