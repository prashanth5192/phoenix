import numpy as np
from operator import truediv
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import csv, sys

long_cons_filename = sys.argv[1]
long_nocons_filename = sys.argv[2]
short_cons_filename = sys.argv[3]
short_nocons_filename = sys.argv[4]
cons_load_graph = sys.argv[5]
nocons_load_graph = sys.argv[6]

long_job_finish_times_cons = []
long_job_finish_times_uncons = []
long_task_completion_times_cons = []
long_task_completion_times_uncons = []
cons_load_big=[]
cons_load_small=[]
cons_load_all=[]
nocons_load_big=[]
nocons_load_small=[]
nocons_load_all=[]
short_job_finish_times_cons = []
short_job_finish_times_uncons = []
short_task_completion_times_cons = []
short_task_completion_times_uncons = []

long_cons_reader = csv.reader(open(long_cons_filename), delimiter=',')
long_nocons_reader = csv.reader(open(long_nocons_filename), delimiter=',')
short_cons_reader = csv.reader(open(short_cons_filename), delimiter=',')
short_nocons_reader = csv.reader(open(short_nocons_filename), delimiter=',')

cons_load_reader = csv.reader(open(cons_load_graph), delimiter=' ')
nocons_load_reader = csv.reader(open(nocons_load_graph), delimiter=' ')

for row in long_cons_reader:
	long_job_finish_times_cons.append(float(row[3]))
	long_task_completion_times_cons.append(float(row[0]))

for row in long_nocons_reader:
	long_job_finish_times_uncons.append(float(row[3]))
	long_task_completion_times_uncons.append(float(row[0]))

for row in short_cons_reader:
	short_job_finish_times_cons.append(float(row[3]))
	short_task_completion_times_cons.append(float(row[0]))

for row in short_nocons_reader:
	short_job_finish_times_uncons.append(float(row[3]))
	short_task_completion_times_uncons.append(float(row[0]))

for row in cons_load_reader:
	cons_load_all.append(float(row[1]))
	cons_load_big.append(float(row[3]))
	cons_load_small.append(float(row[5]))

for row in nocons_load_reader:
	nocons_load_all.append(float(row[1]))
	nocons_load_big.append(float(row[3]))
	nocons_load_small.append(float(row[5]))


cons_long_average = ((sum(long_job_finish_times_cons)/len(long_job_finish_times_cons)))
nocons_long_average = ((sum(long_job_finish_times_uncons)/len(long_job_finish_times_uncons)))
cons_short_average = ((sum(short_job_finish_times_cons)/len(short_job_finish_times_cons)))
nocons_short_average =((sum(short_job_finish_times_uncons)/len(short_job_finish_times_uncons)))

print "constrained_long_jobs %f" % cons_long_average
print "constrained_short_jobs %f" % cons_short_average
print "Unconstrained_long_jobs %f" % nocons_long_average
print "Unconstrained_short_jobs %f" % nocons_short_average

long_cons_rep = []
long_cons_rep = np.repeat(cons_long_average,len(long_task_completion_times_cons))
short_cons_rep = []
short_cons_rep = np.repeat(cons_short_average,len(short_task_completion_times_cons))
long_nocons_rep = []
long_nocons_rep = np.repeat(nocons_long_average,len(long_task_completion_times_uncons))
short_nocons_rep = []
short_nocons_rep = np.repeat(nocons_short_average,len(short_task_completion_times_uncons))


fig = plt.figure(num=None, figsize=(60, 20), dpi=200, facecolor='w', edgecolor='none')

plt1 = fig.add_subplot(311)
x = np.arange(len(short_task_completion_times_cons))
y = np.arange(0,max(short_task_completion_times_uncons),1000.0)
plt1.plot(x, short_job_finish_times_cons, 'rx', label='Constraint')
plt1.plot(x, short_job_finish_times_uncons, 'b-', label='Unconstrained')

plt1.plot(x,short_cons_rep,'r')
plt1.plot(x,short_nocons_rep,'b')

#plt1.scatter(short_task_completion_times_cons, short_job_finish_times_cons, color= 'r', edgecolors='none', label='constraint')
#plt1.scatter(short_task_completion_times_uncons, short_job_finish_times_uncons, color= 'b', edgecolors='none', label='unconstraint')
#plt1.plot(x, short_job_finish_times_cons, 'rx', label='Constraint')
#plt1.plot(x, short_job_finish_times_uncons, 'b--', label='Unconstraint')
plt1.set_yscale('symlog')
plt1.set_xlabel('Job number')
plt1.set_ylabel('QoS violation % deterioration')
plt1.set_title('Short Jobs Constrained vs Unconstrained')
plt1.legend(['Constrained','Unconstrained'],loc='lower right')


plt = fig.add_subplot(312)
x = np.arange(len(long_task_completion_times_cons))
y = np.arange(0,max(long_task_completion_times_uncons),100.0)
#log_y_values = np.log(long_job_finish_times_cons)
#log_y1_values = np.log(long_job_finish_times_uncons)
#plt.scatter(long_task_completion_times_cons, long_job_finish_times_cons, color= 'r', edgecolors='none', label='constraint')
#plt.scatter(long_task_completion_times_uncons, long_job_finish_times_uncons, color= 'b', edgecolors='none', label='unconstraint')
plt.plot(x, long_job_finish_times_cons, 'rx', label='Constraint')
plt.plot(x, long_job_finish_times_uncons, 'b-', label='Unconstrained')
plt.plot(x,long_cons_rep,'r')
plt.plot(x,long_nocons_rep,'b')
plt.set_yscale('symlog')
plt.set_xlabel('Job number')
plt.set_ylabel('QoS violation % deterioration')
plt.set_title('Long Jobs Constrained vs Unconstrained')
plt.legend(loc='lower right')
#plt.show()
#long_fig.savefig('long_jobs.png',bbox_inches='tight')
#short_fig = plt.figure(num=None, figsize=(20, 3), dpi=100, facecolor='w', edgecolor='none')
#plt.show()
#short_fig.savefig('short_jobs.png',bbox_inches='tight')
#load_fig = plt.figure.Figure(num=None, figsize=(20, 3), dpi=100, facecolor='w', edgecolor='none')

plt2 = fig.add_subplot(313)
x = np.arange(len(cons_load_all))
y = np.arange(len(nocons_load_all))

cons_average_util = ((sum(cons_load_all)/len(cons_load_all)))
nocons_average_util = ((sum(nocons_load_all)/len(nocons_load_all)))

#print cons_average_util
#z = len(cons_average_util)
cons_rep = []
cons_rep = np.repeat(cons_average_util,len(cons_load_all))
nocons_rep = np.repeat(nocons_average_util,len(nocons_load_all))

plt2.plot(x, cons_load_all, 'rx')
#plt.plot(x, , color='b')
#plt.plot(y, , color='r')
plt2.plot(y, nocons_load_all , 'b-')

plt2.plot(x,cons_rep,'g')
#plt2.plot(x,nocons_rep,'b')
#plt2.plot(x,nocons_average_util,'b')
#plt2.set_yscale('symlog')

plt2.set_xlabel('Datacenter monitor interval')
plt2.set_ylabel('Datacenter Utilization %')
plt2.set_title('Constrained vs Unconstrained Load')
plt2.legend(['Constrained','Unconstrained'],loc='lower right')
#plt.show()
fig.savefig(str(sys.argv[7])+'.png',bbox_inches='tight')
