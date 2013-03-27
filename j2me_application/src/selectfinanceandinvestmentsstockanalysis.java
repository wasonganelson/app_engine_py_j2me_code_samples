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
public class selectfinanceandinvestmentsstockanalysis
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
    public selectfinanceandinvestmentsstockanalysis()
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
        String choices[]={"Barclays Bank","CFC Stanbic Bank","CFC Insurance",
        "Housing Finance","Centum Investments","Kenya Commercial Bank","National Bank",
        "Pan African Insurance","Diamond Trust Bank","Jubilee Insurance","Standard Chartered Bank",
        "NIC Bank","Equity Bank","Olympia Capital","Co-operative Bank",
        "Kenya Re-Insurance"};
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
                if(choice.getSelectedItem() == "Barclays Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Barclays Bank1"));t.start();}
                else if(choice.getSelectedItem() == "Barclays Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Barclays Bank2"));t.start();}
                else if(choice.getSelectedItem() == "Barclays Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Barclays Bank3"));t.start();}
                else if(choice.getSelectedItem() == "CFC Stanbic Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("CFC Stanbic Bank1"));t.start();}
                else if(choice.getSelectedItem() == "CFC Stanbic Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("CFC Stanbic Bank2"));t.start();}
                else if(choice.getSelectedItem() == "CFC Stanbic Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("CFC Stanbic Bank3"));t.start();}
                else if(choice.getSelectedItem() == "CFC Insurance" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("CFC Insurance1"));t.start();}
                else if(choice.getSelectedItem() == "CFC Insurance" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("CFC Insurance2"));t.start();}
                else if(choice.getSelectedItem() == "CFC Insurance" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("CFC Insurance3"));t.start();}
                else if(choice.getSelectedItem() == "Housing Finance" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Housing Finance1"));t.start();}
                else if(choice.getSelectedItem() == "Housing Finance" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Housing Finance2"));t.start();}
                else if(choice.getSelectedItem() == "Housing Finance" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Housing Finance3"));t.start();}
                else if(choice.getSelectedItem() == "Centum Investments" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Centum Investments1"));t.start();}
                else if(choice.getSelectedItem() == "Centum Investments" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Centum Investments2"));t.start();}
                else if(choice.getSelectedItem() == "Centum Investments" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Centum Investments3"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Commercial Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Kenya Commercial Bank1"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Commercial Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Kenya Commercial Bank2"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Commercial Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Kenya Commercial Bank3"));t.start();}
                else if(choice.getSelectedItem() == "National Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("National Bank1"));t.start();}
                else if(choice.getSelectedItem() == "National Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("National Bank2"));t.start();}
                else if(choice.getSelectedItem() == "National Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("National Bank3"));t.start();}
                else if(choice.getSelectedItem() == "Pan African Insurance" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Pan African Insurance1"));t.start();}
                else if(choice.getSelectedItem() == "Pan African Insurance" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Pan African Insurance2"));t.start();}
                else if(choice.getSelectedItem() == "Pan African Insurance" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Pan African Insurance3"));t.start();}
                else if(choice.getSelectedItem() == "Diamond Trust Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Diamond Trust Bank1"));t.start();}
                else if(choice.getSelectedItem() == "Diamond Trust Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Diamond Trust Bank2"));t.start();}
                else if(choice.getSelectedItem() == "Diamond Trust Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Diamond Trust Bank3"));t.start();}
                else if(choice.getSelectedItem() == "Jubilee Insurance" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Jubilee Insurance1"));t.start();}
                else if(choice.getSelectedItem() == "Jubilee Insurance" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Jubilee Insurance2"));t.start();}
                else if(choice.getSelectedItem() == "Jubilee Insurance" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Jubilee Insurance3"));t.start();}
                else if(choice.getSelectedItem() == "Standard Chartered Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Standard Chartered Bank1"));t.start();}
                else if(choice.getSelectedItem() == "Standard Chartered Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Standard Chartered Bank2"));t.start();}
                else if(choice.getSelectedItem() == "Standard Chartered Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Standard Chartered Bank3"));t.start();}
                else if(choice.getSelectedItem() == "NIC Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("NIC Bank1"));t.start();}
                else if(choice.getSelectedItem() == "NIC Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("NIC Bank2"));t.start();}
                else if(choice.getSelectedItem() == "NIC Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("NIC Bank3"));t.start();}
                else if(choice.getSelectedItem() == "Equity Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Equity Bank1"));t.start();}
                else if(choice.getSelectedItem() == "Equity Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Equity Bank2"));t.start();}
                else if(choice.getSelectedItem() == "Equity Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Equity Bank3"));t.start();}
                else if(choice.getSelectedItem() == "Olympia Capital" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Olympia Capital1"));t.start();}
                else if(choice.getSelectedItem() == "Olympia Capital" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Olympia Capital2"));t.start();}
                else if(choice.getSelectedItem() == "Olympia Capital" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Olympia Capital3"));t.start();}
                else if(choice.getSelectedItem() == "Co-operative Bank" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Co-operative Bank1"));t.start();}
                else if(choice.getSelectedItem() == "Co-operative Bank" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Co-operative Bank2"));t.start();}
                else if(choice.getSelectedItem() == "Co-operative Bank" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Co-operative Bank3"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Re-Insurance" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Kenya Re-Insurance1"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Re-Insurance" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Kenya Re-Insurance2"));t.start();}
                else if(choice.getSelectedItem() == "Kenya Re-Insurance" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getfinanceandinvestmentsstockanalysis("Kenya Re-Insurance3"));t.start();}

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