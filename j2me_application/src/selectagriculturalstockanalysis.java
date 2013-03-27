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
public class selectagriculturalstockanalysis
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
    public selectagriculturalstockanalysis()
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
        String choices[]={"Kakuzi","REA Vipingo","Sasini"};
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
                if(choice.getSelectedItem() == "Kakuzi" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getagriculturalstockanalysis("Kakuzi1"));t.start();}
                else if(choice.getSelectedItem() == "Kakuzi" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getagriculturalstockanalysis("Kakuzi2"));t.start();}
                else if(choice.getSelectedItem() == "Kakuzi" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getagriculturalstockanalysis("Kakuzi3"));t.start();}
                else if(choice.getSelectedItem() == "REA Vipingo" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getagriculturalstockanalysis("REA Vipingo1"));t.start();}
                else if(choice.getSelectedItem() == "REA Vipingo" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getagriculturalstockanalysis("REA Vipingo2"));t.start();}
                else if(choice.getSelectedItem() == "REA Vipingo" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getagriculturalstockanalysis("REA Vipingo3"));t.start();}
                else if(choice.getSelectedItem() == "Sasini" && choice1.getSelectedItem() == "1 year analysis"){t = new Thread(new getagriculturalstockanalysis("Sasini1"));t.start();}
                else if(choice.getSelectedItem() == "Sasini" && choice1.getSelectedItem() == "2 year analysis"){t = new Thread(new getagriculturalstockanalysis("Sasini2"));t.start();}
                else if(choice.getSelectedItem() == "Sasini" && choice1.getSelectedItem() == "3 year analysis"){t = new Thread(new getagriculturalstockanalysis("Sasini3"));t.start();}
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
