from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    application = models.FileField(upload_to="media")
    application_name = models.CharField(max_length=255)
    application_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    applicationOwner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.application_name}"
# Application model end 

class CandidateProfile(models.Model):
    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField()
    linkedin_profile = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    expected_ctc = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status_in_interview_choices = (
        ("Shortlisted", "Shortlisted"),
        ("Initial Communication", "Initial Communication"),
        ("HR Screening/Preliminary Interview", "HR Screening/Preliminary Interview"),
        ("Coordination for Technical/Functional Rounds", "Coordination for Technical/Functional Rounds"),
        ("Feedback and Follow-Up", "Feedback and Follow-Up"),
        ("Final Interview", "Final Interview"),
        ("Offer Rollout", "Offer Rollout"),
        ("Post-Interview Process", "Post-Interview Process"),
        ("Rejected", "Rejected"),
    )
    status_in_interview = models.CharField(max_length=225, choices=status_in_interview_choices, blank=True, null=True, default="Shortlisted")
    ratingChoices = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    candidate_rating = models.CharField(max_length=5, choices=ratingChoices, default="null")

    def __str__(self):
        return f"{self.id}, {self.first_name} {self.last_name}, {self.role}, {self.email}"
# CandidateProfile model end 

class CandidateSkillset(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, blank=False, null=False)
    skill_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.candidate.first_name} {self.candidate.last_name}, {self.skill_name} "
# CandidateSkillset model end 

class CandidateExperience(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, blank=False, null=False)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=50)
    startingDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    summary = models.TextField()
    company_location = models.TextField()
    number_of_experience = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# CandidateExperience model end 


class IndustryType(models.Model):
    industry_type_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.industry_type_name}"
# company_type end here 


# company is our client we are hiring for 
class Company(models.Model):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    is_active = models.BooleanField(null=True, blank=True)
    company_name = models.CharField(max_length=255)
    company_address = models.TextField(blank=True, null=True)
    company_email = models.CharField(max_length=255, blank=True, null=True)
    company_info = models.TextField(blank=True, null=True)
    company_domain_name = models.CharField(max_length=255, blank=True, null=True)
    industry_type = models.ForeignKey(IndustryType, on_delete=models.CASCADE, blank=True, null=True)
    company_postal_code = models.CharField(max_length=255, blank=True, null=True)
    company_number_of_employees = models.IntegerField(blank=True, null=True)
    company_time_zone = models.CharField(max_length=255, blank=True, null=True)
    company_linkedin_profile = models.CharField(max_length=255, blank=True, null=True)
    company_annual_revenue = models.CharField(max_length=255, blank=True, null=True)
    company_city = models.CharField(max_length=255, blank=True, null=True)
    company_state_region = models.CharField(max_length=255, blank=True, null=True)
    company_contact_number = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.company_name}, {self.industry_type.industry_type_name}"
# Company model end 

class JobPosting(models.Model):
    is_active = models.BooleanField(default=False)
    is_live_job_post = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_role = models.CharField(max_length=255)
    package = models.CharField(max_length=10, null=True, blank=True, default="Not Disclosed")
    experience_required = models.IntegerField(default=0)
    location = models.CharField(max_length=255)
    number_of_openings = models.IntegerField()
    number_of_applicants = models.IntegerField()
    job_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.id} - {self.job_role} - {self.company.company_name}"
# JobPosting model end 

class ShortlistedCandidate(models.Model):
    is_active = models.BooleanField(default=True)
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE,)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.job_posting.number_of_applicants += 1
        self.job_posting.save()
        super().save(*args, **kwargs)
 
    def __str__(self):
        return f"{self.id} - {self.candidate.first_name} {self.candidate.last_name} - {self.company.company_name} - {self.job_posting.job_role}"
# shortlistedCandidateForCompany model end 
     
class ShortlistedCandidateTimeline(models.Model):
    shortlisted_Candidate = models.ForeignKey(ShortlistedCandidate, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Interviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.id} - {self.shortlisted_Candidate.company.company_name} - {self.shortlisted_Candidate.job_posting.job_role} - {self.comment_title} - {self.shortlisted_Candidate.candidate.first_name} {self.shortlisted_Candidate.candidate.last_name}"
# ShortlistedCandidateTimeline models end 


class CandidateProject(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE,)
    project_name = models.CharField(max_length=255)
    project_link = models.CharField(max_length=255, blank=True, null=True)
    project_description = models.TextField()
    start_at = models.DateField()
    end_at = models.DateField()
    is_active = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project_name} by {self.candidate.email}"
    
class CandidateEducation(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE,)
    education_name = models.CharField(max_length=255)
    university_college_name = models.CharField(max_length=255)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateTimeField(blank=True, null=True)
    pursuing = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f"{self.education_name} - {self.university_college_name} - {self.candidate.email}"
    

class CompanyProfileViewPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.company.company_name}"