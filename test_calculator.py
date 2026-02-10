"""
Unit Tests for Calculator Module
Tests basic arithmetic operations to ensure correctness.
"""

from calculator import add

def test_addition():
    """Test that 2 + 2 equals 4"""
    result = add(2, 2)
    assert result == 4, f"Expected 4, but got {result}"
    print("✓ Test passed: 2 + 2 = 4")

def test_addition_negative():
    """Test addition with negative numbers"""
    result = add(-1, 1)
    assert result == 0, f"Expected 0, but got {result}"
    print("✓ Test passed: -1 + 1 = 0")

def test_addition_zero():
    """Test addition with zero"""
    result = add(5, 0)
    assert result == 5, f"Expected 5, but got {result}"
    print("✓ Test passed: 5 + 0 = 5")

if __name__ == "__main__":
    test_addition()
    test_addition_negative()
    test_addition_zero()
    print("\n✅ All tests passed!")
