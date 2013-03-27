import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.html.HTMLComponent;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import java.io.DataInputStream;
import javax.microedition.io.Connector;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getcommercialandservicesstock implements Runnable
{
    private DataInputStream is;
    private Command back;
    private HTMLComponent hc;
    private Form f;
    private int x;
    private StringBuffer data;
    private String response;
    private String url;
    private String choice;
    public getcommercialandservicesstock(String choice)
    {
        try
        {
            UIManager.getInstance().setThemeProps(mStockQuote.r1.getTheme(mStockQuote.r1.getThemeResourceNames()[0]));
        }
        catch(Exception e){}
        this.choice = choice;
    }
    public void run()
    {
        url = "";
        response = "\n\n\n\tloading...";
        data = new StringBuffer();
        f = null;
        if(choice.equals("All")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/commercialandservicesall.php";}
        else if(choice.equals("AccessKenya")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getaccesskenya.php";}
        else if(choice.equals("Marshalls E.A.")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getmarshallsea.php";}
        else if(choice.equals("Car and General")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getcarandgeneral.php";}
        else if(choice.equals("Kenya Airways")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getkenyaairways.php";}
        else if(choice.equals("CMC Holdings")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getcmc.php";}
        else if(choice.equals("Nation Media Group")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getnmg.php";}
        else if(choice.equals("TPS (Serena)")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/gettps.php";}
        else if(choice.equals("ScanGroup")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getscg.php";}
        else if(choice.equals("Standard Group")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getsg.php";}
        else if(choice.equals("Safaricom")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getsaf.php";}
        else if(choice.equals("Uchumi Supermarket")){url = "http://sasanisasa.webege.com/project/getstocks/commercialandservices/getuc.php";}
        try
        {
            is = Connector.openDataInputStream(url);
            while((x = is.read()) != -1){data = data.append((char)x);}
            response = data.toString();
            is.close();
        }
        catch(Exception e){}
        hc = new HTMLComponent(null);
        hc.setBodyText(response);
        back = new Command("Back");
        f = new Form(mStockQuote.ticker);
        f.addComponent(hc);
        f.addCommand(back);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectcommercialandservicesstock a = new selectcommercialandservicesstock();
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}
