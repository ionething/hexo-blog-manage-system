# 简介
Heox Blog Manage System 是基于flask搭建的hexo博客管理系统，简单易用为目标，方便使用Hexo，也可以使用此项目实现简单的后台管理系统功能。

# 所用技术
- flask
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
### 制作镜像文件（需要先初始化数据库）
	docker build -t editor:0.1 .
### 启动容器
	docker run --rm -p 5000:5000 -d editor:0.1
访问 http://127.0.0.1:5000 即可

# 项目演示
[![登录页](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/index.png?raw=true "登录页")](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/index.png?raw=true "登录页")
[![博客列表](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/blog.png?raw=true "博客列表")](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/blog.png?raw=true "博客列表")
[![博客编辑](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/list.png?raw=true "博客编辑")](https://github.com/ionething/hexo-blog-manage-system/blob/26bee1a745288b74dd9b1d0a1dd54a87bfcb00aa/doc/images/list.png?raw=true "博客编辑")

# TODO
- 实现hexo与git相关操作功能
- 服务器dashboard监控
- flask-login优化登录并加入图形验证码
- 上传图片
- etc.

# 参考文档和项目
- [官方文档](https://dormousehole.readthedocs.io/en/latest/ "官方文档")
- [官方例子flaskr](https://github.com/pallets/flask/tree/master/examples/tutorial/ "官方例子flaskr")
- [开源项目flask-admin](https://github.com/flask-admin/flask-admin.git "开源项目")

# Licence
[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0 "http://www.apache.org/licenses/LICENSE-2.0")

欢迎 Pull Request