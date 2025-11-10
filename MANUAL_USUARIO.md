# 📖 Manual de Usuario - Simulador de Máquina de Turing

## 🎯 Introducción

El Simulador de Máquina de Turing es una herramienta educativa que permite visualizar el funcionamiento paso a paso de una Máquina de Turing. Esta aplicación web facilita la comprensión de conceptos fundamentales de la teoría de la computación mediante una interfaz visual intuitiva.

## 🚀 Primeros Pasos

### Instalación

1. **Descargar el proyecto**
   - Descarga todos los archivos del proyecto
   - Extrae en una carpeta de tu elección

2. **Instalar Python**
   - Asegúrate de tener Python 3.7+ instalado
   - Verifica con: `python --version`

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   - **Opción 1**: Doble clic en `run.bat` (Windows)
   - **Opción 2**: Ejecutar `python app.py` en terminal

5. **Abrir en navegador**
   - Visita: `http://localhost:5000`

## 🖥️ Interfaz de Usuario

### Elementos Principales

#### 1. **Cabecera**
- Título del simulador
- Descripción breve de la funcionalidad

#### 2. **Panel de Controles**
- **Campo de entrada**: Donde ingresas la cadena a evaluar
- **Selector de patrón**: Menú con las 10 expresiones regulares
- **Botones de control**:
  - ▶️ **Simular**: Inicia la simulación
  - ⏭️ **Siguiente Paso**: Avanza un paso
  - ⚡ **Auto**: Ejecución automática
  - 🔄 **Reiniciar**: Vuelve al estado inicial

#### 3. **Visualización de la Máquina**
- **Estado actual**: Muestra el estado en que se encuentra
- **Contador de pasos**: Número del paso actual
- **Cinta**: Representación visual de la cinta de la máquina
- **Cabezal**: Indicador de la posición actual (📍)
- **Resultado**: Muestra si la cadena fue aceptada o rechazada

#### 4. **Panel de Información**
- Descripción del patrón seleccionado
- Información contextual sobre la simulación

## 🎮 Cómo Usar el Simulador

### Paso 1: Seleccionar Expresión Regular
1. Haz clic en el menú desplegable "Expresión regular"
2. Selecciona uno de los 10 patrones disponibles
3. Lee la descripción que aparece en el panel de información

### Paso 2: Ingresar Cadena
1. Escribe la cadena que deseas evaluar en el campo "Cadena de entrada"
2. Usa solo los caracteres válidos para el patrón seleccionado
3. Presiona Enter o haz clic en "Simular"

### Paso 3: Ejecutar Simulación
1. **Simulación Paso a Paso**:
   - Haz clic en "Siguiente Paso" para avanzar manualmente
   - Observa cómo cambia el estado y se mueve el cabezal

2. **Simulación Automática**:
   - Haz clic en "Auto" para ejecución continua
   - Haz clic en "Pausar" para detener
   - La velocidad es de aproximadamente 1 paso por segundo

### Paso 4: Interpretar Resultados
- **✅ Cadena ACEPTADA**: La cadena cumple con la expresión regular
- **❌ Cadena RECHAZADA**: La cadena no cumple con el patrón

## 📋 Expresiones Regulares Disponibles

### 1. `(a|b)*abb` - Cadenas que terminan en "abb"
- **Descripción**: Acepta cualquier cadena de 'a' y 'b' que termine con "abb"
- **Ejemplos válidos**: `abb`, `aabb`, `babb`, `ababb`
- **Ejemplos inválidos**: `ab`, `ba`, `abba`, `abbc`

### 2. `0*1*` - Ceros seguidos de unos
- **Descripción**: Acepta cero o más '0' seguidos de cero o más '1'
- **Ejemplos válidos**: ``, `0`, `1`, `00`, `11`, `0011`
- **Ejemplos inválidos**: `10`, `010`, `101`

### 3. `(ab)*` - Repeticiones de "ab"
- **Descripción**: Acepta cero o más repeticiones de "ab"
- **Ejemplos válidos**: ``, `ab`, `abab`, `ababab`
- **Ejemplos inválidos**: `a`, `b`, `aba`, `ba`

### 4. `1(01)*0` - Empieza con 1, termina con 0
- **Descripción**: Empieza con '1', termina con '0', con "01" en el medio
- **Ejemplos válidos**: `10`, `1010`, `101010`
- **Ejemplos inválidos**: `1`, `0`, `11`, `00`, `101`

### 5. `(a+b)*a(a+b)*` - Contiene al menos una "a"
- **Descripción**: Cualquier cadena de 'a' y 'b' que contenga al menos una 'a'
- **Ejemplos válidos**: `a`, `ab`, `ba`, `aaa`, `bab`
- **Ejemplos inválidos**: ``, `b`, `bb`, `bbb`

### 6. `a*b*` - Aes seguidas de bes
- **Descripción**: Cero o más 'a' seguidas de cero o más 'b'
- **Ejemplos válidos**: ``, `a`, `b`, `aa`, `bb`, `aab`, `aabb`
- **Ejemplos inválidos**: `ba`, `aba`, `bab`

### 7. `(aa)*` - Número par de aes
- **Descripción**: Acepta cero o más pares de 'a'
- **Ejemplos válidos**: ``, `aa`, `aaaa`, `aaaaaa`
- **Ejemplos inválidos**: `a`, `aaa`, `aaaaa`

### 8. `0+1+` - Al menos un 0 seguido de al menos un 1
- **Descripción**: Uno o más '0' seguidos de uno o más '1'
- **Ejemplos válidos**: `01`, `001`, `011`, `0011`
- **Ejemplos inválidos**: ``, `0`, `1`, `10`, `010`

### 9. `(ba)*` - Repeticiones de "ba"
- **Descripción**: Cero o más repeticiones de "ba"
- **Ejemplos válidos**: ``, `ba`, `baba`, `bababa`
- **Ejemplos inválidos**: `a`, `b`, `ab`, `bab`

### 10. `a(a|b)*b` - Empieza con "a", termina con "b"
- **Descripción**: Empieza con 'a', termina con 'b', cualquier cosa en el medio
- **Ejemplos válidos**: `ab`, `aab`, `abb`, `aabb`, `abab`
- **Ejemplos inválidos**: `a`, `b`, `ba`, `aa`, `bb`

## 🎨 Elementos Visuales

### Colores y Significados
- **Verde menta**: Estados activos y elementos seleccionados
- **Rojo**: Estados de rechazo y errores
- **Verde**: Estados de aceptación y éxito
- **Gris oscuro**: Fondo y elementos inactivos
- **Amarillo**: Advertencias y elementos en proceso

### Animaciones
- **Movimiento del cabezal**: Transición suave entre posiciones
- **Celdas activas**: Resaltado con escala y sombra
- **Botones**: Efectos hover y transformaciones
- **Resultados**: Aparición gradual con colores distintivos

## 🔧 Solución de Problemas

### Problemas Comunes

#### 1. **La aplicación no inicia**
- Verifica que Python esté instalado
- Instala las dependencias: `pip install -r requirements.txt`
- Revisa que el puerto 5000 esté disponible

#### 2. **Error al simular**
- Verifica que la cadena contenga solo caracteres válidos
- Asegúrate de haber seleccionado una expresión regular
- Intenta con una cadena más corta

#### 3. **La simulación es muy lenta**
- Usa el modo "Siguiente Paso" para control manual
- Verifica que no haya otros procesos consumiendo recursos

#### 4. **El cabezal no se mueve**
- Actualiza la página (F5)
- Verifica que JavaScript esté habilitado
- Prueba con otro navegador

### Limitaciones
- **Máximo 1000 pasos**: Previene loops infinitos
- **Caracteres válidos**: Solo los definidos en cada patrón
- **Longitud de cadena**: Recomendado máximo 20 caracteres

## 📞 Soporte

Para problemas técnicos o dudas sobre el funcionamiento:
1. Revisa este manual completo
2. Verifica los ejemplos proporcionados
3. Consulta el archivo README.md
4. Revisa el código fuente para detalles técnicos

## 🎓 Propósito Educativo

Este simulador está diseñado para:
- **Visualizar conceptos abstractos** de máquinas de Turing
- **Facilitar el aprendizaje** de expresiones regulares
- **Demostrar la equivalencia** entre diferentes formalismos
- **Proporcionar experiencia práctica** con autómatas

¡Disfruta explorando el fascinante mundo de las Máquinas de Turing! 🤖