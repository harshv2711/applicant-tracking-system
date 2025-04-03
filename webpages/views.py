from django.shortcuts import render, redirect
from django.http import HttpResponse
from .import service
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from client import utils as clientAppUtils
from django.views.decorators.csrf import csrf_exempt

lst =  {
    ("Shortlisted", "Shortlisted"),
    ("Initial Communication", "Initial Communication"),
    ("HR Screening/Preliminary Interview", "HR Screening/Preliminary Interview"),
    ("Coordination for Technical/Functional Rounds", "Coordination for Technical/Functional Rounds"),
    ("Feedback and Follow-Up", "Feedback and Follow-Up"),
    ("Final Interview", "Final Interview"),
    ("Offer Rollout", "Offer Rollout"),
    ("Post-Interview Process", "Post-Interview Process"),
    ("Rejected", "Rejected")
}
interviewStatusList = []

num = 1
for interviewStatus in models.CandidateProfile.status_in_interview_choices:
    interviewStatusList.append({
        "interviewStatus":f"{interviewStatus[0]}",
        "id":num
    })
    num+=1

# Create your views here.
@login_required(login_url="user-login")
def filterCandidates(request):
    # checking is logined user is client
    if not request.user.is_superuser:
        if clientAppUtils.isLoggedInUserIsClient(request.user):
            return render(request, "error-page.html", {
                    "errorName":"Access Denied",
                    "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
                })
    
    print(interviewStatusList)
    reasonsToRejectCandidate = models.ReasonToRejectCandidate.objects.all()
    candidateSkillset = models.CandidateSkillset.objects.values('skill_name',"id")
    candidateRoleList = models.CandidateProfile.objects.values('role',"id")
    companyList = models.Company.objects.values('company_name',"id")
    ctcList = models.CandidateProfile.objects.values('ctc',"id")
    experienceList = models.CandidateProfile.objects.values('experience',"id")
    print("-_______")
    print(candidateRoleList)
    company = models.Company.objects.all().first()
    print(company, "company")
    # filter candidate based on company 
    # filter candidate based on Candidate Role
    # filter candidate based on Interview Status
    # filter candidate based on Candidate CTC
    # filter candidate based on Candidate Skillset
    # filter candidate based on Candidate Experience
    # filter candidate based on Reason to Reject Candidate
    candidates = models.CandidateProfile.objects.all()
    companyIdies = []
    role = []
    interviewStatus = []
    ctc = []
    skills = [
    ]
    experience = 0
    reasonsToReject = []
    if request.method == "POST":
        companyIdies = request.POST.getlist("company")
        role = request.POST.getlist("role")
        interviewStatus = request.POST.getlist("interviewStatus")
        ctc = ctc + request.POST.getlist("ctc")
        skills = request.POST.getlist("candidateSkillset")
        if len(request.POST.getlist("experience")) != 0:
            experience = max(request.POST.getlist("experience"))
        reasonsToReject = request.POST.getlist("reasonsToReject")
        print(request.POST.getlist("experience"), "+++++++++++++++++++++")

    candidatesBasedOnCompany = models.ShortlistedCandidate.objects.filter(company__in=companyIdies)
    candidates = [candidate.candidate for candidate in candidatesBasedOnCompany]
    print("shortlistedCandidateBasedOnCompany", candidatesBasedOnCompany)
    candidatesBasedOnCandidateRole = models.CandidateProfile.objects.filter(role__in=role)
    candidates += list(candidatesBasedOnCandidateRole)
    print("candidatesBasedOnCandidateRole", candidatesBasedOnCandidateRole)
    candidatesBasedOnInterviewStatus = models.CandidateProfile.objects.filter(status_in_interview__in=interviewStatus)
    for i in candidatesBasedOnInterviewStatus:
        candidates.append(i)

    print("candidatesBasedOnInterviewStatus", candidatesBasedOnInterviewStatus)
   
    if len(ctc) != 0:
        candidatesBasedOnCandidateCTC = models.CandidateProfile.objects.filter(ctc__lte=max(ctc))
        for i in candidatesBasedOnCandidateCTC:
            candidates.append(i)
        print("candidatesBasedOnCandidateCTC", candidatesBasedOnCandidateCTC)
  
    candidatesBasedOnCandidateSkillset = models.CandidateSkillset.objects.filter(skill_name__in = skills)
    for i in candidatesBasedOnCandidateSkillset:
        candidates.append(i.candidate)
    print("candidatesBasedOnCandidateSkillset", candidatesBasedOnCandidateSkillset)

    if experience != 0:
        candidatesBasedOnCandidateExperience = models.CandidateProfile.objects.filter(experience__lte=experience)
        for i in candidatesBasedOnCandidateExperience:
            candidates.append(i)
        print("candidatesBasedOnCandidateExperience", candidatesBasedOnCandidateExperience)
   
    candidatesBasedOnReasontoRejectCandidate = models.RejectedCandidate.objects.filter(reason_to_reject__in = reasonsToReject)
    for i in candidatesBasedOnReasontoRejectCandidate:
            candidates.append(i.candidate)
    print("candidatesBasedOnReasontoRejectCandidate", candidatesBasedOnReasontoRejectCandidate)

    
    for candidate in candidates:
        print(candidate.resume_file)
        candidateTimelineList = models.ShortlistedCandidateTimeline.objects.filter(shortlisted_Candidate=candidate.id)
        candidateProjectList = models.CandidateProject.objects.filter(candidate=candidate.id)
        candidateExperienceList = models.CandidateExperience.objects.filter(candidate=candidate.id)
        candidateEducationList = models.CandidateEducation.objects.filter(candidate=candidate.id)
        candidateSkillSetList = models.CandidateSkillset.objects.filter(candidate=candidate.id)
        print(candidateTimelineList)
        print(candidateProjectList)
        print(candidateExperienceList)
        print(candidateEducationList)
        print(candidateSkillSetList)
        candidate.ratinglist = [ i for i in range(0, int(candidate.candidate_rating))]
        candidate.candidateTimelineList = candidateTimelineList
        candidate.candidateProjectList = candidateProjectList
        candidate.candidateExperienceList = candidateExperienceList
        candidate.candidateEducationList = candidateEducationList
        candidate.candidateSkillSetList = candidateSkillSetList

    context = {
        "reasonsToRejectCandidate":reasonsToRejectCandidate,
        "candidateSkillset":candidateSkillset,
        "candidates":candidates,
        "candidateRoleList":candidateRoleList,
        "companyList":companyList,
        "interviewStatusList":interviewStatusList,
        "ctcList":ctcList,
        "experienceList":experienceList,    
    }

    return render(request, "filter.html", context)


@login_required(login_url="user-login")
def companyList(request):
    if not request.user.is_superuser:
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
    if not request.user.is_superuser:
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
    if not request.user.is_superuser:
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

    folders = models.Folder.objects.all()
    for folder in folders:
        folder.files = models.File.objects.filter(folder=folder)
        print(folder.files)

    context = {
        "applicationList":applicationLst,
        "applicationLen":len(applicationLst),
        "keywordsValue":keywordsValue,
        "folders":folders,
    }

    return render(request, "search.html", context = context)
    
    
@login_required(login_url="user-login")
def importApplicationView(request):
    folderList = models.Folder.objects.all()

    if not request.user.is_superuser:
        if clientAppUtils.isLoggedInUserIsClient(request.user):
            return render(request, "error-page.html", {
                    "errorName":"Access Denied",
                    "errorDescription":"You do not have the required permissions to access this section of the dashboard. If you believe this is an error, please contact your administrator or support team for assistance."
                })
    
    if request.method == "POST":
        applicationList = request.FILES.getlist("applications")
        folderId = request.POST["folderId"]
        folderObj = models.Folder.objects.filter(id=folderId).first()

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
            fileObj = models.File(folder=folderObj,file=applicationObj)
            fileObj.save()
            messages.success(request, f'Application Uploaded Sucessfully!')

    return render(request, "import.html", {"folderList":folderList}) 


def fileManager(request):
    folders = models.Folder.objects.all()
    for folder in folders:
        folder.files = models.File.objects.filter(folder=folder)
        for i in folder.files:
            print(i.file.application)
        print(folder.files)
    return render(request, "file-manager.html", {
        "folders":folders,
    })

# @csrf_exempt  # Use only if CSRF protection is not needed (e.g., API calls)
# def renameFolderName(request, id):
#     if request.method == "POST":
#         folder_name = request.POST.get("folderName")
#         folder_id = request.POST.get("folderId")
#         print(id, "folder id ++++++++++++++")
#         folderObj = models.Folder.objects.filter(id=id).first()
#         folderObj.folder_name = folder_name
#         folderObj.save()
#     return redirect("webpages-file-manager-home")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect
from . import models  # Import your models

@csrf_exempt  # Remove this if CSRF protection is needed
def renameFolderName(request, id):
    if request.method == "POST":
        folder_name = request.POST.get("folderName")
        
        # Get the folder object or return error
        folder_obj = get_object_or_404(models.Folder, id=id)
        folder_obj.folder_name = folder_name
        folder_obj.save()
        
        # Return a JSON response for AJAX
        return JsonResponse({"success": True, "message": "Folder renamed successfully"})

    return JsonResponse({"success": False, "message": "Invalid request method"}, status=400)
