from django.shortcuts import render, redirect
from django.http import HttpResponse
from .import service
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from client import utils as clientAppUtils

# Create your views here.
def filterCandidates(request):
    reasonsToRejectCandidate = models.ReasonToRejectCandidate.objects.all()
    company = models.Company.objects.all()
    candidates = models.CandidateProfile.objects.all()

    if request.method == "POST":
        companyName = request.POST["company"]
        print(companyName, "+++++")
    
    for candidate in candidates:
        candidateTimelineList = models.ShortlistedCandidateTimeline.objects.filter(shortlisted_Candidate=candidate.id)
        candidateProjectList = models.CandidateProject.objects.filter(candidate=candidate.id)
        candidateExperienceList = models.CandidateExperience.objects.filter(candidate=candidate.id)
        candidateEducationList = models.CandidateEducation.objects.filter(candidate=candidate.id)
        print(candidateTimelineList)
        print(candidateProjectList)
        print(candidateExperienceList)
        print(candidateEducationList)

        candidate.candidateTimelineList = candidateTimelineList
        candidate.candidateProjectList = candidateProjectList
        candidate.candidateExperienceList = candidateExperienceList
        candidate.candidateEducationList = candidateEducationList

    context = {
        "reasonsToRejectCandidate":reasonsToRejectCandidate,
        "candidates":candidates
    }

    return render(request, "filter.html", context)


@login_required(login_url="user-login")
def companyList(request):
    if clientAppUtils.isLoggedInUserIsClient(request.user):
        return render(request, "error-page.html", {
                "errorName":"Access Denied",
                "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
            })

    companyList = models.Company.objects.all()
    context = {
        "companyList":companyList,
    }
    return render(request, "company-list.html", context)


@login_required(login_url="user-login")
def companyProfile(request, id):
    if clientAppUtils.isLoggedInUserIsClient(request.user):
        return render(request, "error-page.html", {
                "errorName":"Access Denied",
                "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
            })
    
    companyProfileObject = models.Company.objects.filter(id=id).first()
    jobPostinglist = models.JobPosting.objects.filter(company=companyProfileObject)
    print(jobPostinglist)

    for jobPostingItem in jobPostinglist:
        shortlistedCandidateList = models.ShortlistedCandidate.objects.filter(job_posting= jobPostingItem)
        jobPostingItem.shortlistedCandidateList = shortlistedCandidateList
        jobPostingItem.number_of_candidates = len(shortlistedCandidateList)

        print(jobPostingItem.shortlistedCandidateList)
        for candidate in shortlistedCandidateList:
            candidateTimelineList = models.ShortlistedCandidateTimeline.objects.filter(shortlisted_Candidate=candidate.id)
            candidateProjectList = models.CandidateProject.objects.filter(candidate=candidate.id)
            candidateExperienceList = models.CandidateExperience.objects.filter(candidate=candidate.id)
            candidateEducationList = models.CandidateEducation.objects.filter(candidate=candidate.id)
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
        "jobPostLen":len(jobPostinglist),
    }

    return render(request, "company-profile.html", context)

def homeView(request):
    return render(request, "index.html", {"pageTitle":"Home"}) 

@login_required(login_url="user-login")
def searchView(request):
    if clientAppUtils.isLoggedInUserIsClient(request.user):
        return render(request, "error-page.html", {
                "errorName":"Access Denied",
                "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
            })

    applicationList = []
    applicationLst = []
    keywordsValue = ""

    if request.method == "POST":
        keywords = request.POST.get("keywords", None)
        keywordsValue = keywords
        keywordList =  keywords.split(",")
        
        for keyword in keywordList:
            applicationList += models.Application.objects.filter(application_text__icontains=keyword).values()

        for item in applicationList:
            if not (item in applicationLst):
                applicationLst.append(item)

    context = {
        "applicationList":applicationLst,
        "applicationLen":len(applicationLst),
        "keywordsValue":keywordsValue,
    }

    return render(request, "search.html", context = context)
    
    
@login_required(login_url="user-login")
def importApplicationView(request):
    if clientAppUtils.isLoggedInUserIsClient(request.user):
        return render(request, "error-page.html", {
                "errorName":"Access Denied",
                "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
            })
    
    if request.method == "POST":
        applicationList = request.FILES.getlist("applications")
        print("++++++")
        print(applicationList)
        for application in applicationList:
            print(application)
            print(service.convertPdfToText(application))
            applicationObj = models.Application(
                application = application, 
                application_name = application.name, 
                application_text = service.convertPdfToText(application),
                applicationOwner = request.user
            )
            applicationObj.save() 
            messages.success(request, f'Application Uploaded Sucessfully!')

    return render(request, "import.html", ) 