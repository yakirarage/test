from git.repo import Repo

repo = Repo('../test')

repo.index.add(['test.py'])
repo.index.commit('commit from python')

origin = repo.remotes[0]
origin.push()