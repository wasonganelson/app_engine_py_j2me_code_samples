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
public class selectfinanceandinvestmentsstock
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
    public selectfinanceandinvestmentsstock()
    {
        formid = 3;
        try
        {
            UIManager.getInstance().setThemeProps(mStockQuote.r.getTheme(mStockQuote.r.getThemeResourceNames()[0]));
        }
        catch(Exception e){}
        //create form
        f = new Form(mStockQuote.ticker);
        g = new Container();
        a = new canvas();
        g = f.getContentPane();
        g.setLayout(new CoordinateLayout(a.getWidth(),a.getHeight()));
        //create string contenets of combobox
        String choices[]={"All","Barclays Bank","CFC Stanbic Bank","CFC Insurance",
        "Housing Finance","Centum Investments","Kenya Commercial Bank","National Bank",
        "Pan African Insurance","Diamond Trust Bank","Jubilee Insurance","Standard Chartered Bank",
        "NIC Bank","Equity Bank","Olympia Capital","Co-operative Bank",
        "Kenya Re-Insurance"};
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
                if(choice.getSelectedItem() == "All"){t = new Thread(new getfinanceandinvestmentsstock("All"));t.start();}
                else if(choice.getSelectedItem() == "Barclays Bank"){t = new Thread(new getfinanceandinvestmentsstock("Barclays Bank"));t.start();}
                else if(choice.getSelectedItem() == "CFC Stanbic Bank"){t = new Thread(new getfinanceandinvestmentsstock("CFC Stanbic Bank"));t.start();}
                else if(choice.getSelectedItem() == "CFC Insurance"){t = new Thread(new getfinanceandinvestmentsstock("CFC Insurance"));t.start();}
                else if(choice.getSelectedItem() == "Housing Finance"){t = new Thread(new getfinanceandinvestmentsstock("Housing Finance"));t.start();}
                else if(choice.getSelectedItem() == "Centum Investments"){t = new Thread(new getfinanceandinvestmentsstock("Centum Investments"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Commercial Bank"){t = new Thread(new getfinanceandinvestmentsstock("Kenya Commercial Bank"));t.start();}
                else if(choice.getSelectedItem() == "National Bank"){t = new Thread(new getfinanceandinvestmentsstock("National Bank"));t.start();}
                else if(choice.getSelectedItem() == "Pan African Insurance"){t = new Thread(new getfinanceandinvestmentsstock("Pan African Insurance"));t.start();}
                else if(choice.getSelectedItem() == "Diamond Trust Bank"){t = new Thread(new getfinanceandinvestmentsstock("Diamond Trust Bank"));t.start();}
                else if(choice.getSelectedItem() == "Jubilee Insurance"){t = new Thread(new getfinanceandinvestmentsstock("Jubilee Insurance"));t.start();}
                else if(choice.getSelectedItem() == "Standard Chartered Bank"){t = new Thread(new getfinanceandinvestmentsstock("Standard Chartered Bank"));t.start();}
                else if(choice.getSelectedItem() == "NIC Bank"){t = new Thread(new getfinanceandinvestmentsstock("NIC Bank"));t.start();}
                else if(choice.getSelectedItem() == "Equity Bank"){t = new Thread(new getfinanceandinvestmentsstock("Equity Bank"));t.start();}
                else if(choice.getSelectedItem() == "Olympia Capital"){t = new Thread(new getfinanceandinvestmentsstock("Olympia Capital"));t.start();}
                else if(choice.getSelectedItem() == "Co-operative Bank"){t = new Thread(new getfinanceandinvestmentsstock("Co-operative Bank"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Re-Insurance"){t = new Thread(new getfinanceandinvestmentsstock("Kenya Re-Insurance"));t.start();}
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