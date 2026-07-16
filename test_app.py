from app import add, multiply

def test_add():
    assert add(5, 3) == 8
    print("Add test passed!")

def test_multiply():
    assert multiply(4, 3) == 12
    print("Multiply test passed!")

test_add()
test_multiply()
print("All tests passed!")