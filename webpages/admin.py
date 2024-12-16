from django.contrib import admin
from .models import Application, CandidateExperience, CandidateProfile, CandidateSkillset, Company, IndustryType, JobPosting, ShortlistedCandidate, ShortlistedCandidateTimeline
from unfold.admin import ModelAdmin

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
class ApplicationAdmin(ModelAdmin):
    list_display = ["application_name", "created_at", "updated_at", "applicationOwner"]

@admin.register(CandidateSkillset)
class CandidateSkillsetAdmin(ModelAdmin):
    list_display = ["candidate", "skill_name", "created_at", "updated_at"]
    search_fields = [
        "candidate__first_name",
        "candidate__last_name", 
        "skill_name"
    ]
    list_filter = ["skill_name",]

@admin.register(CandidateProfile)
class CandidateProfileAdmin(ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "role",
        "email",
        "phone_number",
        "address",
        "created_at",
        "updated_at",
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
    ]
    list_filter = [
        "role",
    ]

@admin.register(CandidateExperience)
class CandidateExperienceAdmin(ModelAdmin):
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
class IndustryTypeAdmin(ModelAdmin):
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
class CompanyAdmin(ModelAdmin):
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
class JobPostingAdmin(ModelAdmin):
    list_display = [
        "company",
        "job_role",
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
        "experience_required",
        "location",
        "number_of_openings",
        "job_description",
    ]


    list_filter =  [
       "company",
        "job_role",
        "experience_required",
        "location",
        "number_of_openings",
    ]

@admin.register(ShortlistedCandidate)
class ShortlistedCandidateAdmin(ModelAdmin):   
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
    ]

@admin.register(ShortlistedCandidateTimeline)
class ShortlistedCandidateTimelineAdmin(ModelAdmin):
    list_display = [
        "shortlisted_Candidate",
        "timeline_name",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "shortlisted_Candidate__candidate__first_name",
        "shortlisted_Candidate__candidate__last_name",
        "shortlisted_Candidate__candidate__email",
    ]

    list_filter = [
    ]



