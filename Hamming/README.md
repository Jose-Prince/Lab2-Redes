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
1. Entrada (mensaje recibido): 011100101010
2. Bits de datos (k): 7
3. Bits totales (n): 12
```

#### **Prueba 2**

**Emisor:**

```bash
Entrada: 00110
```

**Receptor:**

```bash
1. Entrada (mensaje recibido): 001101011
2. Bits de datos (k): 5
3. Bits totales (n): 9
```

#### **Prueba 3**

**Emisor:**

```bash
Entrada: 1110
```

**Receptor:**

```bash
1. Entrada (mensaje recibido): 00111101
2. Bits de datos (k): 4
3. Bits totales (n): 8
```
