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
public class selectcommercialandservicesstockanalysis
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
    public selectcommercialandservicesstockanalysis()
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
        String choices[]={"AccessKenya","Marshalls E.A.","Car and General",
        "Kenya Airways","CMC Holdings","Nation Media Group","TPS (Serena)",
        "ScanGroup","Standard Group","Safaricom","Uchumi Supermarket"};
        String choices1[]={"1 year analysis","2 year analysis","3 year analysis"};
        //create combobox
        choice = new ComboBox(choices);
        choice.setPreferredW(a.getWidth()/6*5);
        choice.setPreferredH(a.getHeight()/10);
        choice.setX(a.getWidth()/15);
        choice.setY(0);
        choice1 = new ComboBox(choices1);
        choice1.setPreferredW(a.getWidth()/6*5);
        choice1.setPreferredH(a.getHeight()/10);
        choice1.setX(a.getWidth()/15);
        choice1.setY(a.getHeight()/6);
        g.addComponent(choice);
        g.addComponent(choice1);
        //create button
        go = new Button("GO");
        go.setPreferredW(a.getWidth()/4);
        go.setX(a.getWidth()/15);
        go.setY(a.getHeight()/3);
        go.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                choice.setEnabled(false);
                choice1.setEnabled(false);
                go.setEnabled(false);
                label = new Label();
                label.setPreferredH(a.getWidth()/3);
                label.setPreferredW(a.getWidth()/3);
                label.setX(a.getWidth()/8);
                label.setY(a.getHeight()/4);
                g.addComponent(label);
                f.repaint();
                if(choice.getSelectedItem() == "AccessKenya" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("AccessKenya1"));t.start();}
                else if(choice.getSelectedItem() == "AccessKenya" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("AccessKenya2"));t.start();}
                else if(choice.getSelectedItem() == "AccessKenya" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("AccessKenya3"));t.start();}
                else if(choice.getSelectedItem() == "Marshalls E.A." && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Marshalls E.A.1"));t.start();}
                else if(choice.getSelectedItem() == "Marshalls E.A." && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Marshalls E.A.2"));t.start();}
                else if(choice.getSelectedItem() == "Marshalls E.A." && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Marshalls E.A.3"));t.start();}
                else if(choice.getSelectedItem() == "Car and General" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Car and General1"));t.start();}
                else if(choice.getSelectedItem() == "Car and General" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Car and General2"));t.start();}
                else if(choice.getSelectedItem() == "Car and General" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Car and General3"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Airways" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Kenya Airways1"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Airways" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Kenya Airways2"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Airways" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Kenya Airways3"));t.start();}
                else if(choice.getSelectedItem() == "CMC Holdings" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("CMC Holdings1"));t.start();}
                else if(choice.getSelectedItem() == "CMC Holdings" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("CMC Holdings2"));t.start();}
                else if(choice.getSelectedItem() == "CMC Holdings" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("CMC Holdings3"));t.start();}
                else if(choice.getSelectedItem() == "Nation Media Group" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Nation Media Group1"));t.start();}
                else if(choice.getSelectedItem() == "Nation Media Group" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Nation Media Group2"));t.start();}
                else if(choice.getSelectedItem() == "Nation Media Group" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Nation Media Group3"));t.start();}
                else if(choice.getSelectedItem() == "TPS (Serena)" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("TPS (Serena)1"));t.start();}
                else if(choice.getSelectedItem() == "TPS (Serena)" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("TPS (Serena)2"));t.start();}
                else if(choice.getSelectedItem() == "TPS (Serena)" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("TPS (Serena)3"));t.start();}
                else if(choice.getSelectedItem() == "ScanGroup" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("ScanGroup1"));t.start();}
                else if(choice.getSelectedItem() == "ScanGroup" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("ScanGroup2"));t.start();}
                else if(choice.getSelectedItem() == "ScanGroup" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("ScanGroup3"));t.start();}
                else if(choice.getSelectedItem() == "Standard Group" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Standard Group1"));t.start();}
                else if(choice.getSelectedItem() == "Standard Group" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Standard Group2"));t.start();}
                else if(choice.getSelectedItem() == "Standard Group" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Standard Group3"));t.start();}
                else if(choice.getSelectedItem() == "Safaricom" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Safaricom1"));t.start();}
                else if(choice.getSelectedItem() == "Safaricom" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Safaricom2"));t.start();}
                else if(choice.getSelectedItem() == "Safaricom" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Safaricom3"));t.start();}
                else if(choice.getSelectedItem() == "Uchumi Supermarket" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Uchumi Supermarket1"));t.start();}
                else if(choice.getSelectedItem() == "Uchumi Supermarket" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Uchumi Supermarket2"));t.start();}
                else if(choice.getSelectedItem() == "Uchumi Supermarket" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getcommercialandservicesstockanalysis("Uchumi Supermarket3"));t.start();}
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
                selectstockanalysis a = new selectstockanalysis(formid);
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}
