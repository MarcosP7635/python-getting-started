from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("neutrons-U238", hello.views.plot, name="plot")
    path("MathJax", hello.views.MathJax, name="MathJax")
    path("plotly_js", hello.views.plotly_js, name="plotly_js")

]
