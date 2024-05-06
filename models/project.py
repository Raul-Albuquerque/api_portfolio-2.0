from pydantic import BaseModel


class Project(BaseModel):
    title: str
    image_url: str
    descricao: str
    description: str
    techs: str
    deploy_url: str
    repo_url: str
