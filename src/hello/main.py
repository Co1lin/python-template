import fire


class Hello:
    def __init__(self, prefix: str = 'class Hello'):
        self.prefix = prefix

    def hello(self, name: str = 'World') -> str:
        return f'[{self.prefix}] Hello, {name}!'


if __name__ == '__main__':
    fire.Fire(Hello)
    # python -m hello.main hello --name Colin --prefix haha
