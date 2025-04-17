from script.reload import hot_reload

if __name__ == "__main__":
    hot_reload("src.lib.request", "request_baidu", "https://www.baidu.com")
