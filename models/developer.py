from pydantic import BaseModel


class Developer(BaseModel):
    full_name: str
    stack_pt: str
    stack_en: str
    about: str
    sobre: str
    skills: str
    resume_url: str
    profile_picture: str
    cv_url: str
    whatsapp_url: str
    linkedin_url: str
    email_url: str
    github_url: str
