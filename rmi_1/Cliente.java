import java.rmi.Naming;

public class Cliente {
    public static void main(String[] args) {
        try {

            InterfaceServidor stub = (InterfaceServidor) Naming.lookup("//localhost:9050/servidor");

            System.out.println("Conectado a: " + stub.getIP());

            System.out.println("Hora do Servidor: " + stub.getDateTime());

            stub.sendMessage("Mensagem 1");
            stub.sendMessage("Mensagem 2");
            stub.sendMessage("Mensagem 3");

            System.out.println("Mensagens do servidor:");
            for (String message : stub.getMessages()) {
                System.out.println("\t" + message);
            }

        } catch (Exception e) {
            System.err.println("Error: " + e.toString());
            e.printStackTrace();
        }
    }
}
