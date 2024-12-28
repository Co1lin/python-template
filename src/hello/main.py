import fire


class Hello:
    def __init__(self):
        pass

    def hello(self, name: str = "World") -> str:
        return f"Hello, {name}!"


if __name__ == "__main__":
    fire.Fire(Hello)
