
from .import models
from django.shortcuts import redirect, render

def isLoggedInUserIsClient(LoggedInUser):
    return models.ClientViewPermission.objects.filter(client=LoggedInUser).exists()


def redirectToClient(request):
    if not isLoggedInUserIsClient(request.user):
        return render(request, "error-page.html", {
                "errorName":"Access Denied",
                "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
        })