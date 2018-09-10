 # 简介
Heox Blog Manage System 是基于flask搭建的hexo博客管理系统，简单易用为目标，方便使用Hexo，也可以使用此项目实现简单的后台管理系统功能。本项目的主要目的是为了让自己熟悉Python web开发。由于我时间精力有限，项目很多地方不尽完美，也欢迎 fork 和 Pull Request。

### 说明
- 本质上就是一个markdown编辑器的web实现，所以只要设置改为markdown文件所在目录，就可以编辑该目录的markdown文档。
- 这个小项目还处于开发阶段，功能虽不完善，但是也可以使用和复用。
- 对于企业生产项目，本项目仅供参考，不建议直接使用。

# 技术栈
- flask
- Jinja
- sqlite
- Bootstrap
- [layer](https://layer.layui.com/ "layer")
- [editor.md](https://pandao.github.io/editor.md/index.html "editor.md")

# 使用说明
### 进入项目目录
	cd hexo-blog-manage-system/
## 使用python3环境
### 虚拟环境（可选）
    python3 -m venv venv
    . venv/bin/activate
### 安装依赖
    pip install Flask
### 初始化数据库
    export FLASK_APP=app
    flask init-db
### 启动服务
    # 使用flask命令
	export FLASK_APP=app
    flask run
	# 或者使用python命令
	python3 app.py
### 后台服务（可选）
    nohup python3 app.py > /dev/null 2>&1 &
## 使用Docker
### 初始化数据库（需要安装sqlite3）
	cd hexo-blog-manage-system/
	mkdir instance
	cd instance
	sqlite3 editor.sqlite < ../release/schema.sql
也可以选择其他目录，这样在启动容器的时候需要目录映射，映射到容器内`/usr/src/app/instance`目录。如果有python环境，这一步也可以使用上面的flask初始化数据库的方法。
### 制作镜像文件
	docker build -t editor:0.1 .
可以把镜像传到私有镜像库或者dockerhub上面。
### 启动容器
	docker run --rm -p 5000:5000 -d editor:0.1
访问 http://127.0.0.1:5000 即可。

# 项目演示
[![登录页](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/index.png?raw=true "登录页")](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/index.png?raw=true "登录页")
[![博客列表](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/blog.png?raw=true "博客列表")](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/blog.png?raw=true "博客列表")
[![博客编辑](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/list.png?raw=true "博客编辑")](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/list.png?raw=true "博客编辑")

# TODO
- 实现hexo与git相关操作功能
- 树形结构，可操作不同目录下面的markdown文档
- 服务器dashboard监控
- flask-login优化登录并加入图形验证码
- 前端校验
- 交互和样式优化
- 上传图片
- 用户管理
- etc.

# Done
- 项目框架、基础页面
- 登录登出
- 设置修改
- 文档增查改

# 参考文档和项目
- [官方文档](https://dormousehole.readthedocs.io/en/latest/ "官方文档")
- [官方例子flaskr](https://github.com/pallets/flask/tree/master/examples/tutorial/ "官方例子flaskr")
- [开源项目flask-admin](https://github.com/flask-admin/flask-admin.git "开源项目")

# Licence
[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0 "http://www.apache.org/licenses/LICENSE-2.0")
