=============
附录 A - 快速获取资料
=============
----------
下载 TeX 发行版
----------
如果访问 OverLeaf_ 方便, 同时电脑硬盘局限, 请首先考虑使用 OverLeaf_ 进行云端编译. 否则如果电脑容量充足 (至少需要 **8G**), 可以考虑下载 TeX 发行版进行本地编译, 对于完全没有或只有一点接触过 **TeX** 的人来说, 推荐使用 **TeX Live**, 因为省去折腾下载安装宏包的麻烦, 可以更好地学习使用 **TeX**.

请手动打开以下链接下载 TeX 发行版, 链接虽为 CTAN 镜像网站, 但其会自动重定向至较快的镜像网站进行下载. 如需指定镜像网址, 请访问 镜像列表_ 进行进一步的选择.

:TeX Live:

.. code-block:: shell

	https://mirrors.ctan.org/systems/texlive/Images/texlive2019.iso



:MiKTeX:

.. code-block:: shell

	https://mirrors.ctan.org/systems/win32/miktex/source/miktex-2.9.7140.tar.xz



:MacTeX:

.. code-block:: shell

	https://mirrors.ctan.org/systems/mac/mactex/MacTeX.pkg




----------
安装 TeX 发行版
----------
请参照 啸行_ 大哥所整理的文档 ``install-latex``. 最初创作文档的契机来自于许多人无法打开图形界面, 啸行_ 大哥只能一点点地解释命令行, 为提高效率, 所以将常见问题整理成文档的形式. 文档中介绍了在不同的系统上如何安装, 卸载与更新 TeX Live, 同时介绍了 TeX 中常用的编辑器 - TeXstudio. 请通过以下命令下载文档.

.. code-block:: shell

	https://github.com/OsbertWang/install-latex/releases/download/v6.2/Install-LaTeX.pdf




----------
安装 TeX 编辑器
----------
:TeXstudio:

.. code-block:: shell

	# Windows
	https://github.com/texstudio-org/texstudio/releases/download/2.12.16/texstudio-2.12.16-win-qt5.exe
	
	# MacOS
	https://github.com/texstudio-org/texstudio/releases/download/2.12.16/texstudio-2.12.16-osx.dmg
	
	# Linux
	echo 'DIY (do it yourself)'



:其他编辑器:
	请参照相应文档进行配置.


-----------
下载 TeX 入门文档
-----------
如果已经安装 TeX 发行版, 请在命令行运行 ``texdoc lshort-zh``, 否则运行以下命令下载入门文档.

.. code-block:: shell

	http://mirrors.ctan.org/info/lshort/chinese/lshort-zh-cn.pdf





.. _OverLeaf: https://www.overleaf.com/
.. _镜像列表: https://www.ctan.org/mirrors
.. _啸行: https://github.com/OsbertWang
