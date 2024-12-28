def test_hello():
    from hello.main import Hello

    hello = Hello()
    assert "Hello, World!" in hello.hello()
