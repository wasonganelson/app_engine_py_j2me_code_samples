import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.html.HTMLComponent;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import java.io.DataInputStream;
import javax.microedition.io.Connector;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getagriculturalstock implements Runnable
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
    public getagriculturalstock(String choice)
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
        if(choice.equals("All")){url = "http://sasanisasa.webege.com/project/getstocks/agricultural/agriculturalall.php";}
        else if(choice.equals("Kakuzi")){url = "http://sasanisasa.webege.com/project/getstocks/agricultural/getkakuzi.php";}
        else if(choice.equals("REA Vipingo")){url = "http://sasanisasa.webege.com/project/getstocks/agricultural/getreavipingo.php";}
        else if(choice.equals("Sasini")){url = "http://sasanisasa.webege.com/project/getstocks/agricultural/getsasini.php";}
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
                selectagriculturalstock a = new selectagriculturalstock();
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}
