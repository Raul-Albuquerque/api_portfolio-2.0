from pydantic import BaseModel

class Developer(BaseModel):
  full_name: str
  stack: str
  about: str
  skills: str
  cv_url: str
  whatsapp_url: str
  linkedin_url: str
  email_url: str
  github_url: str
