import matplotlib.pyplot as plt


days = ['sat','sun','mon','tue','wed','thu','fri']
company_1 = [1000,1250,2200,1420,1700,2200,1050]
company_2 = [850,940,590,730,550,420,950]

# plt.plot(days,company_1,label = 'company_1',color = 'red',linestyle = 'dashed',marker = 'P')
plt.plot(days,company_1,"g--P",label = 'company_1')

plt.bar(days,company_2,label = 'company_2',color = 'blue')
plt.scatter(days,company_2,label = 'company_2',color = 'green',s=200,alpha=0.5)


plt.xlabel('days')
plt.ylabel('sells')

plt.ylim([0,5000])

plt.legend()
plt.grid()


plt.show()