from pydantic import BaseModel

class Experience(BaseModel):
  company_name: str
  position: str
  period: str
  job_description: str