- bin/: 存放项目的一些可执行文件，当然你可以起名script/之类的也行。
- python/: 存放项目的所有源代码。
    - 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。
    - 其子目录tests/存放单元测试代码； 
    - 程序的入口最好命名为main.py。
- docs/: 存放一些文档。
- setup.py: 安装、部署、打包的脚本。
- requirements.txt: 存放软件依赖的外部Python包列表。
- README: 项目说明文件。


    ProjectName
    │ readme 项目说明文档
    │ requirements.txt 存放依赖的外部Python包列表
    │ setup.py 安装、部署、打包的脚本
    ├─ bin 存放脚本，执行文件等
    │ └─ projectname
    ├─ docs 文档和配置
    │ └─ abc.rst
    │ └─ conf.py 配置文件
    └─ projectname 工程源码（包括源码、测试代码等）
    │ main.py 程序入口
    │ init.py
    └─ tests 测试代码
    └─ test_main.py
    └─ init.py
