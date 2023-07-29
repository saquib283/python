import matplotlib.pyplot as plt

slices=[7,3,4,12]
activities=["sleeping","eating","playing","studying"]
colrs=['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=colrs,
        startangle=70,
        shadow=True,
        explode=(0,0,0,0.05),
        autopct='%1.1f%%')
plt.title('pie plot')
plt.show()