import com.sun.lwuit.Form;
import com.sun.lwuit.Container;
import com.sun.lwuit.Button;
import com.sun.lwuit.Label;
import com.sun.lwuit.Command;
import com.sun.lwuit.layouts.GridLayout;
import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
class startform
{
    private int formid;
    private Form f;
    private Container g;
    private Button stockquote,stockanalysis,rss;
    public startform(int x)
    {
        formid = 1;
        try
        {
            UIManager.getInstance().setThemeProps(mStockQuote.r.getTheme(mStockQuote.r.getThemeResourceNames()[0]));
        }
        catch (java.lang.Exception e){}
        f = new Form(mStockQuote.ticker);
        g = new Container();
        g = f.getContentPane();
        g.setLayout(new GridLayout(2,2));
        //creating option buttons
        stockquote = new Button("stock quotes");
        stockquote.setIcon(mStockQuote.stockquotes);
        stockquote.setTextPosition(Button.BOTTOM);
        stockquote.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectstock a = new selectstock(formid);
            }
        });
        stockanalysis = new Button("stock analysis");
        stockanalysis.setIcon(mStockQuote.stockanalysis);
        stockanalysis.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectstockanalysis a = new selectstockanalysis(formid);
            }
        });
        stockanalysis.setTextPosition(Button.BOTTOM);
        final Button forexrate = new Button("forex rates");
        forexrate.setIcon(mStockQuote.forexrate);
        forexrate.setTextPosition(Button.BOTTOM);
        forexrate.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectforexrate a = new selectforexrate();
            }
        });
        rss = new Button("news feeds");
        rss.setIcon(mStockQuote.exit);
        rss.setTextPosition(Button.BOTTOM);
        rss.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                Label label = new Label();
                canvas a = new canvas();
                label.setPreferredH(a.getWidth()/3);
                label.setPreferredW(a.getWidth()/3);
                g.addComponent(label);
                stockquote.setEnabled(false);
                stockanalysis.setEnabled(false);
                forexrate.setEnabled(false);
                rss.setEnabled(false);
                Thread t = new Thread(new getfeeds());
                t.start();
                f.repaint();
            }
        });
        g.addComponent(stockquote);
        g.addComponent(stockanalysis);
        g.addComponent(forexrate);
        g.addComponent(rss);
        Command exit = new Command("Quit");
        f.addCommand(exit);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                mStockQuote.x.notifyDestroyed();
            }
        });
        f.setTransitionInAnimator(CommonTransitions.createSlide(CommonTransitions.SLIDE_HORIZONTAL,x>formid,500));
        f.show();
    }
}