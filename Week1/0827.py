def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius and Fahrenheit."""
    from_unit, to_unit = from_unit.upper(), to_unit.upper()
    
    if from_unit not in ("C", "F") or to_unit not in ("C", "F"):
        raise ValueError("Unsupported temperature unit! Only 'C' and 'F' are allowed.")
    
    if from_unit == to_unit:
        return value
    
    if from_unit == "C" and to_unit == "F":
        return value * 9/5 + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9


# ================== Unit Tests ==================
import unittest

class TestTemperatureConversion(unittest.TestCase):
    def test_c_to_f(self):
        self.assertAlmostEqual(convert_temperature(0, "C", "F"), 32.0)
        self.assertAlmostEqual(convert_temperature(100, "C", "F"), 212.0)

    def test_f_to_c(self):
        self.assertAlmostEqual(convert_temperature(32, "F", "C"), 0.0)
        self.assertAlmostEqual(convert_temperature(212, "F", "C"), 100.0)

    def test_same_unit(self):
        self.assertEqual(convert_temperature(25, "C", "C"), 25)
        self.assertEqual(convert_temperature(77, "F", "F"), 77)

    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            convert_temperature(100, "K", "C")

if __name__ == "__main__":
    unittest.main()