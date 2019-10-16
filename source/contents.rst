====
声明
====
如果不加 ``contents.*`` 文件在 `readthedocs <https://readthedocs.org>`_ 网站编译会产生如下错误，如果知道解决方案，请提 `issue <https://github.com/Iydon/tex/issues>`_.
::

	$ python /home/docs/checkouts/readthedocs.org/user_builds/tex/envs/latest/bin/sphinx-build -T -b readthedocs -d _build/doctrees-readthedocs -D language=zh_CN . _build/html

	Running Sphinx v1.8.5
	loading translations [zh_CN]... done
	making output directory...
	building [mo]: targets for 0 po files that are out of date
	building [readthedocs]: targets for 2 source files that are out of date
	updating environment: 2 added, 0 changed, 0 removed
	reading sources... [ 50%] index
	reading sources... [100%] preface

	/home/docs/checkouts/readthedocs.org/user_builds/tex/envs/latest/lib/python3.7/site-packages/recommonmark/parser.py:65: UserWarning: Container node skipped: type=document
	  warn("Container node skipped: type={0}".format(mdnode.t))
	/home/docs/checkouts/readthedocs.org/user_builds/tex/checkouts/latest/source/index.rst:7: WARNING: Title underline too short.

	LaTeX 资源及学习路径
	=============

	Traceback (most recent call last):
	  File "/home/docs/checkouts/readthedocs.org/user_builds/tex/envs/latest/lib/python3.7/site-packages/sphinx/cmd/build.py", line 304, in build_main
	    app.build(args.force_all, filenames)
	  File "/home/docs/checkouts/readthedocs.org/user_builds/tex/envs/latest/lib/python3.7/site-packages/sphinx/application.py", line 341, in build
	    self.builder.build_update()
	  File "/home/docs/checkouts/readthedocs.org/user_builds/tex/envs/latest/lib/python3.7/site-packages/sphinx/builders/__init__.py", line 347, in build_update
	    len(to_build))
	  File "/home/docs/checkouts/readthedocs.org/user_builds/tex/envs/latest/lib/python3.7/site-packages/sphinx/builders/__init__.py", line 360, in build
	    updated_docnames = set(self.read())
	  File "/home/docs/checkouts/readthedocs.org/user_builds/tex/envs/latest/lib/python3.7/site-packages/sphinx/builders/__init__.py", line 472, in read
	    self.env.doc2path(self.config.master_doc))
	sphinx.errors.SphinxError: master file /home/docs/checkouts/readthedocs.org/user_builds/tex/checkouts/latest/source/contents.rst not found

	Sphinx error:
	master file /home/docs/checkouts/readthedocs.org/user_builds/tex/checkouts/latest/source/contents.rst not found
