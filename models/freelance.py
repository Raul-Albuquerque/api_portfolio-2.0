from pydantic import BaseModel


class Freelance(BaseModel):
    title: str
    image_url: str
    descricao: str
    description: str
    techs: str
    deploy_url: str
