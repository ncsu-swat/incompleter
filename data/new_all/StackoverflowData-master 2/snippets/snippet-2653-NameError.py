#Source: https://stackoverflow.com/questions/67834528/scipy-and-numpy-upgrade-generates-typeerror-cannot-cast-array-data-from-dtype
y_trajectory = scipy.integrate.odeint(growth_a_derivs, y_start, t_array, atol=eps, args=myargs)