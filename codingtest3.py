class newcomplex(object):
    def init(self, real, complexs):
        self.real = real
        self.complex = complexs
        
    def __str__(self):
        return self.real + '+' + self.complex + 'i'
            
    def __add__(self, other):
        total_real = self.real + other.real
        total_complex= self.complex + other.complex
        return newcomplex(total_real, total_complex)
