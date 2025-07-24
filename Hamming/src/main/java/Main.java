public class Main {
  public static void main(String[] args) {
    String msg = "11011010101";
    // String msg = "11011000101";

    int totalBits = 11;
    int dataBits = 7;
    String outputPath = "./reports/r_hamming_report.txt";
    String detailPath = "./reports/r_hamming_detail.txt";
    String configPath = "./protocol.yaml";

    Receiver receiver = new Receiver(msg, totalBits, dataBits, outputPath,
        detailPath, configPath);

    // Exportar los archivos
    receiver.exportToTxt(outputPath);
    receiver.exportDetailTxt(detailPath);

    // Mostrar salida esperada
    System.out.println("Mensaje final decodificado: " + receiver.getMsgOutput());
    System.out.println("Reporte generado en: " + outputPath);
    System.out.println("Detalle generado en: " + detailPath);
  }
}
