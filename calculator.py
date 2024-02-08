grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

flatRate = 0.20
standardDeduction = 10000.0
dependentDeduction = 3000.0

taxableIncome = grossIncome - standardDeduction - dependentDeduction * numDependents
incomeTax = flatRate * taxableIncome

print(f'The income tax is ${incomeTax}')
