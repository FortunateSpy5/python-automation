import git
import json
from datetime import datetime

file = json.load(open('git_projects.json'))

path = file['path']
projects = [project["name"] for project in file['projects'] if project["active"]]

with open('git_push.log', 'a') as log:
    for project in projects:
        repo = git.Repo(path + project)
        # add all changes
        repo.git.add(A=True)
        # commit changes if there are any
        if repo.is_dirty():
            # commit changes
            repo.git.commit(m=f'Automated commit - {datetime.now()}')
            # push changes
            origin = repo.remotes.origin
            origin.push()
            # Add to log
            log.write(f'{datetime.now()} - {project} - Pushed successfully')