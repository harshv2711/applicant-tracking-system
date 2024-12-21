from django.contrib import admin
from .models import (
    Application, 
    CandidateExperience, 
    CandidateProfile, 
    CandidateSkillset, 
    Company, 
    IndustryType, 
    JobPosting, 
    ShortlistedCandidate, 
    ShortlistedCandidateTimeline, 
    CandidateProject,
    CandidateEducation,
)
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Application)
# admin.site.register(CandidateProfile)
# admin.site.register(CandidateSkillset)
# admin.site.register(CandidateExperience)
# admin.site.register(IndustryType)
# admin.site.register(Company)
# admin.site.register(JobPosting)
# admin.site.register(ShortlistedCandidate)
# admin.site.register(ShortlistedCandidateTimeline)

@admin.register(Application)
class ApplicationAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ["application_name", "created_at", "updated_at", "applicationOwner"]
    search_fields = [
        "application_name",
        "application_text",
        "applicationOwner__username"
    ]

@admin.register(CandidateSkillset)
class CandidateSkillsetAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ["candidate", "skill_name", "created_at", "updated_at"]
    search_fields = [
        "candidate__first_name",
        "candidate__last_name", 
        "skill_name"
    ]
    list_filter = ["skill_name",]

@admin.register(CandidateProfile)
class CandidateProfileAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "role",
        "expected_ctc",
        "email",
        "phone_number",
        "address",
        "created_at",
        "updated_at",
        "status_in_interview",
    ]
    search_fields =  [
        "first_name", 
        "last_name",
        "role",
        "email",
        "phone_number",
        "created_at",
        "updated_at",
        "linkedin_profile",
        "address",
        "expected_ctc",
        "status_in_interview",
    ]
    list_filter = [
        "role",
        "expected_ctc",
        "status_in_interview",
    ]

@admin.register(CandidateExperience)
class CandidateExperienceAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "candidate", 
        "company_name", 
        "designation", 
        "startingDate", 
        "endDate",
        "summary",
        "company_location",
        "number_of_experience",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "designation",
        "company_name",
        "number_of_experience",
        "company_location",
    ]

    search_fields = [
       "candidate__first_name", 
        "candidate__last_name", 
        "company_name", 
        "designation", 
        "startingDate", 
        "endDate",
        "summary",
        "company_location",
        "number_of_experience"
    ]

@admin.register(IndustryType)
class IndustryTypeAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "industry_type_name"
    ]
    search_fields = [
        "industry_type_name"
    ]

    list_filter = [
        "industry_type_name",
    ]

@admin.register(Company)
class CompanyAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "company_name",
        "company_email",
        "company_contact_number",
        "company_domain_name",
        "industry_type",
        "company_postal_code",
        "company_number_of_employees",
        "company_time_zone",
        "company_linkedin_profile",
        "company_city",
        "company_state_region",
        "company_address",
    ]

    search_fields = [
        "company_name",
        "company_email",
        "company_contact_number",
        "company_domain_name",
        "industry_type",
        "company_postal_code",
        "company_number_of_employees",
        "company_time_zone",
        "company_linkedin_profile",
        "company_city",
        "company_state_region",
        "company_address",
    ]

    list_filter = [
        "industry_type",
        "company_postal_code",
        "company_number_of_employees",
        "company_time_zone",
        "company_city",
        "company_state_region",
    ]

@admin.register(JobPosting)
class JobPostingAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "company",
        "job_role",
        "is_live_job_post",
        "package",
        "experience_required",
        "location", 
        "number_of_openings",
        "number_of_applicants",
        # "job_description",
        "created_by",
        "created_at",
        "updated_at",

    ]

    search_fields = [
       "company__company_name",
        "job_role",
        "package",
        "experience_required",
        "location",
        "number_of_openings",
        "job_description",
        "is_live_job_post",
    ]


    list_filter =  [
       "company",
        "job_role",
        "package",
        "experience_required",
        "location",
        "number_of_openings",
    ]

@admin.register(ShortlistedCandidate)
class ShortlistedCandidateAdmin(ModelAdmin, ImportExportModelAdmin):   
    list_display = [
        "candidate",
        "job_posting",
        "company",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "job_posting",
        "company__company_name",
        "candidate__role"
    ]

    search_fields = [
        "candidate__first_name"
        "candidate__last_name"
        "candidate__role"
        "candidate__email"
        "candidate__phone_number"
    ]

@admin.register(ShortlistedCandidateTimeline)
class ShortlistedCandidateTimelineAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "shortlisted_Candidate",
        "comment_title",
        "comment",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "shortlisted_Candidate__candidate__first_name",
        "shortlisted_Candidate__candidate__last_name",
        "shortlisted_Candidate__candidate__email",
        "comment_title",
        "comment",
    ]

    list_filter = [
    ]

@admin.register(CandidateProject)
class CandidateProjectAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "candidate__first_name",
        "candidate__last_name",
        "candidate__email",
        "candidate__role",
        "project_name",
        "project_link",
        "project_description",
        "start_at",
        "end_at",
        "is_active",
        "created_at",
        "updated_at"
    ]

    search_fields = [
        "candidate__first_name",
        "candidate__last_name",
        "candidate__email",
        "candidate__role",
        "project_name",
    ]

    list_filter = [
        "candidate__role",
    ]


@admin.register(CandidateEducation)
class CandidateEducationAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = [
        "education_name",
        "university_college_name",
        "starting_date",
        "ending_date",
        "pursuing"
    ]

    search_fields = [
        "education_name",
        "university_college_name",
        "starting_date",
        "ending_date",
        "pursuing",
    ]   

    list_filter = [
        "education_name",
        "university_college_name",
        "pursuing",
        "starting_date",
        "ending_date",
        
    ]