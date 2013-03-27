import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
public class Client
{
    public static Socket clientsocket;
    public static ObjectOutputStream clientrequest;
    public static ObjectInputStream serverreply;
    private static String inboundmessage,outboundmessage;
    public static void main(String args[])
    {
        Client client = new Client();
        client.startclient();
    }
    public void startclient()
    {

        try
        {
            form1 a = new form1();
        }
        catch(Exception e)
        {
            System.out.print("\n\n"+e);
        }
    }
    public static void sendclientrequest(String x)
    {
        try
        {
            clientsocket = new Socket("localhost",2000);
            System.out.println("\nConnected to server from "+clientsocket.getLocalSocketAddress());
            clientrequest = new ObjectOutputStream(clientsocket.getOutputStream());
            clientrequest.flush();
            serverreply = new ObjectInputStream(clientsocket.getInputStream());
            outboundmessage = "";
            outboundmessage = x;
            clientrequest.writeObject(outboundmessage);
        }
        catch(Exception e)
        {
            System.out.print("\n\nError sending request to server"+"\n\n"+e);
        }
    }
    public static String readserverresponse()
    {
        try
        {
            inboundmessage = "";
            inboundmessage = (String)serverreply.readObject();
        }
        catch (Exception e)
        {
            System.out.print("\n\nError reading request from server"+"\n\n"+e);
        }
        return inboundmessage;
    }
    public static void shutdownclient()
    {
        try
            {
                serverreply.close();
                clientrequest.close();
                clientsocket.close();
            }
            catch(Exception e)
            {
                System.out.print("\n\n"+e);
            }
    }
}