# Flask + SQLAlchemy TodoList (MSV 架构)

基于 Flask、SQLAlchemy 和 AngularJS 的前后端分离 TodoList 示例，使用本地 MySQL 数据库，目录遵循 web-project-(flask+sqlalchemy)-start1 结构。

## 目录结构

```
web-project-(flask+sqlalchemy)-start1/
├── app/                        # 应用模块
│   ├── __init__.py            # 应用工厂函数、路由定义
│   ├── static/                # 静态资源
│   │   ├── css/              # 样式文件
│   │   └── js/               # JavaScript 文件
│   └── templates/             # HTML 模板
│       └── index.html        # 待办事项列表页面
├── config/                    # 配置模块
│   ├── __init__.py
│   ├── config.py             # 数据库连接配置
│   └── sct.sql               # 数据库脚本
├── controller/                # 控制器层（业务逻辑）
│   ├── __init__.py
│   ├── userController.py     # 用户业务逻辑
│   └── todolistController.py # 待办事项业务逻辑
├── database/                  # 数据库文件
│   └── sct.sql               # 数据库结构和初始数据
├── models/                    # 数据模型层
│   ├── __init__.py           # 数据库实例和基础模型
│   ├── user.py               # 用户模型
│   └── todolist.py           # 待办事项模型
├── utils/                     # 工具类模块
│   ├── __init__.py
│   ├── commons.py            # 通用工具函数
│   ├── error.py              # 错误处理
│   ├── loggings.py           # 日志记录
│   ├── response_code.py      # 响应状态码定义
│   └── rsa_encryption_decryption.py  # RSA 加密解密
├── requirements.txt           # 项目依赖
└── start.py                  # 应用入口文件
```

## 环境配置

1. 创建并初始化数据库：

   ```bash
   mysql -u root -p < database/sct.sql
   ```

   如需修改数据库连接，更新 `config/config.py` 或设置环境变量 `MYSQL_USER`、`MYSQL_PASSWORD`、`MYSQL_HOST`、`MYSQL_PORT`、`MYSQL_DB`。

2. 创建虚拟环境并安装依赖：

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. 运行应用：

   ```bash
   flask --app start run
   ```

   浏览器访问 <http://127.0.0.1:5000/> 即可使用前端页面。

## API 概览

- `GET /api/todos/`：获取任务列表
- `POST /api/todos/`：创建任务，body 需要 `title` 和可选 `status`
- `PATCH /api/todos/<id>`：更新任务标题或状态
- `DELETE /api/todos/<id>`：删除任务

所有 JSON 响应统一包含 `code`、`message`、`data` 字段。
