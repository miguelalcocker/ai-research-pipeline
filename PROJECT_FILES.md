# Archivos del Proyecto AI Research Data Extraction

**Estado:** ✅ Corregido y Funcional  
**Fecha:** 2025-11-17

---

## 📁 Estructura de Archivos

### 🟢 Scripts Principales

| Archivo | Propósito | Uso |
|---------|-----------|-----|
| `extract_ai_research_data.py` | Script principal de extracción | `python extract_ai_research_data.py` |
| `config.yaml` | Configuración del pipeline | Editar parámetros |
| `requirements.txt` | Dependencias Python | Auto-instaladas |

### 🔵 Scripts de Testing

| Archivo | Papers | Tiempo | Comando |
|---------|--------|--------|---------|
| `verify_fix.py` | 25 | ~1 min | `python verify_fix.py` |
| `quick_test.py` | 500 | 5-10 min | `python quick_test.py` |
| `minimal_test.py` | 100 | 2-3 min | `python minimal_test.py` |

### 📘 Documentación

| Archivo | Contenido |
|---------|-----------|
| `QUICK_START.md` | ⭐ **Inicio rápido** - Empieza aquí |
| `FIXES_APPLIED.md` | Detalles técnicos de las correcciones |
| `START_HERE.md` | Guía de inicio del proyecto original |
| `INSTALLATION.md` | Instalación y troubleshooting |
| `PROJECT_SUMMARY.md` | Overview completo del proyecto |
| `PROJECT_FILES.md` | Este archivo |

### 📊 Outputs (Generados al Ejecutar)

```
output/
├── data/
│   ├── fact_publications.csv      (Tabla de hechos principal)
│   ├── dim_authors.csv            (Dimensión de autores)
│   ├── dim_institutions.csv       (Dimensión de instituciones)
│   ├── dim_venues.csv             (Dimensión de venues)
│   └── dim_time.csv               (Dimensión temporal)
├── logs/
│   ├── extraction_log.txt         (Log de ejecución)
│   └── data_quality_report.html   (Reporte de calidad)
└── README.md                      (Documentación del dataset)
```

---

## 🎯 Qué Leer Según Tu Objetivo

### Solo quiero ejecutarlo YA
→ **QUICK_START.md**

### Quiero entender qué se corrigió
→ **FIXES_APPLIED.md**

### Tengo problemas de instalación
→ **INSTALLATION.md**

### Quiero ver todas las features del proyecto
→ **PROJECT_SUMMARY.md**

### Quiero customizar el script
→ Editar **config.yaml** + leer comentarios en **extract_ai_research_data.py**

---

## 🚀 Flujo de Trabajo Recomendado

```
1. Lee QUICK_START.md (2 minutos)
   ↓
2. Ejecuta verify_fix.py (1 minuto)
   ↓
3. Revisa output/logs/data_quality_report.html
   ↓
4. Si todo bien → Ejecuta quick_test.py (5-10 min)
   ↓
5. Si todo bien → Ejecuta extract_ai_research_data.py (15-30 min)
   ↓
6. Importa CSVs a Power BI
   ↓
7. ¡Crea dashboards!
```

---

## 📝 Cambios Realizados

### Archivos Modificados
- ✏️ `extract_ai_research_data.py` - 3 correcciones críticas aplicadas

### Archivos Nuevos Creados
- ✨ `verify_fix.py` - Verificación rápida
- ✨ `minimal_test.py` - Test mínimo
- ✨ `QUICK_START.md` - Guía de inicio rápido
- ✨ `FIXES_APPLIED.md` - Documentación de correcciones
- ✨ `PROJECT_FILES.md` - Este archivo
- ✨ `.gitignore` - Reglas de git

---

## 🔧 Configuración Personalizable

### config.yaml - Secciones Principales

```yaml
data_collection:
  min_papers: 5000      # Mínimo de papers a extraer
  max_papers: 15000     # Máximo de papers
  start_year: 2019      # Año inicial
  end_year: 2024        # Año final

core_concepts:          # Conceptos para buscar
  - "artificial intelligence"
  - "machine learning"
  # ... agregar más

subfield_keywords:      # Keywords para clasificación
  "Graph Neural Networks":
    - "graph neural network"
    # ... más keywords

quality:
  min_abstract_length: 100  # Tamaño mínimo de abstract
  breakthrough_paper_percentile: 95  # Top 5%
```

---

## 💾 Tamaños Aproximados

### Scripts
- `extract_ai_research_data.py`: ~52 KB (1,000+ líneas)
- `config.yaml`: ~3 KB
- Otros scripts: ~1-2 KB cada uno

### Outputs (después de extracción completa)
- Total dataset: ~50-100 MB
- `fact_publications.csv`: ~30-60 MB
- `dim_time.csv`: ~50-60 KB
- Otros: ~1-5 MB cada uno

---

## 🔍 Archivos Ignorados (.gitignore)

```
__pycache__/
*.pyc
output/
*.csv
*.json
*.log
*.txt
```

---

## 🛠️ Mantenimiento

### Actualizar Dataset
```bash
# Borrar outputs viejos
rm -rf output/

# Ejecutar nueva extracción
python extract_ai_research_data.py
```

### Cambiar Enfoque de Investigación
```bash
# Editar config.yaml
vim config.yaml

# Modificar core_concepts y subfield_keywords
# Ejecutar de nuevo
python extract_ai_research_data.py
```

---

## 📊 Estadísticas del Proyecto

- **Líneas de código:** ~1,400
- **Funciones:** ~20
- **Clases:** 4
- **Archivos Python:** 4
- **Archivos de documentación:** 6
- **Tablas generadas:** 5
- **Métricas calculadas:** 10+
- **Subfields clasificados:** 10

---

## ✅ Checklist de Verificación

Antes de empezar tu proyecto, verifica:

- [ ] Python 3.8+ instalado
- [ ] Conexión a internet estable
- [ ] ~500MB espacio en disco disponible
- [ ] Leído QUICK_START.md
- [ ] Ejecutado verify_fix.py exitosamente
- [ ] Power BI Desktop instalado (para visualización)

---

**Última actualización:** 2025-11-17  
**Versión:** 1.0 (Corregida)  
**Estado:** ✅ Verificado y Funcional
