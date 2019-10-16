#!/usr/bin/env python
import os


def recursive_folder(path='', ignores=None):
	'''
	Example
	=======
		>>> for file in recursive_folder('.'):
		...     print(file)
	'''
	path = path or os.path.curdir
	ignores = ignores or list()
	for dirpath, dirnames, filenames in os.walk(path):
		dirpath_tuple = dirpath.split(os.path.sep)
		if any(ign in dirpath_tuple for ign in ignores):
			continue
		for filename in filenames:
			if filename in ignores:
				continue
			yield os.path.join(dirpath, filename)


def split_extension(file):
	'''
	Example
	=======
		>>> root, ext = split_extension(file)
	'''
	return os.path.splitext(file)


def join_path(a, *p):
	'''os.path.join
	'''
	return os.path.join(a, *p)


def judge_path_type(path, type_):
	'''
	Argument
	=======
		type_: str, in {'file', 'dir', 'link', 'mnt'}

	Example
	=======
		>>> flag = judge_path_type(path, type_=type_)
	'''
	if type_=='file':return os.path.isfile(path)
	elif type_=='dir': return os.path.isdir(path)
	elif type_=='link': return os.path.islink(path)
	elif type_=='mnt': return os.path.ismount(path)
	else: raise TypeError('Type `{}` is illegal.')


def read_file(file, encoding='utf-8'):
	'''
	Argument
	=======
		encoding: str, if not encoding, then use binary mode
	'''
	if encoding:
		with open(file, 'r', encoding=encoding) as f:
			return f.read()
	else:
		with open(file, 'rb') as f:
			return f.read()


def write_file(file, content, encoding='utf-8'):
	'''
	Argument
	=======
		encoding: str, if not encoding, then use binary mode
	'''
	head, _ = os.path.split(file)
	try:
		os.makedirs(head)
	except FileExistsError:
		pass

	if encoding and isinstance(content, str):
		with open(file, 'w', encoding=encoding) as f:
			f.write(content)
	elif isinstance(content, bytes):
		with open(file, 'wb') as f:
			f.write(content)
	else:
		raise Exception
