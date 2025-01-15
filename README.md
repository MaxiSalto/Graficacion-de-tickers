📊 Yahoo Finance Data Dashboard
🔥 Automatiza la descarga, estructuración y visualización de datos financieros con Python, Excel y Dash.

Este proyecto permite descargar información histórica de tickers de inversión desde Yahoo Finance, estructurar la base de datos automáticamente con una macro de Excel, y visualizar los datos con Plotly Dash en un servidor local.

⚙️ Funcionalidad del Proyecto
1️⃣ Descarga los datos históricos de Yahoo Finance utilizando yfinance.
2️⃣ Transforma y organiza los datos con una macro de Excel (VBA).
3️⃣ Visualiza los gráficos interactivos con Plotly y Dash en tu navegador.

🛠️ Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes librerías en tu entorno de Python:

bash
Copiar código
pip install yfinance pandas plotly dash
🔧 Herramientas adicionales necesarias:

Excel con soporte para macros (VBA).
Python 3.9+.
📂 Configuración Inicial
1️⃣ Descarga el Excel que usarás en este proyecto.
2️⃣ Inserta la macro de VBA que encontrarás en este repositorio (archivo VBA.bas).

La macro automatiza la limpieza y estructuración de los datos descargados.
3️⃣ Guarda el archivo Excel con la macro habilitada (.xlsm).
🚀 Cómo Usarlo
🧩 Paso 1: Ejecutar original_yfinance.py
Este script descargará automáticamente los datos históricos de los tickers más relevantes que ya están configurados en el archivo.

📦 Salida: Un archivo Excel con los datos descargados.

📊 Paso 2: Aplicar la Macro de Excel
Abre el Excel generado y ejecuta la macro que configuraste previamente.

🔄 Esto reorganizará los datos para que estén listos para graficar.

📈 Paso 3: Ejecutar Velas_v2.py
Este script generará un gráfico interactivo utilizando Plotly Dash y abrirá un servidor local para que puedas visualizarlo en tu navegador.

💻 Accede al dashboard local:
Presiona Ctrl + Click en la dirección que aparece en la terminal (por ejemplo: http://127.0.0.1:8050/).

🎨 Ejemplo del Gráfico Interactivo
![Gráfico Interactivo](Ejemplo Grafico.png)

🧑‍💻 Contribución y Feedback
Este proyecto está abierto a mejoras.
¡Cualquier contribución es bienvenida! 🙌

📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

