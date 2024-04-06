
# DEVELOPER SERIALIZER

def developer_serializer(developer) -> dict:
  return {
    'id': str(developer['_id']),
    'full_name': developer['full_name'],
    'stack': developer['stack'],
    'skills': developer['skills'],
    'about': developer['about'],
    'cv_url': developer['cv_url'],
    'whatsapp_url': developer['whatsapp_url'],
    'linkedin_url': developer['linkedin_url'],
    'email_url': developer['email_url'],
    'github_url': developer['github_url'],
  }


# EXPERIENCE SERIALIZER

def experience_serializer(experience) -> dict:
  return {
    'id': str(experience['_id']),
    'company_name': experience['company_name'],
    'position': experience['position'],
    'period': experience['period'],
    'job_description': experience['job_description'],
  }

def list_experience(experiences) -> list:
  return [list_experience(experience) for experience in experiences]


# PROJECT SERIALIZER

def project_serializer(project) -> dict:
  return {
    'id': str(project['_id']),
    'title': project['title'],
    'image_url': project['image_url'],
    'description': project['description'],
    'deploy_url': project['deploy_url'],
    'repo_url': project['repo_url'],
  }

def list_project(projects) -> list:
  return[list_project(project) for project in projects]

