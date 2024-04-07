
# DEVELOPER SERIALIZER

def developer_serializer(developer) -> dict:
  return {
    'id': str(developer['_id']),
    'full_name': developer['full_name'],
    'stack': developer['stack'],
    'skills': developer['skills'],
    'about': developer['about'],
    'sobre': developer['sobre'],
    'cv_url': developer['cv_url'],
    'whatsapp_url': developer['whatsapp_url'],
    'linkedin_url': developer['linkedin_url'],
    'email_url': developer['email_url'],
    'github_url': developer['github_url']
  }

def list_dev(developers) -> list:
  if developers:
    return developer_serializer(developers[0])
  return []

def list_devs(developers) -> list:
  if developers:
    return [developer_serializer(developer) for developer in developers]
  return []


# EXPERIENCE SERIALIZER

def experience_serializer(experience) -> dict:
  return {
    'id': str(experience['_id']),
    'company_name': experience['company_name'],
    'company_image_url': experience['company_image_url'],
    'position': experience['position'],
    'cargo': experience['cargo'],
    'period': experience['period'],
    'job_description': experience['job_description'],
    'descricao': experience['descricao'],
  }

def list_experience(experiences) -> list:
  return [experience_serializer(experience) for experience in experiences]

# PROJECT SERIALIZER

def project_serializer(project) -> dict:
  return {
    'id': str(project['_id']),
    'title': project['title'],
    'image_url': project['image_url'],
    'description': project['description'],
    'descricao': project['descricao'],
    'deploy_url': project['deploy_url'],
    'repo_url': project['repo_url'],
  }

def list_project(projects) -> list:
  return [project_serializer(project) for project in projects]

