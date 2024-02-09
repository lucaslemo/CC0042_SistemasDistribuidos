import java.rmi.Remote;
import java.rmi.RemoteException;
import java.text.ParseException;
import java.util.List;

public interface InterfaceServidor extends Remote {

    String getIP() throws RemoteException;
    String getDateTime() throws RemoteException, ParseException;
    void sendMessage(String message) throws RemoteException;
    List<String> getMessages() throws RemoteException;

}
