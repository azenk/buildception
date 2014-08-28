
from buildbot.changes.gitpoller import GitPoller
changes = []
changes.append(GitPoller(
        	'https://github.com/azenk/smoker-api.git',
        	workdir='smokerapi-workdir', branch='master',
        	pollinterval=30))
