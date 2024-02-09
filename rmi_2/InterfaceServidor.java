import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceServidor extends Remote {

    double euroToReal(double value) throws RemoteException;
    double realToEuro(double value) throws RemoteException;
    double realToDollar(double value) throws RemoteException;
    double dollarToReal(double value) throws RemoteException;

}
