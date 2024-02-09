import java.rmi.registry.LocateRegistry;
import java.rmi.Naming;
import java.rmi.Remote;


public class Servidor {

    public static void main(String args[]){  
        try{
            Functions stub = new Functions();
            LocateRegistry.createRegistry(9050);
            Naming.rebind("//localhost:9050/servidor", (Remote) stub);

            System.out.println("Servidor iniciado...");

        } catch(Exception e) {
            System.err.println("Error: " + e.toString());
            e.printStackTrace();
        }  
    }
    
}
