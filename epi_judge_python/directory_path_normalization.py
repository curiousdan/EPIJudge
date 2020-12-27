from test_framework import generic_test

# eg: /usr/lib/../bin/gcc = /usr/bin/gcc
# eg: scripts//./../scripts/awkscripts/././ = scripts/awkscripts
# return the shortest equivalent pathname.

# 12/26/2020
def shortest_equivalent_path(path: str) -> str:
	# book soln
	if not path:
		raise ValueError("empty string input")
	path_names = []
	
	if path[0] == '/':
		path_names.append('')
		
	# lol ok, guys
	for token in (token for token in path.split("/") if token not in ['.','']):
		if token == "..":
			if not path_names or path_names[-1] == "..": 
				path_names.append(token)
			else:
				if path_names[-1] == "/":
					raise ValueError("path's f'd bro")
				path_names.pop()
		else:
			path_names.append(token)
	result = "/".join(path_names)
	return result[result.startswith('//'):] 
	#okay bros. this offsets by 1, because it evals to True = 1 lmao
	# avoidable by using my solution
	
	
def my_failed_attempt(path):
	path_build = []
	path_split = path.split('/')
	if path_split[0] == "":
		path_build.append("/")
	for path_element in path_split:
		if path_element in (".", ""):
			continue
		elif path_element == "..":
			if not path_build or path_build[-1] == "..":
				path_build.append("..")
			else:
				path_build.pop()
		else:
			path_build.append(path_element)
		
	result = "/".join(path_build)
	return result[result.startswith("//"):]


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('directory_path_normalization.py',
																																	'directory_path_normalization.tsv',
#																																	my_failed_attempt))
																																	shortest_equivalent_path))

