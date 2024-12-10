from jar import Jar


def test_init():
    # Assert lets you check if a condition is true
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(2)
    assert jar1.capacity == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    jar.deposit(2)
    assert jar.size == 9

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2
