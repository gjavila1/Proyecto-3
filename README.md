# Simulador de Máquina de Turing

Un simulador visual e interactivo de Máquina de Turing desarrollado con Flask, que permite observar el funcionamiento paso a paso y validar 10 expresiones regulares diferentes.

## Características

- **Simulación Visual**: Observa el cabezal moviéndose sobre la cinta en tiempo real
- **10 Expresiones Regulares**: Patrones predefinidos para validar diferentes tipos de cadenas
- **Controles Interactivos**: Ejecución paso a paso o automática
- **Interfaz Moderna**: Diseño con colores menta y oscuros, completamente responsivo
- **Animaciones Suaves**: Transiciones fluidas para una mejor experiencia visual

##Instalación y Ejecución

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona o descarga el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto-3.1
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

4. **Abre tu navegador**
   - Visita: `http://localhost:5000`

##Expresiones Regulares Incluidas

| Patrón | Descripción | Ejemplo Válido |
|--------|-------------|----------------|
| `(a\|b)*abb` | Cadenas que terminan en "abb" | `aabb`, `baabb` |
| `0*1*` | Ceros seguidos de unos | `0011`, `111` |
| `(ab)*` | Repeticiones de "ab" | `ab`, `abab` |
| `1(01)*0` | Empieza con 1, termina con 0 | `10`, `1010` |
| `(a+b)*a(a+b)*` | Contiene al menos una "a" | `a`, `bab` |
| `a*b*` | Aes seguidas de bes | `aabb`, `bb` |
| `(aa)*` | Número par de aes | `aa`, `aaaa` |
| `0+1+` | Al menos un 0 y un 1 | `01`, `0011` |
| `(ba)*` | Repeticiones de "ba" | `ba`, `baba` |
| `a(a\|b)*b` | Empieza con "a", termina con "b" | `ab`, `aabb` |

##Cómo Usar

1. **Selecciona una expresión regular** del menú desplegable
2. **Ingresa una cadena** en el campo de texto
3. **Haz clic en "Simular"** para comenzar
4. **Controla la ejecución**:
   - **Siguiente Paso**: Avanza un paso a la vez
   - **Auto**: Ejecución automática con pausa
   - **Reiniciar**: Vuelve al estado inicial

##Arquitectura del Proyecto

```
Proyecto-3.1/
├── app.py                 # Aplicación Flask principal
├── turing_machine.py      # Clase TuringMachine
├── regex_patterns.py      # Definición de patrones
├── requirements.txt       # Dependencias
├── templates/
│   └── index.html        # Interfaz principal
└── static/
    ├── css/
    │   └── style.css     # Estilos con tema menta/oscuro
    └── js/
        └── script.js     # Lógica del frontend
```

##Componentes Principales

### `TuringMachine` (turing_machine.py)
- Simula el comportamiento de una Máquina de Turing
- Maneja estados, transiciones y movimientos del cabezal
- Optimizada para prevenir loops infinitos

### `REGEX_PATTERNS` (regex_patterns.py)
- Contiene las 10 expresiones regulares como máquinas de Turing
- Cada patrón incluye estados, alfabeto y tabla de transiciones

### Frontend (JavaScript)
- Clase `TuringSimulator` para manejar la interfaz
- Animaciones suaves del cabezal y la cinta
- Controles interactivos para la simulación

##Diseño Visual

- **Colores**: Paleta menta (#a7f3d0, #6ee7b7, #34d399) con fondo oscuro
- **Animaciones**: Transiciones CSS suaves y efectos hover
- **Responsivo**: Adaptable a dispositivos móviles y desktop
- **Accesibilidad**: Contrastes adecuados y navegación por teclado

##Casos de Prueba Sugeridos

### Patrón: `(a|b)*abb`
- ✅ Válidas: `abb`, `aabb`, `babb`, `ababb`
- ❌ Inválidas: `ab`, `ba`, `abba`

### Patrón: `0*1*`
- ✅ Válidas: ``, `0`, `1`, `001`, `0011`
- ❌ Inválidas: `10`, `010`, `101`

##Notas 

- **Prevención de loops**: Límite de 1000 pasos por simulación
- **Optimización**: Código minimalista sin funcionalidades innecesarias
- **Compatibilidad**: Funciona en Windows, macOS y Linux
- **Rendimiento**: Carga rápida y animaciones fluidas
