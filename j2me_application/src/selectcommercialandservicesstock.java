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
public class selectcommercialandservicesstock
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
    public selectcommercialandservicesstock()
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
        g = new Container();
        g = f.getContentPane();
        g.setLayout(new CoordinateLayout(a.getWidth(),a.getHeight()));
        //create string contenets of combobox
        String choices[]={"All","AccessKenya","Marshalls E.A.","Car and General",
        "Kenya Airways","CMC Holdings","Nation Media Group","TPS (Serena)",
        "ScanGroup","Standard Group","Safaricom","Uchumi Supermarket"};
        //create combobox
        choice = new ComboBox(choices);
        choice.setPreferredW(a.getWidth()/6*5);
        choice.setPreferredH(a.getHeight()/10);
        choice.setX(a.getWidth()/15);
        choice.setY(0);
        g.addComponent(choice);
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
                label = new Label();
                label.setPreferredH(a.getWidth()/3);
                label.setPreferredW(a.getWidth()/3);
                label.setX(a.getWidth()/9);
                label.setY(a.getHeight()/4);
                g.addComponent(label);
                f.repaint();
                if(choice.getSelectedItem() == "All"){t = new Thread(new getcommercialandservicesstock("All"));t.start();}
                else if(choice.getSelectedItem() == "AccessKenya"){t = new Thread(new getcommercialandservicesstock("AccessKenya"));t.start();}
                else if(choice.getSelectedItem() == "Marshalls E.A."){t = new Thread(new getcommercialandservicesstock("Marshalls E.A."));t.start();}
                else if(choice.getSelectedItem() == "Car and General"){t = new Thread(new getcommercialandservicesstock("Car and General"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Airways"){t = new Thread(new getcommercialandservicesstock("Kenya Airways"));t.start();}
                else if(choice.getSelectedItem() == "CMC Holdings"){t = new Thread(new getcommercialandservicesstock("CMC Holdings"));t.start();}
                else if(choice.getSelectedItem() == "Nation Media Group"){t = new Thread(new getcommercialandservicesstock("Nation Media Group"));t.start();}
                else if(choice.getSelectedItem() == "TPS (Serena)"){t = new Thread(new getcommercialandservicesstock("TPS (Serena)"));t.start();}
                else if(choice.getSelectedItem() == "ScanGroup"){t = new Thread(new getcommercialandservicesstock("ScanGroup"));t.start();}
                else if(choice.getSelectedItem() == "Standard Group"){t = new Thread(new getcommercialandservicesstock("Standard Group"));t.start();}
                else if(choice.getSelectedItem() == "Safaricom"){t = new Thread(new getcommercialandservicesstock("Safaricom"));t.start();}
                else if(choice.getSelectedItem() == "Uchumi Supermarket"){t = new Thread(new getcommercialandservicesstock("Uchumi Supermarket"));t.start();}
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
                selectstock a = new selectstock(formid);
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}