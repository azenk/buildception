def config(c):
	c['change_source'].append(GitPoller(
        	'https://github.com/azenk/smoker-api.git',
        	workdir='smokerapi-workdir', branch='master',
        	pollinterval=30))
	return c
