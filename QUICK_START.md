# 🚀 Quick Start - Iniciar el Repositorio

Sigue estos pasos para publicar tu curso en GitHub.

## 📋 Paso 1: Verificar Prerrequisitos

```powershell
# Verifica que Git está instalado
git --version

# Si no está instalado, descarga de: https://git-scm.com/download/win
```

## 🎯 Paso 2: Personalizar el README Principal

Edita `README.md` y actualiza:
- [ ] Tu nombre como instructor
- [ ] Tu email de contacto
- [ ] Tu perfil de LinkedIn (opcional)
- [ ] El enlace del repositorio (después de crearlo)

## 🔧 Paso 3: Inicializar Git

```powershell
# Abre PowerShell y navega a la carpeta
cd "c:\Users\Cesar\OneDrive - KnowBu\Learning - IA\Learning - Bootcamps\Fundamentos_Python"

# Inicializa Git
git init

# Configura tu identidad (una sola vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# Añade todos los archivos
git add .

# Verifica qué se añadirá (debe excluir _privado/)
git status

# Crea el primer commit
git commit -m "Initial commit: Curso Fundamentos de Python"
```

## 🌐 Paso 4: Crear Repositorio en GitHub

1. Ve a https://github.com y inicia sesión
2. Click en **"+"** (arriba derecha) → **"New repository"**
3. Configura:
   - **Repository name:** `fundamentos-python`
   - **Description:** "Curso completo de Fundamentos de Python"
   - **Public** (para compartir abiertamente)
   - **NO** marques "Initialize with README"
4. Click **"Create repository"**

## 📤 Paso 5: Conectar y Subir

Copia los comandos que GitHub te muestra, o usa estos:

```powershell
# Conecta tu repo local con GitHub
git remote add origin https://github.com/TU-USUARIO/fundamentos-python.git

# Renombra la rama a 'main'
git branch -M main

# Sube todo a GitHub
git push -u origin main
```

## ✅ Paso 6: Verificar

1. Recarga la página de tu repositorio en GitHub
2. Deberías ver toda la estructura del curso
3. Los notebooks deben tener vista previa

## 🎓 Paso 7: Compartir con Participantes

Tu repositorio estará en:
```
https://github.com/TU-USUARIO/fundamentos-python
```

**Instrucciones para participantes:**

```markdown
Para obtener el material:

1. Opción A - Descargar ZIP:
   - Ve a https://github.com/TU-USUARIO/fundamentos-python
   - Click "Code" → "Download ZIP"

2. Opción B - Clonar (recomendado):
   ```bash
   git clone https://github.com/TU-USUARIO/fundamentos-python.git
   cd fundamentos-python
   pip install -r requirements.txt
   jupyter notebook
   ```
```

## 🔄 Actualizar Material

Cuando hagas cambios:

```powershell
# Añade cambios
git add .

# Commit con mensaje descriptivo
git commit -m "Añade ejercicios de la Semana 2"

# Sube a GitHub
git push
```

Los participantes actualizan con:
```bash
git pull
```

## 🆘 Solución de Problemas

### Error: "git no se reconoce"
Instala Git desde: https://git-scm.com/download/win

### Error: "Permission denied"
Configura SSH o usa HTTPS con token personal:
https://docs.github.com/en/authentication

### Archivos privados se están subiendo
Verifica `.gitignore` y ejecuta:
```powershell
git rm -r --cached _privado/
git commit -m "Remove private files"
git push
```

## 📚 Recursos

- [GitHub Docs](https://docs.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Guía Completa de Compartir](./guia_compartir.md)

---

**¡Listo para compartir tu curso! 🎉**
