from pydantic import BaseModel


class Freelance(BaseModel):
    title: str
    image_url: str
    description: str
    descricao: str
    techs: str
    deploy_url: str
    layout_url: str
