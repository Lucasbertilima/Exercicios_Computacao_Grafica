import java.util.Scanner;
public class Algoritmo2 {
    public static int fibonacci(int n) {
        if (n <= 1)
            return n;
        else
            return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Informe um número: ");
        
        int num = scan.nextInt();
        scan.close();
        int resultado = fibonacci(num);
        System.out.println("O " + num + "º número na sequência de Fibonacci é: " + resultado);
    }
}