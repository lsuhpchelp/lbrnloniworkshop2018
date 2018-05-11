#!/usr/bin/env python

import scipy.integrate as integrate
import scipy.special as special
result_integ, err = integrate.quad(lambda x: x**2, 1, 3)
result_real = 1./3.*(3.**3-1**3)

print "result_real=", result_real
print "result_integ=", result_integ