import java.rmi.*;  
import java.rmi.server.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Functions extends UnicastRemoteObject implements InterfaceServidor{  
    
    private List<String> messages;

    Functions () throws RemoteException {
        super();  
        this.messages = new ArrayList<String>();
    }

    @Override
    public String getIP() throws RemoteException {
        try {
            return java.net.InetAddress.getLocalHost().getHostAddress();
        } catch (java.net.UnknownHostException e) {
            System.err.println("Error: " + e.getMessage());
            return "IP indisponível";
        }
    }

    @Override
    public String getDateTime() throws RemoteException, ParseException {
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm");
        return formatter.format(Calendar.getInstance().getTime());
    }

    @Override
    public void sendMessage(String message) throws RemoteException {
        this.messages.add(message);
    }

    @Override
    public List<String> getMessages() throws RemoteException {
        return this.messages;
    }
 
}  
