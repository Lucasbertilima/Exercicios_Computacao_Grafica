import java.util.Scanner;

/**
 * Maior de idade
 */
public class Algoritmo5 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Insira sua idade:");
        int idadeInserida = scanner.nextInt();

        System.out.println(idadeInserida < 18 ? "É menor de idade." : "É maior de idade");
        scanner.close();
    }
}
