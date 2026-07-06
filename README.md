# market-analysis
proyecto colaborativo de análisis de datos usando Python 

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-yellow)

## Descripción

**Market Analysis** es un proyecto desarrollado en Python cuyo objetivo es analizar un conjunto de datos de mercado mediante técnicas de limpieza, procesamiento, análisis estadístico y visualización de datos.

El proyecto está organizado siguiendo una estructura modular que facilita el mantenimiento del código y el trabajo colaborativo utilizando Git y GitHub.

---

# Objetivos

- Limpiar y preparar el conjunto de datos.
- Analizar la información mediante estadísticas descriptivas.
- Generar gráficos para interpretar los resultados.
- Mantener una estructura organizada y escalable.
- Aplicar control de versiones con Git.

---

# Estructura del proyecto

```text
market-analysis/
│
├── data/
│   └── market.csv
│
├── notebooks/
│   └── analisis.ipynb
│
├── src/
│   ├── limpieza.py
│   ├── analisis.py
│   ├── graficos.py
│   └── utils.py
│
├── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Descripción de carpetas

## data/

Contiene el conjunto de datos utilizado durante el análisis.

## notebooks/

Incluye notebooks de Jupyter para realizar análisis exploratorios.

## src/

Contiene el código fuente del proyecto.

- **limpieza.py:** limpieza y preparación de datos.
- **analisis.py:** procesamiento y análisis estadístico.
- **graficos.py:** generación de gráficos.
- **utils.py:** funciones auxiliares reutilizables.

## images/

Carpeta destinada a almacenar los gráficos generados por el proyecto.

---

# Tecnologías utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/belencampos14/market-analysis.git
```

Entrar al proyecto:

```bash
cd market-analysis
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Ejecución

Ejecutar cada módulo desde la carpeta principal:

```bash
python src/limpieza.py
```

```bash
python src/analisis.py
```

```bash
python src/graficos.py
```

También puede abrirse el notebook:

```
notebooks/analisis.ipynb
```

---

# Dataset

El proyecto utiliza el archivo:

```
data/market.csv
```

como fuente principal para el análisis de datos.

---

# Flujo de trabajo

1. Cargar el dataset.
2. Limpiar la información.
3. Analizar los datos.
4. Generar gráficos.
5. Interpretar los resultados.

---

# Trabajo colaborativo

El proyecto fue desarrollado utilizando Git y GitHub mediante ramas independientes para facilitar el trabajo en equipo y el control de versiones.

---

# Integrantes

| Integrante | Responsabilidad |
|------------|-----------------|
| Belen Campos | Limpieza del dataset |
| Hitler Campoverde | Análisis estadístico |
| Edgar Crespo | Generación de gráficos |
| Adrian Lara | Documentación, README y configuración del proyecto |

---

# Conclusiones

- Una estructura organizada facilita el mantenimiento del proyecto.
- La limpieza de datos es fundamental antes de cualquier análisis.
- Los gráficos permiten comprender mejor la información obtenida.
- Git y GitHub mejoran el trabajo colaborativo y el seguimiento de cambios.

---

# Licencia

Proyecto desarrollado con fines académicos.
