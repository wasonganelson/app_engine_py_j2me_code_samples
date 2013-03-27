import java.io.DataInputStream;
import javax.microedition.io.Connector;
public class tickerandupdate implements Runnable
{
    private char mark;
    private DataInputStream is;
    private int x;
    private StringBuffer data;
    public void run()
    {
        mark = '#';
        data = new StringBuffer();
        x = 0;
        is = null;
        try
        {
            is = Connector.openDataInputStream("http://sasanisasa.webege.com/project/forexandstockupdates/update.php");
            is.close();
            is = Connector.openDataInputStream("http://sasanisasa.webege.com/project/forexandstockupdates/stockticker.php");
            while((x = is.read()) != -1){data = data.append((char)x);}
            mStockQuote.ticker = data.toString();
            int markk = mark;
            mStockQuote.ticker = mStockQuote.ticker.substring(0,mStockQuote.ticker.indexOf(markk));
            is.close();
        }
        catch(Exception e){}
    }
}
