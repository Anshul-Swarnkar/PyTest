def test_1():
    x=10
    y=10
    assert x==y

def test_2():
    name="Selenium"
    title="Selenium is web automation"
    assert name in title

def test_3():
    name="jenkins"
    title="Jenkins is CI Server"
    assert name in title, "title does not match"
