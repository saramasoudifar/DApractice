import matplotlib.pyplot as plt

days = ['sat','sun','mon','tue','wed','thu','fri']
company_1 = [1000,1250,2200,1420,1700,2200,1050]
company_2 = [850,940,590,730,550,420,950]

plt.subplot(1,2,1)
plt.title("company_1")
plt.plot(days,company_1,label = 'company_1')
plt.legend()

plt.subplot(1,2,2)
plt.title("company_2")
plt.bar(days,company_2,label = 'company_2')
plt.legend()

plt.savefig('companies.jpg')
plt.show()