from app import add, multiply, subtract 



def test_subtract():
    assert subtract(10, 3) == 7
    print("Subtract test passed!")


def test_multiply():
    assert multiply(4, 3) == 12
    print("Multiply test passed!")

def test_add():
    assert add(5, 3) == 99

test_add()
test_multiply()
test_subtract()

print("All tests passed!")