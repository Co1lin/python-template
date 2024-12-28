def test_hello():
    from hello.main import Hello

    hello = Hello()
    assert hello.hello() == "Hello, World!"
