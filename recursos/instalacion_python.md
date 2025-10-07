# 🐍 Guía de Instalación de Python

Esta guía te ayudará a instalar Python en tu sistema operativo.

## 📋 Requisitos Previos

- **Sistema Operativo:** Windows 10+, macOS 10.13+, o Linux
- **Espacio en disco:** Al menos 500 MB libres
- **Conexión a Internet:** Para descargar Python y paquetes

## 🪟 Windows

### Opción 1: Instalador Oficial (Recomendada)

1. **Descarga Python:**
   - Ve a [python.org/downloads](https://www.python.org/downloads/)
   - Descarga la última versión (Python 3.11+ recomendado)

2. **Ejecuta el instalador:**
   - ⚠️ **IMPORTANTE:** Marca la casilla "Add Python to PATH"
   - Selecciona "Install Now" para instalación estándar
   - O "Customize installation" para opciones avanzadas

3. **Verifica la instalación:**
   ```powershell
   python --version
   ```
   Deberías ver algo como: `Python 3.11.x`

### Opción 2: Microsoft Store

1. Abre Microsoft Store
2. Busca "Python 3.11" (o la versión más reciente)
3. Haz clic en "Obtener" o "Instalar"
4. Verifica con `python --version` en PowerShell

### Problemas Comunes en Windows

**Python no se reconoce:**
```powershell
# Añade Python al PATH manualmente
# Busca: "Variables de entorno" en el menú de Windows
# Añade: C:\Users\TuUsuario\AppData\Local\Programs\Python\Python311
```

## 🍎 macOS

### Opción 1: Instalador Oficial

1. **Descarga Python:**
   - Ve a [python.org/downloads](https://www.python.org/downloads/)
   - Descarga el instalador para macOS

2. **Ejecuta el instalador (.pkg)**
   - Sigue las instrucciones del asistente

3. **Verifica la instalación:**
   ```bash
   python3 --version
   ```

### Opción 2: Homebrew (Recomendada para desarrolladores)

1. **Instala Homebrew** (si no lo tienes):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Instala Python:**
   ```bash
   brew install python
   ```

3. **Verifica:**
   ```bash
   python3 --version
   ```

### Nota para macOS
macOS incluye Python 2.7 por defecto. **Siempre usa `python3`** para ejecutar Python 3.x.

## 🐧 Linux

### Ubuntu/Debian

Python 3 generalmente viene preinstalado. Para instalar la última versión:

```bash
# Actualiza los paquetes
sudo apt update

# Instala Python 3
sudo apt install python3 python3-pip python3-venv

# Verifica
python3 --version
```

### Fedora/CentOS/RHEL

```bash
# Fedora
sudo dnf install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip

# Verifica
python3 --version
```

### Arch Linux

```bash
sudo pacman -S python python-pip

python --version
```

## 📦 Instalación de pip

**pip** es el gestor de paquetes de Python. Normalmente se instala automáticamente.

### Verificar pip:
```bash
# Windows
pip --version

# macOS/Linux
pip3 --version
```

### Instalar pip si falta:
```bash
# Windows/macOS/Linux
python -m ensurepip --upgrade

# O descarga get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

## 🔧 Configuración del Entorno Virtual

Los entornos virtuales aíslan las dependencias de cada proyecto.

### Crear entorno virtual:

```bash
# Windows
python -m venv nombre_entorno
nombre_entorno\Scripts\activate

# macOS/Linux
python3 -m venv nombre_entorno
source nombre_entorno/bin/activate
```

### Desactivar entorno virtual:
```bash
deactivate
```

## 🎯 Instalación de Jupyter

Para seguir el curso, necesitas Jupyter Notebook:

```bash
# Activar entorno virtual primero (recomendado)
pip install jupyter notebook ipykernel

# Iniciar Jupyter
jupyter notebook
```

## ✅ Verificación Completa

Ejecuta este script para verificar tu instalación:

```python
# guardar como test_install.py
import sys
import platform

print(f"Python {sys.version}")
print(f"Ejecutable: {sys.executable}")
print(f"Sistema: {platform.system()} {platform.release()}")

try:
    import pip
    print(f"pip: {pip.__version__}")
except ImportError:
    print("pip: No instalado")

print("\n✅ Python está correctamente instalado!")
```

Ejecutar:
```bash
python test_install.py
```

## 🆘 Solución de Problemas

### "Python no se reconoce como comando"
- **Solución:** Añade Python al PATH de tu sistema
- Windows: Variables de entorno → PATH → Añadir ruta de Python
- macOS/Linux: Añade a `~/.bashrc` o `~/.zshrc`:
  ```bash
  export PATH="/usr/local/bin/python3:$PATH"
  ```

### Error de permisos al instalar paquetes
```bash
# Instala solo para tu usuario
pip install --user nombre_paquete

# O usa entorno virtual (recomendado)
```

### Versión incorrecta de Python
```bash
# Especifica la versión explícitamente
python3 archivo.py

# O crea un alias
alias python=python3
```

## 📚 Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [Tutorial de pip](https://pip.pypa.io/en/stable/getting-started/)
- [Guía de entornos virtuales](https://docs.python.org/es/3/tutorial/venv.html)

## 🎓 Próximo Paso

Una vez instalado Python, revisa la [Guía de Jupyter](./guia_jupyter.md) para comenzar con los notebooks del curso.

---

**¿Problemas?** Contacta al instructor o abre un issue en el repositorio.
