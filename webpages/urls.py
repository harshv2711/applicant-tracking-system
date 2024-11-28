from django.urls import path
from .views import homeView, searchView, importApplicationView

urlpatterns = [
    path("", view=homeView, name="webpages-home"),
    path("search", view=searchView, name="webpages-search"),
    path("import", view=importApplicationView, name="webpages-import"),
]