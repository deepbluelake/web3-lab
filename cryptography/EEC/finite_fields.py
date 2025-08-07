class FiniteFieldElement:
    def __init__(self, value, prime):
        if value < 0 or value >= prime:
            raise ValueError(f"Value {value} not in field range 0 to {prime - 1}")
        self.value = value
        self.prime = prime

    def __repr__(self):
        return f"{self.value} (mod {self.prime})"

    def __eq__(self, other):
        return self.value == other.value and self.prime == other.prime

    def __add__(self, other):
        self._check_field(other)
        result = (self.value + other.value) % self.prime
        return FiniteFieldElement(result, self.prime)

    def __sub__(self, other):
        self._check_field(other)
        result = (self.value - other.value) % self.prime
        return FiniteFieldElement(result, self.prime)

    def __mul__(self, other):
        self._check_field(other)
        result = (self.value * other.value) % self.prime
        return FiniteFieldElement(result, self.prime)

    def __truediv__(self, other):
        self._check_field(other)
        inv = pow(other.value, -1, self.prime)  # Modular inverse using Fermat's little theorem
        result = (self.value * inv) % self.prime
        return FiniteFieldElement(result, self.prime)

    def __pow__(self, exponent):
        result = pow(self.value, exponent, self.prime)
        return FiniteFieldElement(result, self.prime)

    def _check_field(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot operate on two numbers in different fields.")
