import logging
import time
from watchdog.events import FileSystemEventHandler
import importlib
from watchdog.observers import Observer


def hot_reload(module_name: str, function_name: str, *args, **kwargs) -> None:
    observer = Observer()
    event_handler = ReloadMonitor(module_name, function_name, *args, **kwargs)
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
            # pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


class ReloadMonitor(FileSystemEventHandler):
    def __init__(
        self,
        module_name: None | str = None,
        function_name: None | str = None,
        *args,
        **kwargs,
    ):
        """
        __init__ 初始化函数
        该函数用于初始化ReloadMonitor类的实例。
        该类用于监控指定模块的文件变化，并在文件变化时重新加载模块。
        该类继承自FileSystemEventHandler类。
        该类的实例可以用于监控指定目录下的文件变化，并在文件变化时执行指定的函数。

        Args:
            module_name (None | str, optional): 重载模块的名称，例如：src.request. Defaults to None.
            function_name (None | str, optional): 重载函数的名称，例如：request_baidu. Defaults to None.
            _*args: 可变参数(匿名参数)，用于传递给函数的参数。
            _**kwargs: 关键字参数(命名参数)，用于传递给函数的参数。
        """
        super().__init__(
            # 传递给父类的参数
        )

        # 预先导入模块
        self.module = importlib.import_module(module_name)
        self.function_name = function_name
        self.args = args
        self.kwargs = kwargs

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            logging.info(f"检测到文件修改：{event.src_path}, 重新加载模块...")
            try:
                self.module = importlib.reload(self.module)

                # 如果提供了函数名，则调用该函数
                if self.function_name:
                    if hasattr(self.module, self.function_name):
                        func = getattr(self.module, self.function_name)
                        func(*self.args, **self.kwargs)
                    else:
                        logging.error(
                            f"模块 {self.module.__name__} 中没有找到函数 {self.function_name}"
                        )

            except Exception as e:
                print(f"重新加载时出错: {e}")
