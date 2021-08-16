from ctypes import *
import numpy as np
from numpy.ctypeslib import load_library,ndpointer

libc = CDLL("libc.so.6")
printf = libc.printf

msg_int = c_int(0)
msg_char = c_char_p(b'Hello world!')
msg_array = (c_int * 4)(1, 2, 3, 4)

print(msg_int, msg_int.value)
print(msg_char, msg_char.value)
for i in msg_array:
	print(i)
print("Index Array", msg_array[2])

class coste(Union):
	_fields_ = [
		("coste1", c_long),
		("coste2", c_int),
		("nombre", c_char),
	]

value = input("Introduce numero: ")
my_cost = coste(int(value))
print("Coste1 %ld" % coste.coste1)
print("Coste2 %d", coste.coste2)
print("Coste3 %s", coste.nombre)

def dgesv(N,A,B):
	A = np.asfortranarray(A.astype(np.float64))
	B = np.asfortranarray(B.astype(np.float64))

	cN=c_int(N)
	NRHS=c_int(1)
	LDA=c_int(N)
	IPIV=(c_int * N)()
	LDB=c_int(N)
	INFO=c_int(1)

	lapack=load_library(’liblapack.so’,’/usr/lib/’)
	lapack.dgesv_.argtypes=[POINTER(c_int),
							POINTER(c_int),
							ndpointer(dtype=np.float64,ndim=2,flags=’FORTRAN’),
							POINTER(c_int), POINTER(c_int),
							ndpointer(dtype=np.float64,
									  ndim=2,
									  flags=’FORTRAN’),
							POINTER(c_int),POINTER(c_int)]
	lapack.dgesv_(cN,NRHS,A,LDA,IPIV,B,LDB,INFO) 
	return B

print(dgesv(2,np.array([[1,2],[1,4]]),np.array([[1,3]])))
