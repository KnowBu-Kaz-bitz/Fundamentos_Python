# 🚀 Guía para Compartir el Curso

Esta guía te explica cómo compartir el material del curso con los participantes de manera profesional y eficiente.

## 📋 Antes de Compartir

### ✅ Checklist de Preparación

- [ ] Todos los notebooks están completos y funcionan
- [ ] Las presentaciones están convertidas a PDF
- [ ] Los archivos privados están en `_privado/`
- [ ] El `.gitignore` está configurado correctamente
- [ ] El `README.md` principal está actualizado con tu información
- [ ] Los `requirements.txt` incluyen todas las dependencias

### 🔒 Verificar Material Privado

El `.gitignore` ya está configurado para excluir:
- Carpeta `_privado/` completa
- Archivos `.pptx` originales
- Carpetas antiguas de organización

**Verifica antes de publicar:**
```powershell
# Verifica qué se incluirá en Git
git status
git ls-files
```

## 🎯 Opción 1: GitHub (RECOMENDADA)

### Ventajas
✅ Control de versiones  
✅ Colaboración fácil  
✅ Vista previa de notebooks  
✅ Gratis para repositorios públicos  
✅ Profesional y estándar en la industria  

### Pasos para Publicar

#### 1. Inicializar Repositorio Git

```powershell
# Navega a la carpeta del curso
cd "c:\Users\Cesar\OneDrive - KnowBu\Learning - IA\Learning - Bootcamps\Fundamentos_Python"

# Inicializa Git
git init

# Añade todos los archivos (respetando .gitignore)
git add .

# Verifica qué se añadirá
git status

# Primer commit
git commit -m "Initial commit: Curso Fundamentos de Python"
```

#### 2. Crear Repositorio en GitHub

1. Ve a [github.com](https://github.com) e inicia sesión
2. Click en "+" → "New repository"
3. Configura:
   - **Nombre:** `fundamentos-python` (o el que prefieras)
   - **Descripción:** "Curso completo de Fundamentos de Python con notebooks interactivos"
   - **Visibilidad:** Public (para compartir) o Private (solo invitados)
   - **NO** inicialices con README (ya lo tienes)

4. Click en "Create repository"

#### 3. Conectar y Subir

```powershell
# Conecta tu repositorio local con GitHub
git remote add origin https://github.com/TU-USUARIO/fundamentos-python.git

# Sube el código
git branch -M main
git push -u origin main
```

#### 4. Compartir con Participantes

**Enlace del repositorio:**
```
https://github.com/TU-USUARIO/fundamentos-python
```

**Instrucciones para participantes:**

```markdown
## 📥 Cómo Obtener el Material

### Opción A: Descargar ZIP (Fácil)
1. Ve a https://github.com/TU-USUARIO/fundamentos-python
2. Click en "Code" → "Download ZIP"
3. Extrae el archivo
4. Sigue las instrucciones del README.md

### Opción B: Clonar con Git (Recomendado)
```bash
git clone https://github.com/TU-USUARIO/fundamentos-python.git
cd fundamentos-python
pip install -r requirements.txt
jupyter notebook
```

### Actualizar el Material
Si hay actualizaciones durante el curso:
```bash
cd fundamentos-python
git pull
```
```

### 5. Configurar GitHub Pages (Opcional)

Para documentación web estática:

1. En tu repositorio GitHub: Settings → Pages
2. Source: Deploy from a branch → main → /docs
3. Crea carpeta `docs/` con HTML generado

## 🌐 Opción 2: Google Drive

### Ventajas
✅ Fácil para usuarios no técnicos  
✅ Ideal para presentaciones y PDFs  
✅ 15GB gratis  

### Pasos

#### 1. Preparar Carpeta

```powershell
# Crea una copia limpia sin archivos privados
# Opción: Usa Robocopy para copiar selectivamente
```

#### 2. Subir a Google Drive

1. Abre [drive.google.com](https://drive.google.com)
2. Crea carpeta "Fundamentos de Python"
3. Sube todo el contenido (excepto `_privado/`)
4. Organiza en subcarpetas si es necesario

#### 3. Compartir

**Opción A: Enlace público**
1. Click derecho en la carpeta → "Compartir"
2. Click en "Cambiar" junto a "Restringido"
3. Selecciona "Cualquiera con el enlace"
4. Permiso: "Visualizador"
5. Copia el enlace

**Opción B: Solo participantes específicos**
1. Click derecho → "Compartir"
2. Añade emails de participantes
3. Selecciona permiso: "Visualizador" o "Comentador"

**Enlace a compartir:**
```
https://drive.google.com/drive/folders/ID-DE-TU-CARPETA
```

## 🔗 Opción 3: GitHub + Google Drive (HÍBRIDO)

### Estrategia Recomendada

**GitHub para:**
- ✅ Notebooks (.ipynb)
- ✅ Código Python (.py)
- ✅ Archivos de datos pequeños (<25MB)
- ✅ Markdown y documentación

**Google Drive para:**
- ✅ Presentaciones PPTX originales (si quieres compartirlas)
- ✅ Videos del curso
- ✅ Archivos grandes (datasets >25MB)
- ✅ PDFs de las presentaciones

### Implementación

1. **Publica en GitHub** (ver Opción 1)
2. **Crea carpeta en Google Drive** con material complementario
3. **Añade enlaces en el README.md:**

```markdown
## 📊 Material Complementario

El código y notebooks están en este repositorio. Material adicional:

- [📁 Presentaciones (Google Drive)](ENLACE-A-TU-DRIVE)
- [🎥 Videos del Curso](ENLACE-A-VIDEOS)
- [📊 Datasets Grandes](ENLACE-A-DATOS)
```

## 📱 Opción 4: Google Colab

### Para Notebooks Interactivos en la Nube

#### Ventajas
✅ No requiere instalación local  
✅ Ejecutable directamente en el navegador  
✅ GPU gratis (para ejercicios avanzados)  

#### Configurar

1. **Sube notebooks a Google Drive** en carpeta específica
2. **Comparte cada notebook con enlace directo:**
   - Abre el notebook en Colab
   - File → "Copy to Drive" (si es necesario)
   - Share → Copia enlace

3. **Botón "Open in Colab" en GitHub:**

Añade al principio de cada notebook:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TU-USUARIO/fundamentos-python/blob/main/Semana_1_Introduccion/notebooks/S1_Contenido_N1.ipynb)
```

## 🎓 Opción 5: Plataformas de Cursos

### Plataformas Gratuitas

**GitHub + nbviewer:**
- Enlace: `https://nbviewer.org/github/TU-USUARIO/fundamentos-python/tree/main/`
- Vista previa renderizada de notebooks

**Binder (Ejecutable):**
1. Ve a [mybinder.org](https://mybinder.org)
2. Introduce URL de tu repositorio
3. Genera enlace ejecutable
4. Añade badge a tu README:
```markdown
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TU-USUARIO/fundamentos-python/main)
```

**Kaggle:**
- Sube datasets y notebooks
- Comparte URL pública

## 📧 Comunicación con Participantes

### Email de Bienvenida (Template)

```
Asunto: 🐍 Bienvenido al Curso de Fundamentos de Python

Hola [Nombre],

¡Bienvenido al Bootcamp de Fundamentos de Python!

📚 ACCESO AL MATERIAL:
GitHub: https://github.com/TU-USUARIO/fundamentos-python
Google Drive: [ENLACE SI APLICA]

🚀 PRIMEROS PASOS:
1. Instala Python: Ver guía en /recursos/instalacion_python.md
2. Clona/descarga el repositorio
3. Instala dependencias: pip install -r requirements.txt
4. Inicia Jupyter: jupyter notebook
5. Comienza con Semana 1

📅 CALENDARIO:
- Semana 1: [Fechas] - Introducción
- Semana 2: [Fechas] - Estructuras de Control
- Semana 3: [Fechas] - Funciones
- Semana 4: [Fechas] - Proyecto Final

💬 SOPORTE:
- Email: [tu-email]
- Discord/Slack: [enlace si aplica]

¡Nos vemos en clase! 🎉

[Tu Nombre]
Instructor - Fundamentos de Python
```

## 🔄 Actualizaciones Durante el Curso

### Con GitHub

```powershell
# Realiza cambios en el material
# ...

# Añade y confirma cambios
git add .
git commit -m "Añade ejercicios adicionales Semana 2"
git push

# Los participantes actualizan con:
git pull
```

### Con Google Drive

- Los cambios se reflejan automáticamente
- Notifica por email si son cambios importantes

## 📊 Analíticas y Seguimiento

### GitHub
- Revisa "Insights" para ver:
  - Número de clones
  - Visitantes
  - Forks y stars

### Google Drive
- Actividad de la carpeta
- Quién accedió y cuándo

## 🎯 Recomendación Final

**Para un curso profesional:**

```
GitHub (Código y notebooks)
    ↓
Google Drive (Presentaciones y videos)
    ↓
Google Colab (Notebooks interactivos opcionales)
    ↓
Email/Slack (Comunicación)
```

## ✅ Checklist Final Antes de Compartir

- [ ] README.md actualizado con tu información
- [ ] .gitignore configurado (material privado excluido)
- [ ] Todos los notebooks probados y funcionando
- [ ] requirements.txt completo
- [ ] Enlaces en README apuntando correctamente
- [ ] Material privado en `_privado/` (no se comparte)
- [ ] Presentaciones convertidas a PDF (opcional)
- [ ] Repositorio GitHub público o Drive compartido
- [ ] Email de bienvenida preparado
- [ ] Calendario del curso definido

---

## 🆘 ¿Necesitas Ayuda?

- **Git/GitHub:** [Guía oficial de GitHub](https://guides.github.com/)
- **Google Drive:** [Centro de ayuda de Drive](https://support.google.com/drive)
- **Google Colab:** [Preguntas frecuentes](https://research.google.com/colaboratory/faq.html)

---

**¡Listo para compartir tu curso! 🚀**
```

## 📝 Notas Importantes

1. **Licencia:** Ya tienes MIT License - permite uso libre con atribución
2. **Privacidad:** Nunca subas información personal o sensible
3. **Tamaño:** GitHub tiene límite de 100MB por archivo (usa Git LFS si necesario)
4. **Costos:** GitHub y Google Drive (15GB) son gratis

¡Éxito con tu curso! 🎓
