import matplotlib.pyplot as plt

days = ['sat','sun','mon','tue','wed','thu','fri']
company_1 = [1000,1250,1500,1420,1300,1800,1050]

mean = sum(company_1)/len(company_1)

plt.plot(days,company_1,'b',label = 'company_1')
plt.plot(['sat','fri'],[mean,mean],'g--P',label = 'mean')

plt.show()