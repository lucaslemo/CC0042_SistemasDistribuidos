import java.rmi.Naming;
import java.util.Random;

public class Cliente {
    public static void main(String[] args) {
        try {

            InterfaceServidor stub = (InterfaceServidor) Naming.lookup("//localhost:9050/servidor");

            Random r = new Random();
            Double value = 100 + (r.nextDouble() * (500 - 100));
            value = Math.floor((value * 0.19) * 100) / 100;

            System.out.println(value + " dólares, são: " + stub.dollarToReal(value) + " em real");
            System.out.println(value + " euros, são: " + stub.euroToReal(value) + " em real");
            System.out.println(value + " reais, são: " + stub.realToDollar(value) + " em dólar");
            System.out.println(value + " reais, são: " + stub.realToEuro(value) + " em euro");

        } catch (Exception e) {
            System.err.println("Error: " + e.toString());
            e.printStackTrace();
        }
    }
}
