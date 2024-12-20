from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.contrib.auth.decorators import login_required
from webpages import models as webpagesModels
from .import models
from .utils import isLoggedInUserIsClient
from user.models import Profile


# Create your views here.
def clientHome(request):
    return render(request, "client/index.html")

@login_required(login_url="user-login")
def companyDashboard(request):
    # checking is logined user is client 
    if not isLoggedInUserIsClient(request.user):
        return render(request, "error-page.html", {
                "errorName":"Access Denied",
                "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
            })
    else:
        ClientViewPermissionObj = models.ClientViewPermission.objects.filter(client=request.user.id).first()

    # companyProfileObject = webpagesModels.Company.objects.filter(id=id).first()
    companyProfileObject = ClientViewPermissionObj.company_profile
    jobPostinglist = webpagesModels.JobPosting.objects.filter(company=companyProfileObject)
    print(jobPostinglist)

    for jobPostingItem in jobPostinglist:
        shortlistedCandidateList = webpagesModels.ShortlistedCandidate.objects.filter(job_posting= jobPostingItem)
        jobPostingItem.shortlistedCandidateList = shortlistedCandidateList
        jobPostingItem.number_of_candidates = len(shortlistedCandidateList)

        print(jobPostingItem.shortlistedCandidateList)
        for candidate in shortlistedCandidateList:
            candidateTimelineList = webpagesModels.ShortlistedCandidateTimeline.objects.filter(shortlisted_Candidate=candidate.id)
            candidateProjectList = webpagesModels.CandidateProject.objects.filter(candidate=candidate.id)
            candidateExperienceList = webpagesModels.CandidateExperience.objects.filter(candidate=candidate.id)
            candidateEducationList = webpagesModels.CandidateEducation.objects.filter(candidate=candidate.id)
            print(candidateTimelineList)
            print(candidateProjectList)
            print(candidateExperienceList)
            print(candidateEducationList)

            candidate.candidateTimelineList = candidateTimelineList
            candidate.candidateProjectList = candidateProjectList
            candidate.candidateExperienceList = candidateExperienceList
            candidate.candidateEducationList = candidateEducationList

    context = {
        "companyObject":companyProfileObject,
        "jobPostinglist":jobPostinglist,
        "jobPostLen":len(jobPostinglist)
    }

    return render(request, "client/dashboard.html", context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username'].replace(' ','_')
        email = request.POST['email'].replace(' ','')
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        
        # password and confirm password must be equal.
        if password == confirm_password:
            # username should not exists.
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username already taken.')
                return redirect('client-register')

            # check for email. if exists redirect to register page.
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, f"Email alread exists")
                    return redirect('client-register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    user_queryset = User.objects.filter(username=username).first()
                    profile = Profile(user=user_queryset)
                    profile.save()
                    messages.success(request, f'Account Created Sucessfully!')
                    return redirect('client-login')
        else:
            messages.error(request, f'Password Not Matching.')
            return redirect('client-register')

    return render(request, 'client/register.html', {'title': 'Sign Up'})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if not isLoggedInUserIsClient(request.user):
                messages.error(request, f'Use Staff login page to login as a Staff.')
                auth.logout(request)
                return redirect('client-login')
            messages.success(request, f'Welcome back {user.username}')
            return redirect('client-dasboard')
        else:
            messages.error(request, f'Invalid credentials')
            return redirect('client-login')

    return render(request, 'client/login.html')

def logout(request):
    auth.logout(request)
    return redirect('client-login')
    # return render(request, 'user/logout.html')
