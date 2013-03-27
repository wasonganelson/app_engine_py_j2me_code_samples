import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.html.HTMLComponent;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import java.io.DataInputStream;
import javax.microedition.io.Connector;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getforexrate implements Runnable
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
    public getforexrate(String choice)
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
        data = new StringBuffer();
        if(choice.equals("All")){url = "http://sasanisasa.webege.com/project/getforexrates/selectallforexrates.php";}
        else if(choice.equals("KES/UGX")){url = "http://sasanisasa.webege.com/project/getforexrates/getkesugx.php";}
        else if(choice.equals("KES/TZS")){url = "http://sasanisasa.webege.com/project/getforexrates/getkestzs.php";}
        else if(choice.equals("KES/RWF")){url = "http://sasanisasa.webege.com/project/getforexrates/getkesrwf.php";}
        else if(choice.equals("KES/BIF")){url = "http://sasanisasa.webege.com/project/getforexrates/getkesbif.php";}
        else if(choice.equals("US Dollar")){url = "http://sasanisasa.webege.com/project/getforexrates/getusdollar.php";}
        else if(choice.equals("Canadian Dollar")){url = "http://sasanisasa.webege.com/project/getforexrates/getcandollar.php";}
        else if(choice.equals("Australian Dollar")){url = "http://sasanisasa.webege.com/project/getforexrates/getaudollar.php";}
        else if(choice.equals("Sterling Pound")){url = "http://sasanisasa.webege.com/project/getforexrates/getpound.php";}
        else if(choice.equals("Euro")){url = "http://sasanisasa.webege.com/project/getforexrates/geteuro.php";}
        else if(choice.equals("Swiss Franc")){url = "http://sasanisasa.webege.com/project/getforexrates/getswissfrancs.php";}
        else if(choice.equals("Swedish Krona")){url = "http://sasanisasa.webege.com/project/getforexrates/getswedishkrona.php";}
        else if(choice.equals("Norwegian Kroner")){url = "http://sasanisasa.webege.com/project/getforexrates/getnorkroner.php";}
        else if(choice.equals("Danish Kroner")){url = "http://sasanisasa.webege.com/project/getforexrates/getdankroner.php";}
        else if(choice.equals("JPY(100)")){url = "http://sasanisasa.webege.com/project/getforexrates/getyen.php";}
        else if(choice.equals("Chinese Yuan")){url = "http://sasanisasa.webege.com/project/getforexrates/getyuan.php";}
        else if(choice.equals("Hong Kong Dollar")){url = "http://sasanisasa.webege.com/project/getforexrates/gethkdollar.php";}
        else if(choice.equals("Singapore Dollar")){url = "http://sasanisasa.webege.com/project/getforexrates/getspdollar.php";}
        else if(choice.equals("Indian Rupee")){url = "http://sasanisasa.webege.com/project/getforexrates/getrupee.php";}
        else if(choice.equals("Saudi Riyal")){url = "http://sasanisasa.webege.com/project/getforexrates/getriyal.php";}
        else if(choice.equals("AE Dirham")){url = "http://sasanisasa.webege.com/project/getforexrates/getdirham.php";}
        else if(choice.equals("SA Rand")){url = "http://sasanisasa.webege.com/project/getforexrates/getrand.php";}
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
                selectforexrate a = new selectforexrate();
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}
