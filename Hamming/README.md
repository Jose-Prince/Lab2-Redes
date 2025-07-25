# Algoritmo de Corrección de Errores – Código de Hamming

Este proyecto implementa un **algoritmo de detección y corrección de errores** utilizando el **Código de Hamming** con soporte para **bit de paridad extendida**.
Permite corregir **un solo error** y detectar si hay **más de un error**, en cuyo caso se solicita la **retransmisión** del mensaje.

## 🧪 Descripción General

* Se utiliza el **Código de Hamming** para proteger datos binarios.
* Se aplica una **paridad global (extendida)** para detectar múltiples errores.
* El receptor compara los bits de redundancia recibidos vs. calculados para:

  * Detectar errores.
  * Corregir 1 error (si es posible).
  * Solicitar retransmisión si hay múltiples errores.

## ⚙️ Entorno de ejecución

### 📤 Emisor (Transmisor)

* Lenguaje: `Python 3.13.5`
* Ejecutar desde la carpeta raíz:

```bash
cd Hamming
python transmitter.py
```

* Solicita el mensaje binario (`solo 0s y 1s`) como entrada.
* Retorna la trama de bits codificada con Hamming.

### 📥 Receptor

* Lenguaje: `Java 21 (OpenJDK)`
* Construcción y ejecución con Maven:

```bash
cd Hamming
mvn clean compile exec:java
```

* Solicita como entrada:

  * Trama de bits (mensaje codificado)
  * Cantidad total de bits (`n`)
  * Cantidad de bits de datos (`m`)

## 📁 Archivos generados

Tanto el **emisor** como el **receptor** generan dos archivos `.txt` en la carpeta `reports/`:

1. **Reporte (`*_report.txt`)**:

   * Muestra la configuración utilizada.
   * Entrada recibida y salida generada.
   * Protocolo de codificación/decodificación.

2. **Detalle (`*_detail.txt`)**:

   * Explica paso a paso:

     * Asignación de bits de paridad.
     * Cobertura de paridad por bit.
     * Detección y/o corrección de errores.

## 📘 Protocolo YAML

El archivo `protocol.yaml` define la configuración de codificación/paridad usada por emisor y receptor:

```yaml
parity: even       # Paridad: even (par) o odd (impar)
extended: true     # Paridad extendida (bit global): true / false
```

> Puedes editar este archivo para cambiar el tipo de paridad o desactivar la paridad global.

## 🧪 Casos de prueba

### Caso 1 - Sin errores

#### **Prueba 1**

**Emisor:**

```bash
Entrada: 1011001
```

**Receptor:**

```bash
1. Entrada (mensaje recibido): 101001110010
2. Bits totales (n): 12
3. Bits de datos (m): 7
```

#### **Prueba 2**

**Emisor:**

```bash
Entrada: 00110
```

**Receptor:**

```bash
1. Entrada (mensaje recibido): 1000011001
2. Bits totales (n): 10
3. Bits de datos (m): 5
```

#### **Prueba 3**

**Emisor:**

```bash
Entrada: 1110
```

**Receptor:**

```bash
1. Entrada (mensaje recibido): 00101101
2. Bits totales (n): 8
3. Bits de datos (m): 4
```

### Caso 2 - Un error

#### **Prueba 1**

**Emisor:**

```bash
Entrada: 0100101
```

**Receptor:**

```bash
1. Mensaje recibido por emisor: 110110001010
2. Entrada (mensaje con el séptimo bit con error): 110110101010
2. Bits totales (n): 12
3. Bits de datos (m): 7
```

#### **Prueba 2**

**Emisor:**

```bash
Entrada: 00110
```

**Receptor:**

```bash
1. Mensaje recibido por emisor: 1000011001
2. Entrada (mensaje con el cuarto bit con error): 1001011001
3. Bits totales (n): 10
4. Bits de datos (m): 5
```

#### **Prueba 3**

**Emisor:**

```bash
Entrada: 1110
```

**Receptor:**

```bash
1. Mensaje recibido por emisor: 00101101
2. Entrada (mensaje con el segundo bit con error): 01101101
3. Bits totales (n): 8
4. Bits de datos (m): 4
```

### Caso 3 - Dos + errores

#### **Prueba 1**

**Emisor:**

```bash
Entrada: 0100101
```

**Receptor:**

```bash
1. Mensaje recibido por emisor: 110110001010
2. Entrada (mensaje con el 3 y 4 bit con error): 110111101010
2. Bits totales (n): 12
3. Bits de datos (m): 7
```

#### **Prueba 2**

**Emisor:**

```bash
Entrada: 00110
```

**Receptor:**

```bash
1. Mensaje recibido por emisor: 1000011001
2. Entrada (mensaje con el 1,2,4 y 5 bit con error): 0101111001
3. Bits totales (n): 10
4. Bits de datos (m): 5
```

#### **Prueba 3**

**Emisor:**

```bash
Entrada: 1110
```

**Receptor:**

```bash
1. Mensaje recibido por emisor: 00101101
2. Entrada (mensaje con el 1, 4, 7 y 8 bit con error): 10111110
3. Bits totales (n): 8
4. Bits de datos (m): 4
```
