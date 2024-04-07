from pydantic import BaseModel

class Experience(BaseModel):
  company_name: str
  company_image_url: str
  position: str
  cargo: str
  period: str
  job_description: str
  descricao: str