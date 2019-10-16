=============
附录 A - 快速获取资料
=============
-----------
下载 TeX  发行版
-----------
以下命令采用 CTAN 镜像网站自动重定向至较快的镜像网站进行下载发行版, 请将其输入进命令行中. 如需指定镜像网址, 请访问 `镜像列表 <https://www.ctan.org/mirrors>`_ 进行进一步的选择.

:TeX Live:

.. code-block:: shell

	curl -O https://mirrors.ctan.org/systems/texlive/Images/texlive2019.iso

:MiKTeX:

.. code-block:: shell

	curl -O https://mirrors.ctan.org/systems/win32/miktex/source/miktex-2.9.7140.tar.xz


----------
安装 TeX 发行版
----------
请参照 啸行_ 大哥所整理的文档 ``install-latex``. 最初创作文档的契机来自于许多人无法打开图形界面, 啸行_ 大哥只能一点点地解释命令行, 为提高效率, 所以将常见问题整理成文档的形式. 文档中介绍了在不同的系统上如何安装, 卸载与更新 TeX Live, 同时介绍了 TeX 中常用的编辑器 - TeXstudio. 请通过以下命令下载文档.

.. code-block:: shell

	curl -O https://github.com/OsbertWang/install-latex/releases/download/v6.0/Install-LaTeX.pdf


----------
安装 TeX 编辑器
----------
:TeXstudio:

.. code-block:: shell

	:: Windows
	curl -O https://github.com/texstudio-org/texstudio/releases/download/2.12.16/texstudio-2.12.16-win-qt5.exe

	# MacOS
	curl -O https://github.com/texstudio-org/texstudio/releases/download/2.12.16/texstudio-2.12.16-osx.dmg

	# Linux
	echo 'DIY (do it yourself)'

:其他编辑器:
	请参照相应文档进行配置.


-----------
下载 TeX 入门文档
-----------
如果已经安装 TeX 发行版, 请在命令行运行 ``texdoc lshort-zh``, 否则运行以下命令下载入门文档.

.. code-block:: shell

	curl -O http://mirrors.ctan.org/info/lshort/chinese/lshort-zh-cn.pdf



.. _啸行: https://github.com/OsbertWang
