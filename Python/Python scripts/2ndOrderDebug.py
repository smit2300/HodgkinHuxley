import numpy as np
import sys
import matplotlib as plt

def main():

	start = 0       
	stop = 20           
	N = 100                             
	h = (stop - start)/(N-1) 

	u1_0 = -0.4 # This is y0 and it's given
	u2_0 = -0.6 # This is y'0 and it's given

	x_hw = [i for i in irange(start, stop, h)]

	u1,u2 = euler(ode_u1, ode_u2, x_hw, h, u1_0, u2_0)
	u1_rk,u2_rk = rk(ode_u1, ode_u2, x_hw, h, u1_0, u2_0)

	print("\n")

	print("EULER METHOD SOLUTIONS")

	print("\n")

	for i in range(0,len(u1)):
		print("Euler U1: ", u1[i], "Euler U2: ", u2[i])

	print("\n\n\n")

	"""for i in range(0,len(u2)):
		print("Euler U2: ", u2[i])"""

	print("\n")

	print("RUNGE-KUTTA SOLUTIONS")

	print("\n")

	for i in range(0,len(u1_rk)):
		print("RK U1: ", u1_rk[i], "RK U2: ", u2_rk[i])

	print("\n\n\n")

	"""for i in range(0,len(u2_rk)):
		print("RK U2: ", u2_rk[i])"""


# First test ODE
# 2nd order ODE to solve: y'' - 2y' + 2y = e^(2t) * sin(t)
def ode_u1(t, u1, u2):
	u1_prime = u2
	return u1_prime

def ode_u2(t, u1, u2):
	u2_prime = (2*u2) - (2*u1) + ((np.e**(2*t)) * np.sin(t)) #This is given
	return u2_prime

def irange(start, stop, step): 
	while start < stop:
		yield round(start,4)
		start += step

def euler(ode_u1, ode_u2, x_hw, h, u1_0, u2_0):

	u1 = [] #Initialize an array that will house all of our y values
	u2 = [] #Initialize an array that will house all of our y' values. We'll populate this one before u1.

	u1.append(u1_0)
	u2.append(u2_0)

	for n in range(0, len(x_hw)-1):
		u2.append(u2[n] + h * ode_u2(h*n, u1[n], u2[n])) #When this loop is finished iterating we'll have all of u2 so all of the y' function.
		u1.append(u1[n] + h * ode_u1(h*n, u1[n], u2[n]))

	return u1, u2

def rk(ode_u1, ode_u2, x_hw, h, u1_0, u2_0):

	u1 = []
	u2 = []

	u1.append(u1_0)
	u2.append(u2_0)

	for n in range(0,len(x_hw)-1):
		#u2 function and k's
		#Then append the point for u2
		#After than move on to u1 stuff

		k1_u2 = ode_u2(h*n, u1[n], u2[n])
		k1_u1 = ode_u1(h*n, u1[n], u2[n])

		k2_u2 = ode_u2(h*n + 0.5*h, u1[n] + 0.5*h*k1_u2, u2[n] + 0.5*h*k1_u2)
		k2_u1 = ode_u1(h*n + 0.5*h, u1[n] + 0.5*h*k1_u1, u2[n] + 0.5*h*k1_u1)

		k3_u2 = ode_u2(h*n + 0.5*h, u1[n] + 0.5*h*k2_u2, u2[n] + 0.5*h*k2_u2)
		k3_u1 = ode_u1(h*n + 0.5*h, u1[n] + 0.5*h*k2_u1, u2[n] + 0.5*h*k2_u1)

		k4_u2 = ode_u2(h*n + h, u1[n] + h*k3_u2, u2[n] + h*k3_u2)
		k4_u1 = ode_u1(h*n + h, u1[n] + h*k3_u1, u2[n] + h*k3_u1)

		kbar_u2 = (k1_u2 + 2*k2_u2 + 2*k3_u2 + k4_u2) / 6
		kbar_u1 = (k1_u1 + 2*k2_u1 + 2*k3_u1 + k4_u1) / 6

		u2.append(u2[n] + (kbar_u2*h))
		u1.append(u1[n] + (kbar_u1*h))
		
	return u1, u2

if __name__ == "__main__":
    main()