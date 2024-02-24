import java.util.Scanner;

/**
 * Tabuada
 */
public class Algoritmo3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Insira um número:");
        int numeroInserido = scanner.nextInt();
        StringBuilder resultado = new StringBuilder();

        for (int i = 0; i <= 10; i++) {
            resultado.append(numeroInserido).append("x").append(i).append("=").append(numeroInserido * i).append("\n");
        }

        System.out.println(resultado);
        scanner.close();
    }
}
