#Notes from Hodgkin-Huxley Paper:

	#Gna, Gk = f(time,membrane potential)
	#Ena, Ek, El, Cm, Gl = constants

	#Ionic current is divided into components carried by sodium and potassium ions and a small leakage current.
	#Each component of ionic current is determined by a driving force
		#The driving force is measured as an electrical potential difference and a permeability for that specific ion.

	#Ina = Gna * (E - Ena) where E is membrane potential
	#Ena is an equilibrium potential for Ena - It's the sodium resting membrane potential

	#The influence of membrane potential on permeability can be summarized:
		#1: Depolarization causes a transient increase in sodium conductance and a slower but maintained increase in potassium conductance.
			#Literally just TIC and DOC
		#2: These changes in conductance are graded and can be reversid by repolarizing the membrane.

		#These are results of an action potential.

	#THE NATURE OF PERMEABILITY CHANGES
		##Changes in permeability are dependent on membrane potential
		#Not membrane current
		#If the potential for a specific ion (Ena) is less than membrane potential (E) then the current is inward.
		#If the potential (Ena) gets greater than (E) then the current changes sign but still follows the same time course.
		#If you restore the normal membrane potential it causes the ion conductance to decline to a low value.
		#The permeability changes arise from the effect of the electric field on the distribution or orientation of molecules with a charge or dipole moment.

		#Depolarization allows the carrier molecules to move so that sodium current increases as the membrane potential is reduced. 
			#Remember: Ina = Gna * (E - Ena). If you reduce E then current decreases

		#The first effect of depolarization is a movement of negatively charged molecules from the outside to the inside of the membrane.
			#Gives an initial outward current and an inward current does not occur until combined carriers lose sodium to the internal solution and return to the outside of the membrane.

		#Different hypothesis: Sodium movement depends on the distribution of charged particles which do not act as carriesrs in the usual sense, but which allow sodium to pass through the membrane when they occupy particular sites in the membrane.
			#This means that the rate of movement of particles determines the rate that sodium conductance rises to its max but doesn't affect the max value of Gna.
			#Temperature affects this rate of Gna rise but not its max.
			#Transient nature explanation: The activating particles undergo a chemical change after moving from the position they occupy when the membrane potential is high.

		#Steep relation between ionic conductance and membrane potential.
			#Gna can be increased e-fold by a reduction of only 4mV

	#MEMBRANE CURRENT DURING A VOLTAGE CLAMP

	#1): Divide the total membrane current into Capacitor current and ionic current
		#I = CM * dV/dt + Ii
		#Parallel because of current measurements when dV/dt = 0
			#and setting I=0

	#IONIC Current:

	#Ii = Ina + Ik + Il
	#Individual
		#Ina = Gna(E - Ena)
		#Ik = Gk(E - Ek)
		#Il = Gl(E - El)

		#They change E to V here conveniently

		#V = E - Er
		#Vna = Ena - Er
		#Vk = Ek - Er
		#Vl = El - Er

		#Er = absolute value of the resting potential

	#IONIC CONDUCTANCES

	#Want to find equations that describe the conductances accurately and simply
	#Looks like a charging and then discharging capacitor
	#G = V*I so it's directly proportional to voltage in a capacitor.

	#This is the part of the lectures where Irazoqui talks about a delay in space and time for the charging current
	#They had to use G0 and Ginfinity to compensate.

	#POTASSIUM CONDUCTANCE

	#Gk = Gkbar * n^4
		#dn/dt = alphaSubn * (1 - n) - betaSubn * n
		#Units for Gkbar = conductance / cm^2
		#Alpha and Beta are rate constants that vary with voltage but not with time and have frequency units
		#N is dimensionless and varies between zero and one
		
		#Physical basis understanding:
			#Assume that potassium ions can only cross the membrane when four similar particles occupy a certain region of the membrane.
			#n is a proportion of the particles in a certain orientation or position
			#1-n is the proportion that are somewhere else (outside the membrane)
			#Alpha = rate of transfer from outside to inside
			#Beta = rate of transfer from inside to outside
			#Negative charge on particle - Alpha increase, Beta should decrease when membrane is depolarized.

		#N at rest
			#n0 = (alphaSubn0)/(alphaSubn0 + betaSubn0)
			#This means the resting state proportion of particles inside is equal to the proportion of rate outside to inside over the total rates
			#If V is changed suddenly then alphan and betan immediately take values appropriate for the new voltage (They are rates dictated by voltage)
			#The solution of the first equation in this indent is in the exponential form we see inclass (it's sort of like a capacitor)
			#Figure 3 describes the changes in potassium conductance based on different V's achieved with depolarizations
			#At very large negative depolarizations we see conductance rise very rapidly to high levels
			#Not concerned with depolarizations over 110 mV.

			#Trying to connect alphan and betan to voltage
				#alpha and beta still have units of Hz

	#SODIUM CONDUCTANCE
		#Determined in similar method but has to have a falling factor due to the transient nature of sodium inward current


	#Reconstruction of Nerve Behaviour
		
		#Summary of Equations and Parameters
			#Collect total membrane current equations:
				#I = CmdV/dt + gkbarn^4(V-Vk) + gnabarm^3h(V-Vna) + gbarl(V-Vl)
				#dn/dt = alphan(1-n) - Betan * n 
				#dm/dt = alpham(1-m) - Betam * m 
				#dh/dt = alphah(1-h) - Betah * h 

				#alphan = 0.01(V + 10) / (exp((V+10)/10)-1)
				#betan = 0.125exp(V/80)

				#alpham = All 
				#betam = Functions 

				#alphah = of
				#betah = Vm

#Hodgkin-Huxley Numerical Method Steps
	#1: Estimate V1 from V0 
	#2: Estimate n1 from n0
	#3: Calculate (dn/dt)1 from eqn. 7
	#4: Calculate n1 from equation given
	#5:
	#6: Find m1 and h1 by using steps 2-5
	#7: Calculate gbarkn1^4 and gbarnam^3h
	#8: Calculate (dV/dt)1 using values found in 7 and the originally estimated V1
	#9: 

#Integration procedure


#Function and variables hierarchy:

#Given variables from the paper:
#Cm = 1.0
#Vna = -115
#Vk = +12
#Vl = -10.613
#gbarNa = 120
#gbarK = 36
#gbarL = 0.3

#Functions
#alpha and beta are the "bottom" of the hierarchy. They're at the bottom and functions of the root function which is characteristic of an Ordinary Differential Equation

#alpha = f(Vm) ONCE WE LEARN EULER METHOD WE'LL BE ABLE TO USE THIS
#beta = f(Vm) OTHERWISE IT'S ITERATIVE

#tau = f(alpha, beta)

#n = 
#m = 
#h = 
	#Of the form: Xinfinity - (Xinfinity - X0) * e ^ (-t/tau)

#Gk = f(Vm, t, n)
#Gna = f(Vm, t, m, h)

#Jc = f(Cm, dVmdt)
#Jk = f(Gk, Vm, Vk)
#Jna = f(Gna, Vm, Vna)
#Jl = Gl(Vm, Vl)

#Irazoqui Notes

#Numerical Methods
	#Discrete Time Solutions to Continuous Time Problems
		#What it means to solve an equation numerically
		#Discrete - Takes a continuous function and plots points on it at small intervals to approximate the function
		#Continuous - No gaps in the approximation

		#Solutions of differential equations

		#What is an equation
			#Here and most simply: when you relate a dependent variable y to an independent variable x
			#y = f(x)

		#What is a differential equation
			#We relate the derivative of the independent variable to the dependent variable.
			#dy/dx = f(x)

		#What is a second order differential equation
			#Second derivative somewhere in the equation
			#The second derivative of y with respect to x is proportional to the first derivative of y wrt x as well as x
			#d2y/dx2 = f(dy/dx,x)

		#What is an ordinary differential equation
			#All of the derivatives are taken with respect to a single independent variable
			#d2y/dt2 = f(dy/dt,dy/dx,x)

		#What is a homogeneous linear differential equation
			#One where we can parcel out multiple inputs
			#We want this
				#What is the response of a neuron to multiple inputs
				#Want to solve HH for one input, then another input, then another input
				#Then be able to add up all those solutions at the end
				#This means HH needs to be a linear differential equation
				#This can be thought of like linearity of a circuit!!!

		#J examples
			#Equation: Jm = Jc + Jk + Jna + Jl
			#Differential Equation: dVm/dt = Jc/Cm
			#2nd Order DE: HH model
				#It's a partial diff eq because it relates the 2nd derivative of membrane voltage wrt z distance to the first derivative wrt time of Vm
				#We can use the wave equation to convert it to an ordinary differential equation
			#ODE: HH model divided by v^2
				#2nd derivative of Vm wrt time is proportional to the first derivative of Vm wrt time
				#This is a homogeneous diff eq because we can evaluate the output as a result of a sum of inputs
			#See practice file for example here

		#Sampling rate
			#Separation between each sample taken in discrete time

		#Aliasing
			#We're going to sample at t = 0
			#We don't know what we want h to be
			#If we arbitrarily pick h and it's larger than our period of oscillation then we miss a lot of important data.
			#Undersampling and reflecting a high frequency signal as a low sample signal is called aliasing

		#Nyquist-Shannon Sampling Theorem:
			#Signals of interest are band limited
			#Signal only is seen between 2 different frequencies - that's the band

			#In orded to capture all of the data that we want we need to sample at 2 * the highest frequency in our signal

			#Noise is not band-limited
				#So if we sample at too high a frequency we're going to get a bunch of noise
				#To avoid this we make a band pass filter that cuts off right at the highest frequency the signal reaches

				#This frequency rolls off after Fs so we get a new sampling frequency:
					#fsampling = 1/h = (N-1)/T >= 2fc rather than 2fs - should be roughly 5,000 Hz (s^-1)

				#Why would you oversample?
					#The sampling rate of a tv is the pixels
					#If you are sitting far back you aren't able to distinguish those pixels but if you sit up close having more would be more useful.

					#In bioelectricity
						#Because it's free
						#Makes filtering for anti-aliasing much easier because you can roll off much slower

	#Euler Method

		#Actual method for solving differential equations using numerical methods

		#Equation is of the type: dy/dt = y' = f(y,t)
			#The derivative of the dependent variable wrt the independent variable is proportional to the dependent variable (undifferentiated) and the independent variable
			#Just working on time for now, distance is important but for now we're just gonna hold distance constant and solve at a set of times

		#Problem is of this type: yn+1 = yn + h * f(y,t)
			#yn = the solution at an existing point
			#yn+1 = the solution at the next point
			#h*f(y,t) is the interval times a height giving us a rectangular unit of area between the two solutions, yn and yn+1

			#Euler method assumes straight lines
				#yn+1 = yn + h * y'n
				#Rather than make a rectangle it uses the differential solution to y to multiply by h to give a hyper small rectangle
				#The differential solution is the slope between yn and yn+1
				#Rise * run = delta
				#If you take that delta and add it to the current point you'll get the next point

				#This means that if we're given y0 the first one as well as the actual equation we can solve for every point along that equation.





















		