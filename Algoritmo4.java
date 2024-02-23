import java.util.Scanner;
public class Algoritmo4
{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
        System.out.print("Informe a temperatura: ");
        int num = scan.nextInt();
        
        scan.close();
        
        if (num > 35){
            System.out.println("Precisa usar protetor solar");
        } else {
            System.out.println("Não precisa usar protetor solar");
        }
	}
}
