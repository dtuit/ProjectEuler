import sys, importlib
import os, glob
# import timeit
import time
'''
Basic run script that calculates runtime
usage:
	python eulermain.py <Problem_Number>
'''
def main():
	args = sys.argv[1:]

	modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
	problems = [os.path.basename(f)[:-3] for f in modules if f[0].isdigit()]

	if(args):
		try:
			p_file = [n for n in problems if n.startswith(args[0])]
			
			if(p_file):
				p_file = p_file[0]
			else:
				raise ValueError

			run(p_file)

		except (ImportError, ValueError):
			print("The argument {0} is not a valid problem".format(args[0]))

	else:
		print("Please enter the problem number as command line arg")

def run(p_file):
	problem = importlib.import_module(p_file)

	start = time.time()
	res = problem.solve()
	end = time.time()
	runtime = end - start

	print("problem : ", p_file)
	print("answer  : ", res)
	print("time    :  {0:.8f}".format(runtime))

if __name__ == '__main__':
	main()
