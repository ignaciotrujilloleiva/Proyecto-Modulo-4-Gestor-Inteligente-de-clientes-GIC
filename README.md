# 🏢 Gestor Inteligente de Clientes (GIC) - SolutionTech

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Estado-Finalizado-green?style=for-the-badge)
![POO](https://img.shields.io/badge/Paradigma-POO-orange?style=for-the-badge)

## 📄 Descripción del Proyecto

Este sistema ha sido desarrollado para la empresa **SolutionTech** con el objetivo de modernizar su gestión de clientes. Es una aplicación de consola construida en **Python 3** bajo el paradigma de **Programación Orientada a Objetos (POO)**.

El GIC permite administrar una cartera de clientes de manera eficiente, asegurando la integridad de los datos mediante validaciones avanzadas, manejo de errores robusto y persistencia de datos en formatos **CSV** y **TXT**.

## 🎯 Objetivos Cumplidos

El desarrollo cumple con los requerimientos de la evaluación del **Módulo #4**, abarcando:

* **Diseño Modular:** Separación de lógica, interfaz, modelos y datos.
* **Herencia y Polimorfismo:** Implementación de clases padre y subclases especializadas.
* **Encapsulamiento:** Protección de datos sensibles mediante *getters* y *setters*.
* **Manejo de Errores:** Control de excepciones (`try-except`) para una ejecución fluida.
* **Persistencia:** Almacenamiento de datos en archivos planos (`.csv` y `.txt`).

## 🚀 Funcionalidades Principales

El sistema cumple con los siguientes requerimientos técnicos:

* **Gestión de Clientes (CRUD):**
    * Crear nuevos clientes con validación en tiempo real.
    * Listar la cartera de clientes ordenada por ID.
    * Buscar clientes específicos mediante ID.
    * Editar información de contacto mediante ID.
    * Eliminar registro de cliente mediante ID.
* **Tipología de Clientes (Herencia):**
    * *Regular:* Cliente estándar.
    * *Premium:* Incluye gestión de descuentos.
    * *Corporativo:* Incluye asociación a una empresa.
* **Persistencia de Datos:** Almacenamiento automático en archivos `.csv` (por defecto) o `.txt` según si se indica el formato.
* **Validaciones Avanzadas:** Uso de Expresiones Regulares (Regex) para emails, y validaciones lógicas para nombres, teléfonos y direcciones.
* **Sistema de Logs:** Registro automático de todas las operaciones críticas (altas, bajas, modificaciones) con fecha y hora (`datetime`) en `data/logs.txt`.

## 🛠️ Tecnologías y Conceptos Aplicados

* **Lenguaje:** Python 3
* **POO:** Clases, Objetos, Herencia, Polimorfismo, Encapsulamiento (`@property` y `setters`).
* **Manejo de Archivos:** Lectura y escritura (`open`, `csv`, `os`).
* **Manejo de Excepciones:** Bloques `try-except` y lanzamiento de errores personalizados (`raise ValueError`).
* **re:** Para validaciones con expresiones regulares.
* **datetime:** Para el registro temporal en logs.

## 📂 Estructura del Proyecto

El código está modularizado para garantizar la escalabilidad:

```
GIC_Project/
│
├── main.py                             # Archivo principal del sistema y punto de entrada del programa.
├── README.md                           # Documentación del proyecto
│
├── modulos/                            # Directorio de los módulos del sistema
│   ├── __init__.py                     # Inicializador para el sistema de importaciones
│   ├── menu.py                         # Interfaz de usuario
│   ├── gestor_clientes.py              # Lógica de negocio (Controlador)
│   ├── cliente.py                      # Definición de Clases Cliente
│   ├── validaciones.py                 # Reglas de validación de datos
│   ├── persistencias.py                # Manejo de archivos CSV/TXT
│   └── logs.py                         # Sistema de registro de operaciones
│
├── entregables/                        # Carpeta con los entregables del proyecto
│   │       └── imagenes                # Imagenes utilizadas en el informe de validación
│   ├── Diagramas UML.png               # Imagenes del diagrama UML
│   ├── DIAGRAMA_UML_MERMAID_LIVE.MD    # Codigo utilizado para la creación del diagrama UML
│   └── INFORME_VALIDACION.MD             
│
└── data/                               # Carpeta generada automáticamente
    ├── clientes.csv                    # Base de datos en CSV
    ├── clientes.txt                    # Base de datos en TXT (opcional)
    └── logs.txt                        # Historial de operaciones
```

## 📊 Diagrama de Clases (UML)

El sistema implementa la siguiente arquitectura de clases:

![Diagrama UML](entregables/Diagrama%20UML%20Oscuro.png)

## ⚙️ Instalación

1. Clonar repositorio
git clone https://github.com/ignaciotrujilloleiva/Proyecto-Modulo-4-Gestor-Inteligente-de-clientes-GIC.git

2. Entrar a carpeta
cd proyecto

3. "El proyecto se ejecuta desde **main.py**, que verifica que **menu()** solo se ejecute si se ejecuta desde este archivo." 
python main.py



## 🔧 Configuración de Persistencia (CSV vs TXT)

El sistema utiliza **CSV** por defecto. Si se desea cambiar el almacenamiento a archivos de texto (TXT), se debe modificar la instanciación en el archivo modulos/menu.py:
```
# En modulos/menu.py, línea ~10:

# Para usar TXT:
gestor = GestorClientes(formato="txt")

# Para usar CSV (Por defecto):
gestor = GestorClientes()
```
## 📄 Documentación Técnica y Validaciones

Para un entendimiento detallado del sistema y su confiabilidad, puede revisar los materiales adicionales disponibles en la carpeta **entregables/**:

**Diagrama de clases (UML):** Representación visual de la arquitectura.

**Informe de Validación:** Pruebas realizadas a los métodos de entrada de datos

## ✍️ Autor
Ignacio Trujillo Leiva  
Bootcamp Fullstack Python  
2026
