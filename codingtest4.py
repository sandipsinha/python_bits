class newcomplex(object):
	def __init__(self, real, complexs):
            self.real = real
            self.complex = complexs

        def __str__(self):
            if self.complex < 0:
		sign=''
	    else:
		sign='+'    
            return str(self.real) + sign + str(self.complex) + 'i'

        def __add__(self, other):
            total_real = self.real + other.real
            total_complex= self.complex + other.complex
            return newcomplex(total_real, total_complex)

        def __mod__(self, other):
            total_real = self.real % other.real
            total_complex= self.complex % other.complex
            return newcomplex(total_real, total_complex)

        def __sub__(self, other):
            total_real = self.real - other.real
            total_complex= self.complex - other.complex
            return newcomplex(total_real, total_complex)
