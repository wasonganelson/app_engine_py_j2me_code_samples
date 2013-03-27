import com.sun.lwuit.Label;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import com.sun.lwuit.ComboBox;
import com.sun.lwuit.Container;
import com.sun.lwuit.Button;
import com.sun.lwuit.layouts.CoordinateLayout;
import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class selectforexrate
{
    private Thread t;
    private Form f;
    private canvas a;
    private Container g;
    private ComboBox choice;
    private Button go;
    private Label label;
    private Command back;
    private int formid;
    public selectforexrate()
    {
        formid = 3;
        try
        {
            UIManager.getInstance().setThemeProps(mStockQuote.r.getTheme(mStockQuote.r.getThemeResourceNames()[0]));
        }
        catch(Exception e){}
        //create form
        f = new Form(mStockQuote.ticker);
        a = new canvas();
        g = f.getContentPane();
        g.setLayout(new CoordinateLayout(a.getWidth(),a.getHeight()));
        //create string contenets of combobox
        String choices[]={"All","KES/UGX","KES/TZS","KES/RWF","KES/BIF",
        "US Dollar","Canadian Dollar","Australian Dollar","Sterling Pound",
        "Euro","Swiss Franc","Swedish Krona","Norwegian Kroner","Danish Kroner",
        "JPY(100)","Chinese Yuan","Hong Kong Dollar","Singapore Dollar",
        "Indian Rupee","Saudi Riyal","AE Dirham","SA Rand"};
        //create combobox
        choice = new ComboBox(choices);
        choice.setPreferredW(a.getWidth()/6*5);
        choice.setPreferredH(a.getHeight()/10);
        choice.setX(a.getWidth()/15);
        choice.setY(0);
        g.addComponent(choice);
        //create label
        label = new Label();
        //create button
        go = new Button("GO");
        go.setPreferredW(a.getWidth()/4);
        go.setX(a.getWidth()/15);
        go.setY(a.getHeight()/7);
        go.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                choice.setEnabled(false);
                go.setEnabled(false);
                label.setPreferredH(a.getWidth()/3);
                label.setPreferredW(a.getWidth()/3);
                label.setX(a.getWidth()/9);
                label.setY(a.getHeight()/4);
                g.addComponent(label);
                f.repaint();
                if(choice.getSelectedItem() == "All"){Thread t = new Thread(new getforexrate("All"));t.start();}
                else if(choice.getSelectedItem() == "KES/UGX")
                {
                    t = new Thread(new getforexrate("KES/UGX"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "KES/TZS")
                {
                    t = new Thread(new getforexrate("KES/TZS"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "KES/RWF")
                {
                    t = new Thread(new getforexrate("KES/RWF"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "KES/BIF")
                {
                    t = new Thread(new getforexrate("KES/BIF"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "US Dollar")
                {
                    t = new Thread(new getforexrate("US Dollar"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Canadian Dollar")
                {
                    t = new Thread(new getforexrate("Canadian Dollar"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Australian Dollar")
                {
                    t = new Thread(new getforexrate("Australian Dollar"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Sterling Pound")
                {
                    t = new Thread(new getforexrate("Sterling Pound"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Euro")
                {
                    t = new Thread(new getforexrate("Euro"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Swiss Franc")
                {
                    t = new Thread(new getforexrate("Swiss Franc"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Swedish Krona")
                {
                    t = new Thread(new getforexrate("Swedish Krona"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Norwegian Kroner")
                {
                    t = new Thread(new getforexrate("Norwegian Kroner"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Danish Kroner")
                {
                    t = new Thread(new getforexrate("Danish Kroner"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "JPY(100)")
                {
                    t = new Thread(new getforexrate("JPY(100)"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Chinese Yuan")
                {
                    t = new Thread(new getforexrate("Chinese Yuan"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Hong Kong Dollar")
                {
                    t = new Thread(new getforexrate("Hong Kong Dollar"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Singapore Dollar")
                {
                    t = new Thread(new getforexrate("Singapore Dollar"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Indian Rupee")
                {
                    t = new Thread(new getforexrate("Indian Rupee"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "Saudi Riyal")
                {
                    t = new Thread(new getforexrate("Saudi Riyal"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "AE Dirham")
                {
                    t = new Thread(new getforexrate("AE Dirham"));
                    t.start();
                }
                else if(choice.getSelectedItem() == "SA Rand")
                {
                    t = new Thread(new getforexrate("SA Rand"));
                    t.start();
                }
            }
        });
        g.addComponent(go);
        //create command to move back to mainform...
        back = new Command("Back");
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