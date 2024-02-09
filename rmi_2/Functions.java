import java.rmi.*;  
import java.rmi.server.*;

public class Functions extends UnicastRemoteObject implements InterfaceServidor{  
    
    Functions () throws RemoteException {
        super();  
    }

    @Override
    public double realToEuro(double value) throws RemoteException {
        return Math.floor((value * 0.19) * 100) / 100;
    }

    @Override
    public double euroToReal(double value) throws RemoteException {
        return Math.floor((value * 5.36) * 100) / 100;
    }

    @Override
    public double dollarToReal(double value) throws RemoteException {
        return Math.floor((value * 4.97) * 100) / 100;
    }

    @Override
    public double realToDollar(double value) throws RemoteException {
        return Math.floor((value * 0.20) * 100) / 100;
    }
 
}  
