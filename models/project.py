from pydantic import BaseModel

class Project(BaseModel):
  title: str
  image_url: str
  description: str
  descricao: str
  deploy_url: str
  repo_url: str