import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getagriculturalstockanalysis implements Runnable
{
    private canvas a;
    private String url;
    private Form f;
    private Command back;
    private String choice;
    public getagriculturalstockanalysis(String choice)
    {
        try
        {
            UIManager.getInstance().setThemeProps(mStockQuote.r1.getTheme(mStockQuote.r1.getThemeResourceNames()[0]));
        }
        catch(Exception e){}
        this.choice = choice;
    }
    public void run()
    {
        if(choice.equals("Kakuzi1")){url = "http://live.mystocks.co.ke/graphs/KUKZ.Chart?r=370";}
        else if(choice.equals("Kakuzi2")){url = "http://live.mystocks.co.ke/graphs/KUKZ.Chart?r=740";}
        else if(choice.equals("Kakuzi3")){url = "http://live.mystocks.co.ke/graphs/KUKZ.Chart?r=1100";}
        else if(choice.equals("REA Vipingo1")){url = "http://live.mystocks.co.ke/graphs/REA.Chart?r=370";}
        else if(choice.equals("REA Vipingo2")){url = "http://live.mystocks.co.ke/graphs/REA.Chart?r=740";}
        else if(choice.equals("REA Vipingo3")){url = "http://live.mystocks.co.ke/graphs/REA.Chart?r=1100";}
        else if(choice.equals("Sasini1")){url = "http://live.mystocks.co.ke/graphs/SASN.Chart?r=370";}
        else if(choice.equals("Sasini2")){url = "http://live.mystocks.co.ke/graphs/SASN.Chart?r=740";}
        else if(choice.equals("Sasini3")){url = "http://live.mystocks.co.ke/graphs/SASN.Chart?r=1100";}
        a = new canvas();
        back = new Command("Back");
        f = new Form();
        f.addComponent(a.getchart(url));
        f.addCommand(back);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectagriculturalstockanalysis a = new selectagriculturalstockanalysis();
            }
        });
        f.setScrollableY(true);
        f.setScrollableX(true);
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}
