
class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Performs addition without using class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Uses class-level attribute and performs multiplication."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
