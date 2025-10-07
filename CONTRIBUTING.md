# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al curso de Fundamentos de Python! Este documento te guiará sobre cómo puedes ayudar a mejorar el material.

## 📋 Formas de Contribuir

### 1. Reportar Errores
Si encuentras un error en el código, documentación o notebooks:

1. Verifica que el error no haya sido reportado antes en [Issues](../../issues)
2. Crea un nuevo issue con:
   - **Título descriptivo**
   - **Descripción del error**
   - **Pasos para reproducirlo**
   - **Comportamiento esperado vs. actual**
   - **Capturas de pantalla** (si aplica)

### 2. Sugerir Mejoras
¿Tienes ideas para mejorar el contenido?

1. Abre un issue con el tag `enhancement`
2. Describe claramente tu propuesta
3. Explica por qué sería beneficiosa

### 3. Contribuir con Código

#### Proceso:
1. **Fork** el repositorio
2. **Crea una rama** desde `main`:
   ```bash
   git checkout -b feature/nombre-descriptivo
   ```
3. **Realiza tus cambios** siguiendo las guías de estilo
4. **Commit** con mensajes claros:
   ```bash
   git commit -m "Añade ejercicio de listas en Semana 2"
   ```
5. **Push** a tu fork:
   ```bash
   git push origin feature/nombre-descriptivo
   ```
6. **Abre un Pull Request** con descripción detallada

## 📝 Guías de Estilo

### Notebooks
- Usa celdas markdown para explicaciones claras
- Incluye ejemplos ejecutables en cada concepto
- Añade comentarios en el código
- Sigue PEP 8 para el código Python

### Documentación
- Usa Markdown estándar
- Incluye ejemplos cuando sea posible
- Mantén un tono didáctico y amigable
- Revisa la ortografía y gramática

### Código Python
```python
# Sigue PEP 8
# Usa nombres descriptivos
# Incluye docstrings

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números a promediar
        
    Returns:
        float: El promedio de los números
    """
    return sum(numeros) / len(numeros)
```

## ✅ Checklist antes de enviar PR

- [ ] El código funciona correctamente
- [ ] Se añadieron tests si aplica
- [ ] La documentación está actualizada
- [ ] Los notebooks se ejecutan sin errores
- [ ] Se siguieron las guías de estilo
- [ ] Los commits tienen mensajes descriptivos

## 🔍 Revisión de Pull Requests

Todos los PRs serán revisados. Podemos solicitar cambios para:
- Mantener la calidad del contenido
- Asegurar consistencia
- Mejorar la claridad didáctica

## 📧 ¿Preguntas?

Si tienes dudas sobre cómo contribuir:
- Abre un issue con el tag `question`
- Contacta al instructor

## 🙏 Código de Conducta

- Sé respetuoso y profesional
- Acepta críticas constructivas
- Enfócate en lo mejor para los estudiantes
- Ayuda a crear un ambiente de aprendizaje positivo

---

¡Gracias por hacer este curso mejor para todos! 🎉
