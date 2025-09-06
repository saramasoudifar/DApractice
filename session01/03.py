import matplotlib.pyplot as plt

days = ['sat','sun','mon','tue','wed','thu','fri']
company_1 = [1000,1250,1300,1420,1700,1100,1050]

plt.plot(days,company_1,"g--P",label = 'company_1')

plt.scatter('sat',700)
plt.scatter('wed',1500)
plt.plot(['sat','wed'],[700,1500])
plt.plot(['sat','fri'],[400,400])
plt.plot(['thu','thu'],[0,2000])

plt.ylim([0,2000])
plt.show()