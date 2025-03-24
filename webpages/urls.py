from django.urls import path
from .views import (
    homeView, 
    searchView, 
    importApplicationView, 
    companyProfile,
    companyList,
    filterCandidates,
    fileManager
)

urlpatterns = [
    path("", view=homeView, name="webpages-home"),
    path("search", view=searchView, name="webpages-search"),
    path("import", view=importApplicationView, name="webpages-import"),
    path("company-profile/<int:id>", view=companyProfile, name="webpages-company-profile"),
    path("company", view=companyList, name="webpages-company-list"),
    path("candidate-filter", view=filterCandidates, name="webpages-candidate-filter"),
    path("file-manager", view=fileManager, name="webpages-file-manager-home"),
]