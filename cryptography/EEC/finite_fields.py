class FiniteFieldElement:
    def __init__(self, value, prime):
        if value < 0 or value >= prime:
            raise ValueError(f"Value {value} not in field range 0 to {prime-1}")
        self.value = value
        self.prime = prime

    def __repr__(self):
        return f"{self.value} (mod{self.prime})"
    
    def __eq__(self, other):
        return self.value == other.value and self.prime == other.prime
    
    def __add__(self, other):
        