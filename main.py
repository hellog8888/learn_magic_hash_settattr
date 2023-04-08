class Dimensions:
    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if value not in (int, float) and value < 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

s_inp = input()

lst_dims = []

for i in s_inp.split(';'):
    a1, b1, c1 = i.split()
    lst_dims.append(Dimensions(float(a1.strip(' "')), float(b1.strip(' "')), float(c1.strip(' "'))))

lst_dims = sorted(lst_dims, key=lambda x: hash(x))
