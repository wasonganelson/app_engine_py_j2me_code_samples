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
public class selectindustrialandappliedstockanalysis
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
    public selectindustrialandappliedstockanalysis()
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
        String choices[]={"Athi River Mining","BOC Kenya","British American Tobacco",
        "Carbacid Investments","E.A. Cables","E.A. Breweries","Sameer Africa",
        "Kenol Kobil","Mumias Sugar","Unga Group","Bamburi Cement",
        "Crown berger (K)","E.A. Portland Cement","K.P.L.C","Total Kenya",
        "Eveready E.A.","Kengen"};
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
                if(choice.getSelectedItem() == "Athi River Mining" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Athi River Mining1"));t.start();}
                else if(choice.getSelectedItem() == "Athi River Mining" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Athi River Mining2"));t.start();}
                else if(choice.getSelectedItem() == "Athi River Mining" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Athi River Mining3"));t.start();}
                else if(choice.getSelectedItem() == "BOC Kenya" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("BOC Kenya1"));t.start();}
                else if(choice.getSelectedItem() == "BOC Kenya" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("BOC Kenya2"));t.start();}
                else if(choice.getSelectedItem() == "BOC Kenya" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("BOC Kenya3"));t.start();}
                else if(choice.getSelectedItem() == "British American Tobacco" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("British American Tobacco1"));t.start();}
                else if(choice.getSelectedItem() == "British American Tobacco" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("British American Tobacco2"));t.start();}
                else if(choice.getSelectedItem() == "British American Tobacco" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("British American Tobacco3"));t.start();}
                else if(choice.getSelectedItem() ==  "Carbacid Investments" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis( "Carbacid Investments1"));t.start();}
                else if(choice.getSelectedItem() ==  "Carbacid Investments" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis( "Carbacid Investments2"));t.start();}
                else if(choice.getSelectedItem() ==  "Carbacid Investments" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis( "Carbacid Investments3"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Cables" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Cables1"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Cables" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Cables2"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Cables" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Cables3"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Breweries" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Breweries1"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Breweries" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Breweries2"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Breweries" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Breweries3"));t.start();}
                else if(choice.getSelectedItem() == "Sameer Africa" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Sameer Africa1"));t.start();}
                else if(choice.getSelectedItem() == "Sameer Africa" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Sameer Africa2"));t.start();}
                else if(choice.getSelectedItem() == "Sameer Africa" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Sameer Africa3"));t.start();}
                else if(choice.getSelectedItem() == "Kenol Kobil" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Kenol Kobil1"));t.start();}
                else if(choice.getSelectedItem() == "Kenol Kobil" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Kenol Kobil2"));t.start();}
                else if(choice.getSelectedItem() == "Kenol Kobil" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Kenol Kobil3"));t.start();}
                else if(choice.getSelectedItem() == "Mumias Sugar" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Mumias Sugar1"));t.start();}
                else if(choice.getSelectedItem() == "Mumias Sugar" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Mumias Sugar2"));t.start();}
                else if(choice.getSelectedItem() == "Mumias Sugar" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Mumias Sugar3"));t.start();}
                else if(choice.getSelectedItem() == "Unga Group" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Unga Group1"));t.start();}
                else if(choice.getSelectedItem() == "Unga Group" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Unga Group2"));t.start();}
                else if(choice.getSelectedItem() == "Unga Group" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Unga Group3"));t.start();}
                else if(choice.getSelectedItem() == "Bamburi Cement" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Bamburi Cement1"));t.start();}
                else if(choice.getSelectedItem() == "Bamburi Cement" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Bamburi Cement2"));t.start();}
                else if(choice.getSelectedItem() == "Bamburi Cement" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Bamburi Cement3"));t.start();}
                else if(choice.getSelectedItem() == "Crown berger (K)" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Crown berger (K)1"));t.start();}
                else if(choice.getSelectedItem() == "Crown berger (K)" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Crown berger (K)2"));t.start();}
                else if(choice.getSelectedItem() == "Crown berger (K)" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Crown berger (K)3"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Portland Cement" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Portland Cement1"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Portland Cement" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Portland Cement2"));t.start();}
                else if(choice.getSelectedItem() == "E.A. Portland Cement" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("E.A. Portland Cement3"));t.start();}
                else if(choice.getSelectedItem() == "K.P.L.C" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("K.P.L.C1"));t.start();}
                else if(choice.getSelectedItem() == "K.P.L.C" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("K.P.L.C2"));t.start();}
                else if(choice.getSelectedItem() == "K.P.L.C" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("K.P.L.C3"));t.start();}
                else if(choice.getSelectedItem() == "Total Kenya" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Total Kenya1"));t.start();}
                else if(choice.getSelectedItem() == "Total Kenya" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Total Kenya2"));t.start();}
                else if(choice.getSelectedItem() == "Total Kenya" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Total Kenya3"));t.start();}
                else if(choice.getSelectedItem() == "Eveready E.A." && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Eveready E.A.1"));t.start();}
                else if(choice.getSelectedItem() == "Eveready E.A." && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Eveready E.A.2"));t.start();}
                else if(choice.getSelectedItem() == "Eveready E.A." && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Eveready E.A.3"));t.start();}
                else if(choice.getSelectedItem() == "Kengen" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Kengen1"));t.start();}
                else if(choice.getSelectedItem() == "Kengen" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Kengen2"));t.start();}
                else if(choice.getSelectedItem() == "Kengen" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getindustrialandappliedstockanalysis("Kengen3"));t.start();}
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