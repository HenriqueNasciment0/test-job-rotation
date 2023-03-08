import java.util.Scanner;

public class Fibonacci {

    public static int fibo(int n) {
        if (n < 2) {
            return n;
        } else {
            return fibo(n - 1) + fibo(n - 2);
        }
    }

    public static boolean inFibo(int x, int[] arrayFibo) {
        for (int i = 0; i < arrayFibo.length; i++) {
            if (arrayFibo[i] == x) {
                return true;
            }
        }
        return false;

    }

    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {
            int[] arrayFibo = new int[25];
            int j = 0;

            while (j < 25) {
                arrayFibo[j] = Fibonacci.fibo(j);
                j++;
            }

            System.out.println("Digite um número: ");
            int x = scanner.nextInt();

            boolean resultado = inFibo(x, arrayFibo);

            if (resultado == true) {
                System.out.println("O número " + x + " está na sequência de Fibonacci!");
            } else {
                System.out.println("\033[0;1m" + "O número " + x + " não está na sequência de Fibonacci.");
            }
        }

    }
}
