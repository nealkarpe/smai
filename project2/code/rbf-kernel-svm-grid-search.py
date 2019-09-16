import subprocess
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

log_C = list(range(-5,16,2))
log_gamma = list(range(-15,4,2))

log_C_vals = []
log_gamma_vals = []
accuracies = []


for elem1 in log_C:
	for elem2 in log_gamma:
		command_string = "python3 run.py --classifier_type rbf-svm --num_batches 10 --log_C "+str(elem1)+ " --log_gamma "+str(elem2)
		command_arr = command_string.split()
		proc = subprocess.Popen(command_arr, stdout=subprocess.PIPE)
		(out, err) = proc.communicate()
		out = out.decode("utf-8")
		accuracy = float(out.split("\n")[-2])
		log_C_vals.append(elem1)
		log_gamma_vals.append(elem2)
		accuracies.append(accuracy)
		print(elem1, elem2, accuracy)

# x = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
# y = [-15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3]
# z = [0.0]*len(x)
# dx = [0.5]*len(x)
# dy = [0.5]*len(x)
# dz = [0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.0986, 0.1476, 0.1266, 0.098, 0.098, 0.098, 0.098, 0.098, 0.098, 0.101, 0.1914, 0.284, 0.29219999999999996, 0.11439999999999999, 0.098, 0.098, 0.098, 0.098, 0.1016, 0.197, 0.29779999999999995, 0.3266, 0.3302, 0.2274, 0.099, 0.098, 0.098, 0.098, 0.197, 0.29500000000000004, 0.32480000000000003, 0.3264, 0.3266, 0.2274, 0.099, 0.098, 0.098, 0.098, 0.29599999999999993, 0.3184, 0.30920000000000003, 0.3158, 0.3264, 0.2274, 0.099, 0.098, 0.098, 0.098, 0.3152, 0.3048, 0.2978, 0.3156, 0.3264, 0.2274, 0.099, 0.098, 0.098, 0.098, 0.30240000000000006, 0.28640000000000004, 0.29300000000000004, 0.3156, 0.3264, 0.2274, 0.099, 0.098, 0.098, 0.098, 0.27979999999999994, 0.2824, 0.29300000000000004, 0.3156, 0.3264, 0.2274, 0.099, 0.098, 0.098, 0.098, 0.27440000000000003, 0.2824, 0.29300000000000004, 0.3156, 0.3264, 0.2274, 0.099, 0.098, 0.098, 0.098, 0.2736, 0.2824, 0.29300000000000004, 0.3156, 0.3264, 0.2274, 0.099, 0.098, 0.098, 0.098]

x = log_C_vals
y = log_gamma_vals
z = [0.0]*len(x)
dx = [0.5]*len(x)
dy = [0.5]*len(x)
dz = accuracies

for i in range(len(dz)):
	if dz[i]==max(dz):
		print("max accuracy", x[i],y[i],dz[i])
		break

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

ax1.bar3d(x, y, z, dx, dy, dz)
ax1.set_xlabel('log C')
ax1.set_ylabel('log gamma')
ax1.set_zlabel('Accuracy')
plt.show()