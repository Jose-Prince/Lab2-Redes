import os
import yaml
class HammingTransmitter:
    def __init__(self, msg, config_path="./protocol.yaml", generate_report=True, output_path="./hamming_report.txt"):
        self.msg = msg
        self.msg_bits = []
        self.data_bits = len(msg)
        self.parity_bits = 0
        self.pos_redundancy_bits = []
        self.value_redundancy_bits = {}
        self.type_bit = ["d", "r", "rg"]  # d: data, r: hamming redundancy, rg: global redundancy

        # Leer configuración del archivo YAML
        config = self.loadConfig(config_path)
        self.extended = config.get("extended", True)
        self.is_even_parity = config.get("parity", "even") == "even"
        self.global_redundancy_bits = 1 if self.extended else 0
        
        self.calculateParityBits()
        self.quantity_bits = self.data_bits + self.parity_bits + self.global_redundancy_bits

        self.positionRedundancyBits()
        self.calculateParityBitsValues()
        self.createMsg()
        self.setAllParityBits()
        
        if generate_report:
            self.exportToTxt(filename=output_path)
        
    def loadConfig(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def calculateParityBits(self):
        while (2 ** self.parity_bits < (self.data_bits + self.parity_bits + 1)):
            self.parity_bits += 1

    def positionRedundancyBits(self):
        position_temp = 0
        max_position = self.quantity_bits - 1 if self.extended else self.quantity_bits
        while (2 ** position_temp <= max_position):
            self.pos_redundancy_bits.append(2 ** position_temp)
            position_temp += 1

    def calculateParityBitsValues(self):
        for r in self.pos_redundancy_bits:
            self.value_redundancy_bits[r] = []
            for i in range(1, self.quantity_bits + 1):
                if i & r != 0 and (not self.extended or i != self.quantity_bits):
                    self.value_redundancy_bits[r].append(i)

    def createMsg(self):
        j = 0
        self.msg_bits = []

        for i in range(1, self.quantity_bits + 1):
            if self.extended and i == self.quantity_bits:
                self.msg_bits.append((None, self.type_bit[2]))  # bit de paridad global (al final)
            elif i in self.pos_redundancy_bits:
                self.msg_bits.append((None, self.type_bit[1]))  # bit de paridad hamming
            else:
                self.msg_bits.append((int(self.msg[j]), self.type_bit[0]))
                j += 1

    def calculateParity(self, position):
        values = self.value_redundancy_bits[position]
        count_ones = sum(
            1 for i in values
            if (bit := self.msg_bits[i - 1][0]) is not None and bit == 1
        )
        return count_ones % 2 if self.is_even_parity else (count_ones + 1) % 2

    def calculateParityExtend(self):
        count_ones = sum(
            1 for i in range(self.quantity_bits - 1)  # excluye el último bit (extendido)
            if (bit := self.msg_bits[i][0]) is not None and bit == 1
        )
        return count_ones % 2 if self.is_even_parity else (count_ones + 1) % 2

    def setAllParityBits(self):
        # 1. Calcular paridades Hamming
        for position in self.pos_redundancy_bits:
            parity = self.calculateParity(position)
            self.msg_bits[position - 1] = (parity, self.type_bit[1])

        # 2. Calcular paridad extendida si está activada
        if self.extended:
            parity_extend = self.calculateParityExtend()
            self.msg_bits[-1] = (parity_extend, self.type_bit[2])

    def exportToTxt(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("===== HAMMING TRANSMITTER REPORT =====\n\n")

            f.write("Configuración:\n")
            f.write(f"- Paridad usada: {'par' if self.is_even_parity else 'impar'}\n")
            f.write(f"- Paridad extendida: {'sí' if self.extended else 'no'}\n")
            f.write(f"- Bits de datos: {self.data_bits}\n")
            f.write(f"- Bits de paridad Hamming: {self.parity_bits}\n")
            if self.extended:
                f.write(f"- Bits de redundancia global (extendido): {self.global_redundancy_bits}\n")
            f.write(f"- Bits totales (codificados): {self.quantity_bits}\n")
            f.write(f"- Posiciones de paridad Hamming: {self.pos_redundancy_bits}\n")
            if self.extended:
                f.write(f"- Posición de bit de paridad global (extendido): {self.quantity_bits}\n")
            f.write("\n")

            f.write("Mensaje recibido (bits de datos):\n")
            f.write(f"{self.msg}\n\n")

            f.write("Mensaje codificado (msg_bits):\n")
            f.write("Posición\tBit\tTipo\n")
            for i, (val, tipo) in enumerate(self.msg_bits, start=1):
                f.write(f"{i}\t\t{val if val is not None else '?'}\t{tipo}\n")
            f.write("\n")

            f.write("Cobertura de cada bit de paridad Hamming:\n")
            for r, positions in self.value_redundancy_bits.items():
                f.write(f"r{r} (pos {r}) -> cubre: {positions}\n")
            f.write("\n")

            f.write("Mensaje binario final (para transmisión):\n")
            final = ''.join(str(bit if bit is not None else 'X') for bit, _ in self.msg_bits)
            f.write(final + "\n")

            f.write("\n===== FIN DEL REPORTE =====\n")

def menu():
    report_path="./reports/hamming_report.txt"
    config_path="./protocol.yaml"

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    extended = config.get("extended", True)
    parity_type = config.get("parity", "even")

    print("===== TRANSMISOR HAMMING =====\n")
    print(f"Se utilizará la configuración definida en el archivo: '{os.path.abspath(config_path)}'\n")
    print("Configuración cargada:")
    print(f"- Paridad: {'par' if parity_type == 'even' else 'impar'}")
    print(f"- Paridad extendida: {'sí' if extended else 'no'}\n")

    print("\tHint: Si deseas modificar el tipo de paridad (even/odd) o activar/desactivar la paridad extendida (true/false), edita el archivo 'protocol.yaml'\n")

    print("Ingrese los datos para codificar con Hamming:\n")

    # Solicitar mensaje binario
    msg_valido = False
    msg = ""

    while not msg_valido:
        msg = input("Ingrese el mensaje binario (solo 0s y 1s): ").strip()
        msg_valido = all(c in "01" for c in msg) and len(msg) > 0
        if not msg_valido:
            print("Entrada inválida. Solo se permiten 0s y 1s.")
    
    # Crear transmisor
    transmitter = HammingTransmitter(
        msg=msg,
        config_path=config_path,
        generate_report=True,
        output_path=report_path
    )

    # Mostrar mensaje final codificado y resumen
    mensaje_codificado = ''.join(str(bit) for bit, _ in transmitter.msg_bits)
    print("Codificación final del mensaje:", mensaje_codificado)
    print(f"Reporte generado en: '{os.path.abspath(report_path)}'")

if __name__ == "__main__":
  menu()
