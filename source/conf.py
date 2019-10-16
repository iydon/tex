

import os






project = 'TeX'
copyright = '2019, Iydon Liang'
author = 'Iydon Liang'

release = '0.1'



extensions = [
	'recommonmark',
	'sphinx_rtd_theme',
]

templates_path = ['_templates']

language = 'zh'

exclude_patterns = ['_origin', ]



on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  	import sphinx_rtd_theme

	html_theme = 'sphinx_rtd_theme'
	html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']



latex_elements={
	'preamble': r'''\usepackage{ctex}'''
}
