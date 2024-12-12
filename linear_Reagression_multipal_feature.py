import pandas as pd
import matplotlib.pyplot as plt

dic={
    "areas":[3300,4000,2300,4800,50000],
    "age":[5,13,43,22,3],
    "badroom":[2,4,5,2,1],
    "prices":[100000,50000,40000,45000,500000]
}
df=pd.DataFrame(dic)

X=list(zip(df["areas"],df["age"],df["badroom"]))
Y=df["prices"]

m=len(X)
n=len(X[0])

X_mean = [sum([X[i][j] for i in range(m)]) / m for j in range(n)]
Y_mean=sum(Y)/m

y_dev=[Y[i]-Y_mean for i in range(m)]
x_dev=[[X[i][j]-X_mean[j] for j in range(n) ]for i in range(m)]


# print(x_dev,y_dev)
X_dev_T = [[x_dev[i][j] for i in range(m)] for j in range(n)]
X_dev_T_X_dev = [[sum([X_dev_T[i][k] * x_dev[k][j] for k in range(m)]) for j in range(n)] for i in range(n)]
X_dev_T_Y_dev = [sum([X_dev_T[i][j] * y_dev[j] for j in range(m)]) for i in range(n)]

coefficients = [0] * n
for i in range(n):
    coefficients[i] = X_dev_T_Y_dev[i] / X_dev_T_X_dev[i][i]

intercept = Y_mean - sum([coefficients[j] * X_mean[j] for j in range(n)])

Y_pred = [sum([coefficients[j] * X[i][j] for j in range(n)]) + intercept for i in range(m)]
# print(X_dev_T)
X_new=[[40000,5,3]]

Y_new = [sum([coefficients[j] * X_new[i][j] for j in range(n)]) + intercept for i in range(len(X_new))]

# print(X_dev_T_Y_dev)
print(Y_new)


plt.scatter(df["areas"],Y,color="red")
# plt.scatter(df["age"],Y)
# plt.scatter(df["badroom"],Y,color="green")
plt.plot(df["areas"],Y_pred,color="red")
plt.show()


