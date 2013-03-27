import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.html.HTMLComponent;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import java.io.DataInputStream;
import javax.microedition.io.Connector;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getfinanceandinvestmentsstock implements Runnable
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
    public getfinanceandinvestmentsstock(String choice)
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
        if(choice.equals("All")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/financeandinvestmentsall.php";}
        else if(choice.equals("Barclays Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getbbk.php";}
        else if(choice.equals("CFC Stanbic Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getcfcs.php";}
        else if(choice.equals("CFC Insurance")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getcfci.php";}
        else if(choice.equals("Housing Finance")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/gethf.php";}
        else if(choice.equals("Centum Investments")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getci.php";}
        else if(choice.equals("Kenya Commercial Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getkcb.php";}
        else if(choice.equals("National Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getnbk.php";}
        else if(choice.equals("Pan African Insurance")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getpan.php";}
        else if(choice.equals("Diamond Trust Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getdbk.php";}
        else if(choice.equals("Jubilee Insurance")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getjbi.php";}
        else if(choice.equals("Standard Chartered Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getscb.php";}
        else if(choice.equals("NIC Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getnic.php";}
        else if(choice.equals("Equity Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/geteq.php";}
        else if(choice.equals("Olympia Capital")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getoch.php";}
        else if(choice.equals("Co-operative Bank")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getcbk.php";}
        else if(choice.equals("Kenya Re-Insurance")){url = "http://sasanisasa.webege.com/project/getstocks/financeandinvestments/getkre.php";}
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
                selectfinanceandinvestmentsstock a = new selectfinanceandinvestmentsstock();
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}