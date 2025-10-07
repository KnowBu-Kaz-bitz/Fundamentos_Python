# 📓 Guía de Uso de Jupyter Notebook

Jupyter Notebook es una aplicación web que te permite crear y compartir documentos que contienen código ejecutable, ecuaciones, visualizaciones y texto narrativo.

## 🎯 ¿Qué es Jupyter Notebook?

Jupyter combina:
- **Código:** Python ejecutable
- **Texto enriquecido:** Markdown, LaTeX
- **Visualizaciones:** Gráficos y imágenes
- **Resultados:** Salidas de código

Perfecto para aprendizaje, experimentación y análisis de datos.

## 📦 Instalación

### Opción 1: pip (Recomendada)

```bash
# Crea un entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Instala Jupyter
pip install jupyter notebook ipykernel
```

### Opción 2: Anaconda

Anaconda incluye Jupyter preinstalado:
- Descarga [Anaconda](https://www.anaconda.com/download)
- Instala siguiendo el asistente
- Jupyter ya está disponible

### Verificar instalación:
```bash
jupyter --version
```

## 🚀 Iniciar Jupyter Notebook

### Desde la terminal:

```bash
# Navega a la carpeta del curso
cd ruta/a/Fundamentos_Python

# Inicia Jupyter
jupyter notebook
```

Esto abrirá tu navegador automáticamente en `http://localhost:8888`

### Desde Anaconda Navigator:
1. Abre Anaconda Navigator
2. Haz clic en "Launch" en Jupyter Notebook

## 🖥️ Interfaz de Jupyter

### Dashboard (Página principal)
- **Files:** Navegador de archivos
- **Running:** Notebooks activos
- **Clusters:** (Avanzado) Para computación paralela

### Barra de herramientas
- **New → Python 3:** Crear nuevo notebook
- **Upload:** Subir archivos
- **Checkbox + Botones:** Operaciones en archivos (renombrar, eliminar, etc.)

## 📝 Trabajar con Notebooks

### Crear un nuevo notebook:
1. Clic en "New" → "Python 3"
2. Se abre un notebook vacío
3. Renómbralo haciendo clic en "Untitled"

### Celdas (Cells):

Hay dos tipos principales:

#### 1. Celdas de Código
```python
# Código Python ejecutable
print("¡Hola, Jupyter!")
x = 10
y = 20
print(f"La suma es: {x + y}")
```

#### 2. Celdas Markdown
```markdown
# Título
## Subtítulo

**Negrita** y *cursiva*

- Lista
- De
- Elementos

[Enlaces](https://python.org)
```

### Cambiar tipo de celda:
- En el menú: Cell → Cell Type
- Atajo: Presiona `Esc`, luego:
  - `M` para Markdown
  - `Y` para Código

## ⌨️ Atajos de Teclado Esenciales

### Modo Comando (presiona `Esc`)

| Atajo | Acción |
|-------|--------|
| `A` | Insertar celda arriba |
| `B` | Insertar celda abajo |
| `DD` | Eliminar celda |
| `M` | Cambiar a Markdown |
| `Y` | Cambiar a Código |
| `C` | Copiar celda |
| `V` | Pegar celda |
| `Z` | Deshacer eliminación |

### Modo Edición (presiona `Enter`)

| Atajo | Acción |
|-------|--------|
| `Shift + Enter` | Ejecutar celda y avanzar |
| `Ctrl + Enter` | Ejecutar celda sin avanzar |
| `Alt + Enter` | Ejecutar e insertar celda abajo |
| `Tab` | Autocompletar |
| `Shift + Tab` | Ver documentación |

### Otros atajos útiles

| Atajo | Acción |
|-------|--------|
| `Ctrl + S` | Guardar |
| `H` | Mostrar ayuda de atajos |
| `I, I` | Interrumpir kernel |
| `0, 0` | Reiniciar kernel |

## 🎨 Markdown en Jupyter

### Títulos:
```markdown
# Título 1
## Título 2
### Título 3
```

### Formato de texto:
```markdown
**Negrita**
*Cursiva*
`Código inline`
~~Tachado~~
```

### Listas:
```markdown
- Elemento 1
- Elemento 2
  - Sub-elemento

1. Primero
2. Segundo
3. Tercero
```

### Código:
````markdown
```python
def saludar(nombre):
    return f"Hola, {nombre}!"
```
````

### Ecuaciones (LaTeX):
```markdown
Inline: $E = mc^2$

Bloque:
$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$
```

### Imágenes:
```markdown
![Texto alternativo](ruta/imagen.png)
```

### Enlaces:
```markdown
[Texto del enlace](https://www.ejemplo.com)
```

## 🔧 Funciones Útiles

### Magic Commands

```python
# Medir tiempo de ejecución
%timeit sum(range(1000))

# Ejecutar script externo
%run script.py

# Ver variables en memoria
%whos

# Historial de comandos
%history

# Matplotlib inline (para gráficos)
%matplotlib inline
```

### Ayuda y documentación:

```python
# Ver ayuda
help(print)

# Documentación rápida (shift + tab)
print?

# Código fuente
print??

# Autocompletado (presiona Tab)
import math
math.  # <-- presiona Tab aquí
```

## 💾 Guardar y Exportar

### Guardar:
- **Auto-guardado:** Cada 2 minutos
- **Manual:** `Ctrl + S` o File → Save

### Exportar:
File → Download as:
- **Python (.py):** Solo código
- **HTML (.html):** Vista estática
- **Markdown (.md):** Texto plano
- **PDF:** Requiere LaTeX instalado

### Compartir:
1. **GitHub:** Previsualización automática
2. **nbviewer:** [nbviewer.org](https://nbviewer.org)
3. **Google Colab:** Ejecutable en la nube
4. **Binder:** Interactivo en línea

## 🔄 Gestión del Kernel

El **kernel** es el proceso que ejecuta tu código.

### Operaciones del kernel:
- **Interrupt:** Detiene ejecución actual
- **Restart:** Reinicia y limpia variables
- **Restart & Clear Output:** + Limpia salidas
- **Restart & Run All:** + Ejecuta todo

```python
# Verificar estado del kernel
import sys
print(f"Python: {sys.version}")
print(f"Ejecutable: {sys.executable}")
```

## 🎯 Buenas Prácticas

### 1. Organización
```markdown
# 1. Título del Notebook
## 1.1 Importaciones
## 1.2 Configuración
## 1.3 Carga de datos
## 1.4 Análisis
## 1.5 Conclusiones
```

### 2. Documentación
- Usa celdas markdown para explicaciones
- Comenta código complejo
- Incluye ejemplos de uso

### 3. Ejecución
- Ejecuta las celdas en orden
- Reinicia el kernel periódicamente
- Verifica que todo funciona desde cero

### 4. Código limpio
```python
# ❌ Evitar
x=1;y=2;z=x+y;print(z)

# ✅ Preferir
x = 1
y = 2
z = x + y
print(z)
```

## 🐛 Solución de Problemas

### Jupyter no inicia:
```bash
# Verifica la instalación
pip show jupyter

# Reinstala si es necesario
pip install --upgrade jupyter
```

### Kernel no se conecta:
1. Kernel → Restart
2. Cierra y reabre el notebook
3. Reinstala ipykernel:
   ```bash
   pip install --upgrade ipykernel
   ```

### Error "ModuleNotFoundError":
```python
# Instala el módulo desde una celda
!pip install nombre_modulo
```

### Puerto ya en uso:
```bash
# Usa un puerto diferente
jupyter notebook --port 8889
```

## 🔗 Extensiones Útiles (Opcional)

```bash
# Instalar extensiones
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Habilitar configurador
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```

Extensiones recomendadas:
- **Table of Contents:** Índice automático
- **ExecuteTime:** Tiempo de ejecución
- **Code folding:** Colapsar código
- **Variable inspector:** Ver variables

## 📚 Recursos Adicionales

- [Documentación oficial](https://jupyter-notebook.readthedocs.io/)
- [Jupyter Lab](https://jupyterlab.readthedocs.io/) (próxima generación)
- [Galería de notebooks](https://github.com/jupyter/jupyter/wiki)
- [Atajos completos](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/)

## 🎓 Próximos Pasos

Ahora que conoces Jupyter:
1. Abre los notebooks de la [Semana 1](../Semana_1_Introduccion/)
2. Practica ejecutando las celdas
3. Experimenta modificando el código
4. Crea tus propios notebooks

---

**¡Feliz aprendizaje con Jupyter! 🚀**
