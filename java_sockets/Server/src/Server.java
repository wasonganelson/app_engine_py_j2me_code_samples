import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
public class Server
{
    private static ServerSocket serversocket;
    private static Socket clientsocket = null;
    private static ObjectOutputStream serverreply;
    private static ObjectInputStream clientrequest;
    private static String inboundmessage,outboundmessage;
    public static void main(String args[])
    {
        final Server server = new Server();
        server.startserver();
        while(true)
        {
            server.listenforclientconnection();
        }
    }
    public void startserver()
    {
        try
        {
            serversocket = new ServerSocket(2000);
            System.out.print("\nServer is powered up ... waiting for connection ...on port "+serversocket.getLocalSocketAddress());
        }
        catch(Exception e)
        {
            System.out.print("\n\n"+e);
        }
    }
    public void listenforclientconnection()
    {
        try
        {
            clientsocket = serversocket.accept();
            System.out.print("\nConnected to client from " + clientsocket.getRemoteSocketAddress());
            serverreply = new ObjectOutputStream(clientsocket.getOutputStream());
            serverreply.flush();
            clientrequest = new ObjectInputStream(clientsocket.getInputStream());
            inboundmessage = "";
            while((inboundmessage = (String)clientrequest.readObject()) != null)
            {
                serverreply.writeObject(Server.translate(inboundmessage));
            }
            clientrequest.close();
            serverreply.close();
            clientsocket.close();
        }
        catch(Exception e)
        {
            System.out.print("\n\n"+e);
        }
    }
    public void shutdownserver()
    {
         try
         {
             serversocket.close();
         }
         catch(Exception e)
         {
             System.out.print("\n\n"+e);
         }
     }
    public static String translate(String x)
    {
        outboundmessage = "";
        try
        {
            Class.forName("org.apache.derby.jdbc.ClientDriver");
            Connection dbconnection = DriverManager.getConnection("jdbc:derby://localhost:1527/translator","translator","translator" );
            Statement statement = dbconnection.createStatement();
            ResultSet resultset = statement.executeQuery("select englishword from APP.WORDS where swahiliword="+"'"+x+"'");
            while (resultset.next())
            {
                outboundmessage = outboundmessage + resultset.getString(1);
            }
            if(outboundmessage.equals(""))
            {
                resultset = statement.executeQuery("select swahiliword from APP.WORDS where englishword="+"'"+x+"'");
                while (resultset.next())
                {
                    outboundmessage = outboundmessage + resultset.getString(1);
                }
            }
            if(outboundmessage.equals(""))
            {
                resultset = statement.executeQuery("select englishphrase from APP.PHRASES where swahiliphrase="+"'"+x+"'");
                while (resultset.next())
                {
                    outboundmessage = outboundmessage + resultset.getString(1);
                }
            }
            if(outboundmessage.equals(""))
            {
                resultset = statement.executeQuery("select swahiliphrase from APP.PHRASES where englishphrase="+"'"+x+"'");
                while (resultset.next())
                {
                    outboundmessage = outboundmessage + resultset.getString(1);
                }
            }
            resultset.close();
            statement.close();
            dbconnection.close();
        }
        catch (Exception e)
        {
            System.out.print("\n\n"+e);
        }
        return outboundmessage;
    }
}
