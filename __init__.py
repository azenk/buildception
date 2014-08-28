
def change_sources():
	from buildbot.changes.gitpoller import GitPoller
	srcs = []
	srcs.append(GitPoller(
        	'https://github.com/azenk/smoker-api.git',
        	workdir='smokerapi-workdir', branch='master',
        	pollinterval=30))
	return srcs
