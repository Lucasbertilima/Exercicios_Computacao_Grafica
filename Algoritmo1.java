import java.util.GregorianCalendar;
import java.util.Scanner;

/**
 * Ano bissexto
 */
public class Algoritmo1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Insira um ano para saber se ele é bissexto (apenas números):");
        int anoInserido = scanner.nextInt();

        GregorianCalendar calendario = (GregorianCalendar) GregorianCalendar.getInstance();
        boolean isBissexto = calendario.isLeapYear(anoInserido);
        System.out.println(isBissexto ? "O ano é bissexto." : "O ano não é bissexto.");
        scanner.close();
    }
}
