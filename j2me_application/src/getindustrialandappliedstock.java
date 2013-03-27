import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.html.HTMLComponent;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import java.io.DataInputStream;
import javax.microedition.io.Connector;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getindustrialandappliedstock implements Runnable
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
    public getindustrialandappliedstock(String choice)
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
        if(choice.equals("All")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/industrialandappliedall.php";}
        else if(choice.equals("Athi River Mining")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getarm.php";}
        else if(choice.equals("BOC Kenya")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getboc.php";}
        else if(choice.equals("British American Tobacco")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getbat.php";}
        else if(choice.equals("Carbacid Investments")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getcab.php";}
        else if(choice.equals("E.A. Cables")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/geteac.php";}
        else if(choice.equals("E.A. Breweries")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/geteab.php";}
        else if(choice.equals("Sameer Africa")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getsam.php";}
        else if(choice.equals("Kenol Kobil")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getkol.php";}
        else if(choice.equals("Mumias Sugar")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getms.php";}
        else if(choice.equals("Unga Group")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getug.php";}
        else if(choice.equals("Bamburi Cement")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getbc.php";}
        else if(choice.equals("Crown berger (K)")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getcb.php";}
        else if(choice.equals("E.A. Portland Cement")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/geteap.php";}
        else if(choice.equals("K.P.L.C")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getkplc.php";}
        else if(choice.equals("Total Kenya")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/gettotk.php";}
        else if(choice.equals("Eveready E.A.")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getev.php";}
        else if(choice.equals("Kengen")){url = "http://sasanisasa.webege.com/project/getstocks/industrialandapplied/getken.php";}
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
                selectindustrialandappliedstock a = new selectindustrialandappliedstock();
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}