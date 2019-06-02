import os
from sys import argv
import argparse

def print_filename(path):
	for fname in os.listdir(path):
		child_path = os.path.join(path, fname)
		if os.path.isdir(child_path):
			print_filename(child_path)
		else:
			print(fname)


parser = argparse.ArgumentParser(description='demo')
parser.add_argument('-p', '--path', help='Input path', type=str)
args = parser.parse_args()
			
print_filename(args.path)