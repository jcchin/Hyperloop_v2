import numpy as np
import matplotlib.pyplot as plt

p_tunnel = np.loadtxt('../data_files/pressure_zoom/p_tunnel.txt', delimiter = '\t')
Re = np.loadtxt('../data_files/pressure_zoom/Re.txt', delimiter = '\t')
A_tube = np.loadtxt('../data_files/pressure_zoom/A_tube.txt', delimiter = '\t')
T_tunnel = np.loadtxt('../data_files/pressure_zoom/T_tunnel.txt', delimiter = '\t')
L_pod = np.loadtxt('../data_files/pressure_zoom/L_pod.txt', delimiter = '\t')
power = np.loadtxt('../data_files/pressure_zoom/comp_power.txt', delimiter = '\t')
steady_vac = np.loadtxt('../data_files/pressure_zoom/vac_power.txt', delimiter = '\t')
total_energy = np.loadtxt('../data_files/pressure_zoom/total_energy.txt', delimiter = '\t')

prop_energy = np.loadtxt('../../../paper/images/data_files/pressure_zoom/prop_energy.txt', delimiter = '\t')
tube_energy = np.loadtxt('../../../paper/images/data_files/pressure_zoom/tube_energy.txt', delimiter = '\t')

pod_energy = total_energy-tube_energy

comp_scale = 25641305
power = power*comp_scale

fig = plt.figure(figsize = (3.25,3.5), tight_layout = True)
ax = plt.axes()
plt.setp(ax.get_xticklabels(), fontsize=8)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.plot(p_tunnel, A_tube, 'b-', linewidth = 2.0)
plt.xlabel('Tube Pressure (Pa)', fontsize = 10, fontweight = 'bold')
plt.ylabel('Tube Area ($m^2$)', fontsize = 10, fontweight = 'bold')
ax.set_xticks([40,250,500])
plt.savefig('../graphs/pressure_trades/pressure_vs_Area_zoom.png', format = 'png', dpi = 300)
#plt.show()

fig = plt.figure(figsize = (3.25,3.5), tight_layout = True)
ax1 = fig.add_subplot(211)
line1, = ax1.plot(p_tunnel, steady_vac, 'g-', linewidth = 2.0, label = 'Vaccum Power')
line2, = ax1.plot(p_tunnel, power, 'b-', linewidth = 2.0, label = 'Compressor Power')
ax1.set_ylabel('Power (hp)', fontsize = 10, fontweight = 'bold')
plt.legend(handles = [line1, line2], loc = 1, fontsize = 8)
ax1.set_xticks([40,250,500])
#ax1.set_yticks([14000, 28000, 36000, 56000])
ax2 = fig.add_subplot(212)
ax2.plot(p_tunnel, total_energy/(1.0e6), 'r-', linewidth = 2.0)
ax2.set_xlabel('Tube Pressure (Pa)', fontsize = 10, fontweight = 'bold')
ax2.set_ylabel('Total Energy Cost \n per Year (Million USD)', fontsize = 10, fontweight = 'bold')
ax2.set_xticks([40,250,500])
#ax2.set_yticks([0,10,20,30])
plt.setp(ax1.get_xticklabels(), fontsize=8)
plt.setp(ax1.get_yticklabels(), fontsize=8)
plt.setp(ax2.get_xticklabels(), fontsize=8)
plt.setp(ax2.get_yticklabels(), fontsize=8)
plt.savefig('../graphs/pressure_trades/pressure_vs_power_zoom.png', format = 'png', dpi = 300)
# plt.show()

fig = plt.figure(figsize = (4.,4.), tight_layout = True)
ax1 = fig.add_subplot(211)
line1, = ax1.plot(p_tunnel, tube_energy/.13/1e6, 'g-', linewidth = 2.0, label = 'Vacuum')
#line2, = ax1.plot(p_tunnel, prop_energy, 'b-', linewidth = 2.0, label = 'Yearly Compressor Energy')
line2, = ax1.plot(p_tunnel, pod_energy/.13/1e6, 'b-', linewidth = 2.0, label = 'Pod')
ax1.set_ylabel('Annual Energy \n '+r'(kw-hr $\times 10^6$)', fontsize = 10, fontweight = 'bold')
plt.legend(handles = [line1, line2], loc = 1, fontsize = 8)
ax1.set_xticks([40,250,500])
#ax1.set_yticks([14000, 28000, 36000, 56000])
ax2 = fig.add_subplot(212)
ax2.plot(p_tunnel, total_energy/(1.0e6), 'r-', linewidth = 2.0)
ax2.set_xlabel('Tube Pressure (Pa)', fontsize = 10, fontweight = 'bold')
ax2.set_ylabel('Total Energy Cost \n per Year (Million USD)', fontsize = 10, fontweight = 'bold')
ax2.set_xticks([40,250,500])
#ax2.set_yticks([0,10,20,30])
plt.setp(ax1.get_xticklabels(), fontsize=8)
plt.setp(ax1.get_yticklabels(), fontsize=8)
plt.setp(ax2.get_xticklabels(), fontsize=8)
plt.setp(ax2.get_yticklabels(), fontsize=8)
plt.savefig('../graphs/pressure_trades/pressure_vs_power_zoom.png', format = 'png', dpi = 300)
plt.show()