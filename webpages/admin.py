from django.contrib import admin
from .models import Application, CandidateExperience, CandidateProfile, CandidateSkillset, Company, IndustryType, JobPosting, ShortlistedCandidate, ShortlistedCandidateTimeline

# Register your models here.
admin.site.register(Application)
admin.site.register(CandidateProfile)
admin.site.register(CandidateSkillset)
admin.site.register(CandidateExperience)
admin.site.register(IndustryType)
admin.site.register(Company)
admin.site.register(JobPosting)
admin.site.register(ShortlistedCandidate)
admin.site.register(ShortlistedCandidateTimeline)