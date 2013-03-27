import javax.microedition.midlet.MIDlet;
import com.sun.lwuit.Display;
import com.sun.lwuit.util.Resources;
import com.sun.lwuit.Image;
import com.sun.lwuit.plaf.UIManager;
public class mStockQuote extends MIDlet
{
    private startform a;
    private tickerandupdate tickerandupdatetape;
    private splashscreen splashform;
    public static String ticker = "Loading stockticker.....................Loading stockticker....................";
    public static MIDlet x;
    public static Resources r,r1;
    public static Image stockquotes,stockanalysis,forexrate,exit,agricultural,commercialandservices,financeandinvestments,industrial;
    public void startApp() 
    {
        int formid = 1;
        x = this;
        Display.init(this);
        splashform = new splashscreen();
        tickerandupdatetape = new tickerandupdate();
        tickerandupdatetape.run();
        try
        {
            r = Resources.open("/res/maintheme.res");
            r1 = Resources.open("/res/maintheme1.res");
            UIManager.getInstance().setThemeProps(r.getTheme(r.getThemeResourceNames()[0]));
            stockquotes = Image.createImage("/res/stockquotes.gif");
            stockanalysis = Image.createImage("/res/stockanalysis.gif");
            forexrate = Image.createImage("/res/forexrate.gif");
            exit = Image.createImage("/res/rss.gif");
            agricultural = Image.createImage("/res/agricultural.gif");
            commercialandservices = Image.createImage("/res/commercialandservices.gif");
            financeandinvestments = Image.createImage("/res/financeandinvestments.gif");
            industrial = Image.createImage("/res/industrial.gif");
        }
        catch(Exception e){}
        splashform = null;
        a = new startform(formid);
    }
    public void pauseApp()
    {
    }
    public void destroyApp(boolean unconditional)
    {
    }
}
