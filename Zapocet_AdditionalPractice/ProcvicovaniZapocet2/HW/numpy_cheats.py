import numpy as np

#Většinu věcí vrací numpy jako pole, vždy si kontroluj co to vypisuje pls (prostě printem)

# Creating an array from a list
arr = np.array([1, 2, 3, 4, 5])

# Creating specific arrays
zeros = np.zeros((3, 4))   # A 3x4 matrix of 0.0
ones = np.ones((2, 2))     # A 2x2 matrix of 1.0
rng = np.arange(1, 10, 2)  # [0, 2, 4, 6, 8] - like range() but returns an array| VRACÍ TO POLE!
#arange(start,end-1,krok) - čili kdybychom začali od 1 (arange(1,10,2)), pak: [1 3 5 7 9]

# NumPy (Vectorized)
myarr = np.array([1, 2, 3])
new_arr = myarr * 2  # Result: [2, 4, 6]

#Přidávání prvků
# Add to the end
arr = np.append(arr, 40) 
# Result: [10, 20, 30, 40]
# Insert 15 at index 1
arr = np.insert(arr, 1, 15) 
# Result: [10, 15, 20, 30, 40]

#Odebírání prvků
arr = np.array([10, 15, 20, 30])
# Remove the item at index 1 (the number 15)
arr = np.delete(arr, 1)
# Result: [10, 20, 30]

#Special odebírání
data = np.array([1, 0, 2, 0, 3])
# "Keep everything that is NOT zero"
data = data[data != 0] 
# Result: [1, 2, 3]

# matrix[row, column]
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(matrix[0, 1])    # 20 (First row, second column)
print(matrix[:, 1])     # [20, 50, 80] (All rows, only the second column)
print(matrix[1, 1:])    # [50, 60] (Second row, from second column to the end)


#Reshaping & stuff
a = np.arange(6)       # [0, 1, 2, 3, 4, 5]
b = a.reshape((2, 3))  # Turns it into a 2x3 matrix
c = b.T                # Transpose: flips rows and columns (now 3x2)

#fungujou i nějaké početní věci
prices = np.array([100, 25, 49, 16])
roots = np.sqrt(prices)  # [10.0, 5.0, 7.0, 4.0]

#Rozdíl mezi sčítání sloupců a řádků (axis) [stále vrací jako pole]
data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(data))          # 21 (Total sum)
print(np.sum(data, axis=0))  # [5, 7, 9] (Sums of columns)
print(np.sum(data, axis=1))  # [6, 15] (Sums of rows)

#Výpis velikosty matice/pole
data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Data: {np.shape(data)}") # (2,3) (výška,šířka)





#testing stuff here:
print("-------------------------------------------------")

mynumpy = np.arange(1,10,1)
mynumpy= mynumpy.reshape((3,3))
print(f"{mynumpy}\n\n")
mynumpy=mynumpy*10
print(mynumpy)

numpyArray = np.array([12, 25, 17, 40, 10, 55, 18])
adults = numpyArray[numpyArray>=18] #vezme všechny >= 18 | v podstatě substituje for a if
print(adults)
numpyArray = np.append(numpyArray,5)
print(numpyArray)