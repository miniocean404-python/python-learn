# 命令

## 依赖

1. 将当前环境中所有通过 pip 安装的包及其版本号信息输出到 requirements.txt 文件中。如果该文件不存在，则会自动创建；如果已存在，则会覆盖原有内容。

   ```shell
   pip freeze > requirements.txt
   ```

2. 当你需要在另一个环境中重新安装这些依赖时，只需在新环境中执行以下命令：

   ```shell
   pip install -r requirements.txt
   ```
