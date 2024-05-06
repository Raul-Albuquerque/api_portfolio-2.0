# DEVELOPER SERIALIZER

def developer_serializer(developer) -> dict:
    return {
        "id": str(developer["_id"]),
        "full_name": developer["full_name"],
        "stack_pt": developer["stack_pt"],
        "stack_en": developer["stack_en"],
        "about": developer["about"],
        "sobre": developer["sobre"],
        "skills": developer["skills"],
        "resume_url": developer["resume_url"],
        "profile_picture": developer["profile_picture"],
        "cv_url": developer["cv_url"],
        "whatsapp_url": developer["whatsapp_url"],
        "linkedin_url": developer["linkedin_url"],
        "email_url": developer["email_url"],
        "github_url": developer["github_url"]
    }

def list_devs(developers) -> list:
    return [developer_serializer(developer) for developer in developers]



# FREELANCE SERIALIZER

def freelance_serializer(freelance) -> dict:
    return {
        "id": str(freelance["_id"]),
        "title": freelance["title"],
        "image_url": freelance["image_url"],
        "description": freelance["description"],
        "techs": freelance["techs"],
        "descricao": freelance["descricao"],
        "deploy_url": freelance["deploy_url"],
    }


def list_freelance(freelances) -> list:
    return [freelance_serializer(freelance) for freelance in freelances]


# PROJECT SERIALIZER


def project_serializer(project) -> dict:
    return {
        "id": str(project["_id"]),
        "title": project["title"],
        "image_url": project["image_url"],
        "description": project["description"],
        "techs": project["techs"],
        "descricao": project["descricao"],
        "deploy_url": project["deploy_url"],
        "repo_url": project["repo_url"],
    }


def list_project(projects) -> list:
    return [project_serializer(project) for project in projects]
