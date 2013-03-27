import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.html.HTMLComponent;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import java.io.DataInputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import javax.microedition.io.Connector;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
import org.kxml2.io.KXmlParser;
public class getfeeds implements Runnable
{
    private boolean loop;
    private KXmlParser p;
    private Reader ir;
    private DataInputStream is;
    private Command back;
    private HTMLComponent hc;
    private Form f;
    private int formid;
    private String response;
    private String url;
    public getfeeds()
    {
        try
        {
            UIManager.getInstance().setThemeProps(mStockQuote.r1.getTheme(mStockQuote.r1.getThemeResourceNames()[0]));
        }
        catch(Exception e){}
    }
    public void run()
    {
        formid = 2;
        url = "http://sasanisasa.webege.com/project/rss.php";
        response = "<br />";
        try
        {
            is = Connector.openDataInputStream(url);
            ir = new InputStreamReader(is);
            p = new KXmlParser();
            p.setInput(ir);
            loop = true;
            int count = 1;
            while(loop)
            {
                p.next();
                if(p.getEventType() == KXmlParser.START_TAG && p.getName().equals("description"))
                {
                    p.next();
                    if(p.getText() != null)
                    {
                        response += count+".&nbsp;&nbsp;"+p.getText()+".<br><br>";
                        count++;
                    }
                }
                else if(p.getEventType() == KXmlParser.END_DOCUMENT)
                {
                    loop = false;
                }
            }
            ir.close();
            is.close();
        }
        catch(Exception e){}
        hc = new HTMLComponent(null);
        hc.setBodyText("<b>"+response);
        hc.setEnabled(false);
        back = new Command("Back");
        f = new Form(mStockQuote.ticker);
        f.addComponent(hc);
        f.addCommand(back);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                startform a = new startform(formid);
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}