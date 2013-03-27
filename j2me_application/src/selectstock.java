import com.sun.lwuit.Form;
import com.sun.lwuit.Container;
import com.sun.lwuit.Command;
import com.sun.lwuit.Button;
import com.sun.lwuit.layouts.GridLayout;
import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
class selectstock
{
    private Button agriculturalstocks,commercialandservicesstocks,financeandinvestmentsstocks,industrialandappliedstocks;
    private int formid;
    public selectstock(int x)
    {
        formid = 2;
        try
        {
            UIManager.getInstance().setThemeProps(mStockQuote.r.getTheme(mStockQuote.r.getThemeResourceNames()[0]));
        }
        catch (java.lang.Exception e){}
        Form f = new Form(mStockQuote.ticker);
        Container g = new Container();
        g = f.getContentPane();
        g.setLayout(new GridLayout(2,2));
        //creating option buttons
        agriculturalstocks = new Button("Agricultural stocks");
        agriculturalstocks.setIcon(mStockQuote.agricultural);
        agriculturalstocks.setTextPosition(Button.BOTTOM);
        agriculturalstocks.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectagriculturalstock a = new selectagriculturalstock();
            }
        });
        commercialandservicesstocks = new Button("Commercial and Services stocks");
        commercialandservicesstocks.setIcon(mStockQuote.commercialandservices);
        commercialandservicesstocks.setTextPosition(Button.BOTTOM);
        commercialandservicesstocks.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectcommercialandservicesstock a = new selectcommercialandservicesstock();
            }
        });
        financeandinvestmentsstocks = new Button("Finance and Investments stocks");
        financeandinvestmentsstocks.setIcon(mStockQuote.financeandinvestments);
        financeandinvestmentsstocks.setTextPosition(Button.BOTTOM);
        financeandinvestmentsstocks.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectfinanceandinvestmentsstock a = new selectfinanceandinvestmentsstock();
            }
        });
        industrialandappliedstocks = new Button("Industrial and Applied stocks");
        industrialandappliedstocks.setIcon(mStockQuote.industrial);
        industrialandappliedstocks.setTextPosition(Button.BOTTOM);
        industrialandappliedstocks.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectindustrialandappliedstock a = new selectindustrialandappliedstock();
            }
        });
        g.addComponent(agriculturalstocks);
        g.addComponent(commercialandservicesstocks);
        g.addComponent(financeandinvestmentsstocks);
        g.addComponent(industrialandappliedstocks);
        Command back = new Command("Back");
        f.addCommand(back);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                startform a = new startform(formid);
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createSlide(CommonTransitions.SLIDE_HORIZONTAL,x>formid,500));
        f.show();
    }
}