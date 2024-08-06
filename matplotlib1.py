# matplotlib

# math   graph   library

# used for data visualization


# Line graph

# import matplotlib.pyplot as plt
#
# x = [10,20,30,40]
# y = [10,20,30,40]

# plt.plot(x,y,ls="solid)
# plt.plot(x,y,marker="*", ls="dotted",mfc="r", mec="y")
# plt.plot(x,y,ls'"dashed)
# plt.plot(x,y,ls="dashdot)
# plt.plot(x,y,ls="None")
# plt.plot(x,y,marker="s", ls="dotted",mfc="r", mec="y")
# plt.xlabel("X-axis")
# plt.plot(x,y,marker="|", ls="dotted",mfc="r", mec="y")
#
# plt.ylabel("Y-axis")
# plt.title("Line Graph")
# plt.show()

# marker

# o - circle
# s - square
# 0 - diamond
# p - pentagon
# h - hexagon
# . - point
# * - star
# + - plus
# | - vline
# - - Hline

# color

# edge color - mec

# face color - mfc


# Pie Graph

# import matplotlib.pyplot as plt
#
# std_performance=["Good", "Excellent", "Average", "poor"]
# std_values=[10,20,5,19]
#
# plt.pie(std_values,labels=std_performance, autopct="%2.1f%%", explode=[0.1,0.0,0.0,0.0],shadow=True)
# plt.legend(title="Performance")
# # plt.figure(figsize=(1.1,2.1))
# plt.show()


# Bar Graph

import matplotlib.pyplot as plt

language = ["SQl","Java","Python"]
Ranking = [70,90,85]
x= ["red","yellow","blue"]
plt.bar(language,Ranking,color=x)
plt.xlabel("Language")
plt.ylabel("Ranking")
plt.title("Details of Languages")
plt.show()













