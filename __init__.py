
from buildbot.changes.gitpoller import GitPoller
changes = []
changes.append(GitPoller(
        	'https://github.com/azenk/smoker-client.git',
        	workdir='smokerclient-workdir', branch='master',
        	pollinterval=30))
changes.append(GitPoller(
        	'https://github.com/azenk/smoker-api.git',
        	workdir='smokerapi-workdir', branch='master',
        	pollinterval=30))
