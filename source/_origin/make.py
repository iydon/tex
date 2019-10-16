#!/usr/bin/env python
from macro_parser import parse_macro_in

from utils import config, sh


for file in sh.recursive_folder(ignores=config.ignore_dirs):
	content = parse_macro_in(file)
	target = sh.join_path(config.target_path, file)
	sh.write_file(target, content)
