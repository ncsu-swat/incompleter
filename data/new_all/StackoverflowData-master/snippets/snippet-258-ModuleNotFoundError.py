#Source: https://stackoverflow.com/questions/50355133/matplotlib-0-99-mplot3d-attributeerror-list-object-has-no-attribute-ndim
import cobra
import os
from os.path import join
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
data_dir ='/Users/stephenchapman/Documents/research/FBA_algae_digesate/COBRApy/iCZ843/iCZ843_models'
model = cobra.io.read_sbml_model(join(data_dir, "iCZ843_hetero.xml"))
model.reactions[15].upper_bound = -0 #ammonia
model.reactions[15].lower_bound = -98.3
model.reactions[27].upper_bound = -0 #acetate
model.reactions[27].lower_bound = -3.3
model.reactions[14].upper_bound = -0 #phosphate
model.reactions[14].lower_bound = -10
model.reactions[16].upper_bound = -0 #nitrate
model.reactions[16].lower_bound = -30.3
model.reactions[20].upper_bound = -0 #magnesium
model.reactions[20].lower_bound = -0.56
model.reactions[18].upper_bound = -0 #iron
model.reactions[18].lower_bound = -2.16
model.objective = model.reactions[63]
solution = model.optimize()
model.summary()

ac_uptake = []
NH4_uptake = []
growth_rate = []
for i in range(0,85,5):
    model.reactions[27].lower_bound = -i #acetate uptake
    model.reactions[27].upper_bound = -i
    for j in (0,80,5):
        model.reactions[15].lower_bound = -i #NH4 uptake
        model.reactions[15].upper_bound = -i
        print(solution.f)
        growth_rate.append(solution.f)
        ac_uptake.append(model.reactions[27].lower_bound)
        NH4_uptake.append(model.reactions[15].lower_bound)
        plot_ac_uptake = list(range(0,85,5))
        plot_NH4_uptake = list(range(0,85,5))

X = (plot_ac_uptake)
Y = (plot_NH4_uptake)
X, Y = np.meshgrid(X, Y)
Z = (growth_rate)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()