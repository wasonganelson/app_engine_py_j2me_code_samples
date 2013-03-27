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
public class selectindustrialandappliedstock
{
    private Thread t;
    private Form f;
    private canvas a;
    private Container g;
    private ComboBox choice,choice1;
    private Button go;
    private Label label;
    private Command back;
    private int formid;
    public selectindustrialandappliedstock()
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
        String choices[]={"All","Athi River Mining","BOC Kenya","British American Tobacco",
        "Carbacid Investments","E.A. Cables","E.A. Breweries","Sameer Africa",
        "Kenol Kobil","Mumias Sugar","Unga Group","Bamburi Cement",
        "Crown berger (K)","E.A. Portland Cement","K.P.L.C","Total Kenya",
        "Eveready E.A.","Kengen"};
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
                if(choice.getSelectedItem() == "All"){t = new Thread(new getindustrialandappliedstock("All"));t.start();}
                else if(choice.getSelectedItem() == "Athi River Mining"){t = new Thread(new getindustrialandappliedstock("Athi River Mining"));t.start();}
                else if(choice.getSelectedItem() == "BOC Kenya"){t = new Thread(new getindustrialandappliedstock("BOC Kenya"));t.start();}
                else if(choice.getSelectedItem() == "British American Tobacco"){t = new Thread(new getindustrialandappliedstock("British American Tobacco"));t.start();}
                else if(choice.getSelectedItem() == "Carbacid Investments"){t = new Thread(new getindustrialandappliedstock("Carbacid Investments"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Cables"){t = new Thread(new getindustrialandappliedstock("E.A. Cables"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Breweries"){t = new Thread(new getindustrialandappliedstock("E.A. Breweries"));t.start();}
                else if(choice.getSelectedItem() == "Sameer Africa"){t = new Thread(new getindustrialandappliedstock("Sameer Africa"));t.start();}
                else if(choice.getSelectedItem() == "Kenol Kobil"){t = new Thread(new getindustrialandappliedstock("Kenol Kobil"));t.start();}
                else if(choice.getSelectedItem() == "Mumias Sugar"){t = new Thread(new getindustrialandappliedstock("Mumias Sugar"));t.start();}
                else if(choice.getSelectedItem() == "Unga Group"){t = new Thread(new getindustrialandappliedstock("Unga Group"));t.start();}
                else if(choice.getSelectedItem() == "Bamburi Cement"){t = new Thread(new getindustrialandappliedstock("Bamburi Cement"));t.start();}
                else if(choice.getSelectedItem() == "Crown berger (K)"){t = new Thread(new getindustrialandappliedstock("Crown berger (K)"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Portland Cement"){t = new Thread(new getindustrialandappliedstock("E.A. Portland Cement"));t.start();}
                else if(choice.getSelectedItem() == "K.P.L.C"){t = new Thread(new getindustrialandappliedstock("K.P.L.C"));t.start();}
                else if(choice.getSelectedItem() == "Total Kenya"){t = new Thread(new getindustrialandappliedstock("Total Kenya"));t.start();}
                else if(choice.getSelectedItem() == "Eveready E.A."){t = new Thread(new getindustrialandappliedstock("Eveready E.A."));t.start();}
                else if(choice.getSelectedItem() == "Kengen"){t = new Thread(new getindustrialandappliedstock("Kengen"));t.start();}
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