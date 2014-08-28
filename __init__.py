def change_sources():
	srcs = []
	srcs.append(GitPoller(
        	'https://github.com/azenk/smoker-api.git',
        	workdir='smokerapi-workdir', branch='master',
        	pollinterval=30))
	return srcs
