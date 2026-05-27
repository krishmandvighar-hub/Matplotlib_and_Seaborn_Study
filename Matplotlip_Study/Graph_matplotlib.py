'''
#------------------------------Topic: 1.Matplotlib Markers----------------------------

#1.Markstyle --> marker
#2.markersize --> ms
#3.markeredgecolor --> mec
#4.markerfacecolor --> mfc

import matplotlib.pyplot as plt
import numpy as np

year = np.array([1,2,3,4,5])
salary = np.array([15000,16000,17000,15000,20000])

plt.title("Relationship between Years and Salary")
plt.xlabel("Years")#lable()
plt.ylabel("Salary")

plt.plot(year,salary,marker="o",ms=20,mec="r",mfc="r")
plt.show()

#Format Strings fmt(marker|line|color)
work = np.array([7,8,9,10,11,12])#Direct relation between work and pay
pay = np.array([500,550,600,650,700,750])

plt.title("Relationship between Work and Pay ")
plt.xlabel("Work")#lable()
plt.ylabel("Pay")
	   
plt.plot(work,pay,"o:r")
plt.show()

#-------------------------------Topic: 2.Matplotlib Line method-------------------------

#1.line style -->linestyle or ls
#2.Line color -->color or  c
#3.Line Width -->linewidth or lw
price = np.array([3, 8, 1, 10])

plt.title("Relationship between ")
plt.xlabel("Demand")#lable()
plt.ylabel("Price")

plt.plot(price, linestyle = 'dotted',color = 'r',linewidth="10.5")
plt.show()
#Shotcuts
price2 = np.array([4, 2, 9, 6])

plt.title("Relationship between ")
plt.xlabel("Demand")#lable()
plt.ylabel("Price")

plt.plot(price2, ls = '--',c="hotpink" , lw="10.2")
plt.show()
#multiple Lines
plt.plot(price)
plt.plot(price2)

plt.title("Relationship between ")
plt.xlabel("Demand")#lable()
plt.ylabel("Price")

plt.show()

#---------------------------Topic: 3.Matplotlib Lables(title,xlable,ylable)-----------------------

x2 = np.array([0, 85, 90, 95, 100, 15, 110, 115, 10, 115])
y2 = np.array([240, 20, 260, 70, 280, 290, 300, 310, 320, 330])

plt.plot(x2, y2)



plt.show()

#To set the properties to the lable we use "fontdict" in the title, xlable, ylable 
speed = np.array([10, 20, 25, 30, 35, 40, 45, 50, 55, 60])
distance = np.array([10,9,8,7,6,5,4,3,2,1])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1,loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(speed, distance)
plt.show()

#---------------------------------Topic:4.Matplotlib grid---------------------------------------

x4 = np.array([80, 85, 0, 95, 00, 105, 10, 115, 120, 15])
y4 = np.array([240, 50, 260, 270, 280, 290, 30, 310, 30, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1,loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2,loc = 'right')
plt.ylabel("Calorie Burnage", fontdict = font2,loc = 'bottom')

plt.plot(x4, y4)
plt.grid()

plt.show()

#set to properties to grid(color = 'color', linestyle = 'linestyle', linewidth = number)
x5 = np.array([180, 85, 190, 295, 0, 15, 99, 115, 120, 125])
y5 = np.array([140, 650, 460, 470, 580, 490, 400, 610, 420, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1,loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2,loc = 'right')
plt.ylabel("Calorie Burnage", fontdict = font2,loc = 'bottom')

plt.plot(x5, y5)
plt.grid(color="r",ls=":",lw='0.5')#--

plt.show()

#------------------------------------Topic:5.Matplotlib subplot---------------------------

plt.subplot(2, 4, 1)
plt.plot(year,salary)

plt.subplot(2, 4, 2)
plt.plot(work,pay)

plt.subplot(2, 4, 3)
plt.plot(x2,y2)

plt.subplot(2, 4, 4)
plt.plot(speed,distance)

plt.subplot(2, 4, 5)
plt.plot(x4,y4)

plt.subplot(2, 4, 6)
plt.plot(x5,y5)

plt.subplot(2, 4, 7)
plt.plot(price2)

plt.subplot(2, 4, 8)
plt.plot(price)

plt.show()
'''
#-----------------------------Topic:6.Matplotlib Scatter----------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, c = 'g')

plt.show()

#ColorMap

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#new array for colours
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis',s=100.0,alpha=0.5)
#Size,Alpha(transparency )
plt.colorbar()

plt.show()
#--------------------------------Topic: 7.Metplotlib Bar-----------------------------

#color
#width
sub=np.array(["Maths","Physics","Chemistry","IT","Economy","English"])
marks=np.array([98,88,82,95,88,65])
col=np.array(["r","g","r","g","r","g"])

plt.bar(sub,marks,color=col,width=0.1)
plt.show()

#horizontal bar
#height
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y,height=0.1)#imp barh()
plt.show()

#--------------------------------Topic: 7.Metplotlib Histogram-----------------------------

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 


#--------------------------------Topic: 7.Metplotlib Pie-----------------------------

y = np.array([35, 25, 25, 15])

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
col=["r","y","r","k"]

plt.pie(y, labels = mylabels,startangle = 90,explode = myexplode,shadow = True,colors=col,)
plt.legend(title = "Four Fruits:")
plt.show() 






















