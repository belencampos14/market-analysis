import pandas as pd 
import matplotlib.pyplot as plt
# =========================
# CARGA DEL DATASET
# =========================
df = pd.read_csv("data/market.csv")
# Verificación básica
print(df.head())
print(df.columns)
# ======================
# GRÁFICO 1: Ventas por categoría
# ======================
plt.figure(figsize=(10,5))
df.groupby("Product line")["Sales"].sum().plot(kind="bar")
plt.title("Ventas por categoría")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/grafico1.png")
plt.close()
# ======================
# GRÁFICO 2: Métodos de pago
# ======================
plt.figure()
df["Payment"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Métodos de pago")
plt.ylabel("")
plt.savefig("images/grafico2.png")
plt.close()
# ======================
# GRÁFICO 3: Histograma precios
# ======================
plt.figure()
df["Unit price"].plot(kind="hist", bins=20)
plt.title("Distribución de precios")
plt.savefig("images/grafico3.png")
plt.close()

# ======================
# GRÁFICO 4: Precio vs cantidad
# ======================
plt.figure(figsize=(8,5))

plt.scatter(df["Quantity"], df["Sales"], alpha=0.6)

plt.title("Relación entre cantidad vendida y ventas")
plt.xlabel("Cantidad de productos")
plt.ylabel("Total de ventas")

plt.grid(True)

plt.savefig("images/grafico4.png")
plt.show()
plt.close()

print("TODOS LOS GRÁFICOS FUERON GENERADOS CORRECTAMENTE")

