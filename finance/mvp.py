u = np.array([0.20, 0.13, 0.17])
sig = np.array([0.25, 0.28, 0.20])

c = np.array([
    [0.25**2,0.30*0.25*0.28,0.15*0.25*0.20],
    [0.30*0.25*0.28, 0.28**2, 0.0*0.24*0.25],
    [0.15*0.25*0.20, 0.00*0.24*0.25, 0.20**2]
])

c_1 = np.linalg.inv(c)
m = np.array([0.20, 0.13, 0.17])
u = np.array([1,1,1])

np.matmul([1,1,1], c_1)

w = np.matmul(u, c_1)/np.matmul(np.matmul(u, c_1), u.T)
print("Expected return: ",np.matmul(m, w.T)) #uv
print("Standard Deviation: ",np.sqrt(np.matmul(np.matmul(w, c), w.T))) # sigma v

print("Weights: ",w)
