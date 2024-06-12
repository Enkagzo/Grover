import qsharp
from qsharp import Result as r
import numpy
import matplotlib.pyplot as plt

qsharp.init(project_root = '../Grover')

# First graph: on 3 qubits
nbQbits = 3
l1 = []
# Prepare the alternate result
excepted = [r.Zero] * nbQbits
for i in range(1, nbQbits, 2):
    excepted[i] = r.One
    
for i in range(50):
    result = 0
    for y in range(100):
        result += 1 if qsharp.eval(f"Grover.GroverCall({nbQbits},{i})") == excepted else 0
    l1.append(result)

# Plotting the probabilities
plt.plot(l1, linestyle='-', color='blue')
plt.title('Probabilities Plot')
plt.xlabel('Number of Iteration')
plt.ylabel('Probability')
plt.ylim(0, 100)  
plt.grid(True)
plt.show()

print("Part One finished")

# First graph: on 5 qubits
nbQbits = 5
l2 = []
# Prepare the alternate result
excepted = [r.Zero] * nbQbits
for i in range(1, nbQbits, 2):
    excepted[i] = r.One
    
for i in range(50):
    result = 0
    for y in range(50):
        result += 2 if qsharp.eval(f"Grover.GroverCall({nbQbits},{i})") == excepted else 0
    l2.append(result)

# Plotting the probabilities
plt.plot(l2, linestyle='-', color='red')
plt.title('Probabilities Plot')
plt.xlabel('Number of Iteration')
plt.ylabel('Probability')
plt.ylim(0, 100)  
plt.grid(True)
plt.show()
print("Part Two finished")

# First graph: on 10 qubits
nbQbits = 10
l3 = []
# Prepare the alternate result
excepted = [r.Zero] * nbQbits
for i in range(1, nbQbits, 2):
    excepted[i] = r.One
    
for i in range(50):
    result = 0
    for y in range(25):
        result += 4 if qsharp.eval(f"Grover.GroverCall({nbQbits},{i})") == excepted else 0
    l3.append(result)

# Plotting the probabilities
plt.plot(l3, linestyle='-', color='green')
plt.title('Probabilities Plot')
plt.xlabel('Number of Iteration')
plt.ylabel('Probability')
plt.ylim(0, 100)  
plt.grid(True)
plt.show()

print("Part Three finished")


# Let's talk on those graph! 
# On remarque que les trois graphs sont périodiques,
# Plus nous avons de qbits, plus la prériode longue
# Nous avons alors besoins d'adapter le nombre 
# d'itération de l'algorithme de Grover nécessaire 
# pour avoir une précision optimal est proposionelle 
# au nombre de qbits

# Let's see the 3 alligned
plt.plot(l1, linestyle='-', color='blue')
plt.plot(l2, linestyle='-', color='red')
plt.plot(l3, linestyle='-', color='green')
plt.title('Probabilities Plot')
plt.xlabel('Number of Iteration')
plt.ylabel('Probability')
plt.ylim(0, 100)  
plt.grid(True)
plt.show()