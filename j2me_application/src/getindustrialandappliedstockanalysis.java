import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getindustrialandappliedstockanalysis implements Runnable
{
    private canvas a;
    private String url;
    private Form f;
    private Command back;
    private String choice;
    public getindustrialandappliedstockanalysis(String choice)
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
        if(choice.equals("Athi River Mining1")){url = "http://live.mystocks.co.ke/graphs/ARM.Chart?r=370";}
        else if(choice.equals("Athi River Mining2")){url = "http://live.mystocks.co.ke/graphs/ARM.Chart?r=740";}
        else if(choice.equals("Athi River Mining3")){url = "http://live.mystocks.co.ke/graphs/ARM.Chart?r=1100";}
        else if(choice.equals("BOC Kenya1")){url = "http://live.mystocks.co.ke/graphs/BOC.Chart?r=370";}
        else if(choice.equals("BOC Kenya2")){url = "http://live.mystocks.co.ke/graphs/BOC.Chart?r=740";}
        else if(choice.equals("BOC Kenya3")){url = "http://live.mystocks.co.ke/graphs/BOC.Chart?r=1100";}
        else if(choice.equals("British American Tobacco1")){url = "http://live.mystocks.co.ke/graphs/BAT.Chart?r=370";}
        else if(choice.equals("British American Tobacco2")){url = "http://live.mystocks.co.ke/graphs/BAT.Chart?r=740";}
        else if(choice.equals("British American Tobacco3")){url = "http://live.mystocks.co.ke/graphs/BAT.Chart?r=1100";}
        else if(choice.equals("Carbacid Investments1")){url = "http://live.mystocks.co.ke/graphs/CARB.Chart?r=370";}
        else if(choice.equals("Carbacid Investments2")){url = "http://live.mystocks.co.ke/graphs/CARB.Chart?r=740";}
        else if(choice.equals("Carbacid Investments3")){url = "http://live.mystocks.co.ke/graphs/CARB.Chart?r=1100";}
        else if(choice.equals("E.A. Cables1")){url = "http://live.mystocks.co.ke/graphs/CABL.Chart?r=370";}
        else if(choice.equals("E.A. Cables2")){url = "http://live.mystocks.co.ke/graphs/CABL.Chart?r=740";}
        else if(choice.equals("E.A. Cables3")){url = "http://live.mystocks.co.ke/graphs/CABL.Chart?r=1100";}
        else if(choice.equals("E.A. Breweries1")){url = "http://live.mystocks.co.ke/graphs/EABL.Chart?r=370";}
        else if(choice.equals("E.A. Breweries2")){url = "http://live.mystocks.co.ke/graphs/EABL.Chart?r=740";}
        else if(choice.equals("E.A. Breweries3")){url = "http://live.mystocks.co.ke/graphs/EABL.Chart?r=1100";}
        else if(choice.equals("Sameer Africa1")){url = "http://live.mystocks.co.ke/graphs/FIRE.Chart?r=370";}
        else if(choice.equals("Sameer Africa2")){url = "http://live.mystocks.co.ke/graphs/FIRE.Chart?r=740";}
        else if(choice.equals("Sameer Africa3")){url = "http://live.mystocks.co.ke/graphs/FIRE.Chart?r=1100";}
        else if(choice.equals("Kenol Kobil1")){url = "http://live.mystocks.co.ke/graphs/KENO.Chart?r=370";}
        else if(choice.equals("Kenol Kobil2")){url = "http://live.mystocks.co.ke/graphs/KENO.Chart?r=740";}
        else if(choice.equals("Kenol Kobil3")){url = "http://live.mystocks.co.ke/graphs/KENO.Chart?r=1100";}
        else if(choice.equals("Mumias Sugar1")){url = "http://live.mystocks.co.ke/graphs/MSC.Chart?r=370";}
        else if(choice.equals("Mumias Sugar2")){url = "http://live.mystocks.co.ke/graphs/MSC.Chart?r=740";}
        else if(choice.equals("Mumias Sugar3")){url = "http://live.mystocks.co.ke/graphs/MSC.Chart?r=1100";}
        else if(choice.equals("Unga Group1")){url = "http://live.mystocks.co.ke/graphs/UNGA.Chart?r=370";}
        else if(choice.equals("Unga Group2")){url = "http://live.mystocks.co.ke/graphs/UNGA.Chart?r=740";}
        else if(choice.equals("Unga Group3")){url = "http://live.mystocks.co.ke/graphs/UNGA.Chart?r=1100";}
        else if(choice.equals("Bamburi Cement1")){url = "http://live.mystocks.co.ke/graphs/BAMB.Chart?r=370";}
        else if(choice.equals("Bamburi Cement2")){url = "http://live.mystocks.co.ke/graphs/BAMB.Chart?r=740";}
        else if(choice.equals("Bamburi Cement3")){url = "http://live.mystocks.co.ke/graphs/BAMB.Chart?r=1100";}
        else if(choice.equals("Crown berger (K)1")){url = "http://live.mystocks.co.ke/graphs/BERG.Chart?r=370";}
        else if(choice.equals("Crown berger (K)2")){url = "http://live.mystocks.co.ke/graphs/BERG.Chart?r=740";}
        else if(choice.equals("Crown berger (K)3")){url = "http://live.mystocks.co.ke/graphs/BERG.Chart?r=1100";}
        else if(choice.equals("E.A. Portland Cement1")){url = "http://live.mystocks.co.ke/graphs/PORT.Chart?r=370";}
        else if(choice.equals("E.A. Portland Cement2")){url = "http://live.mystocks.co.ke/graphs/PORT.Chart?r=740";}
        else if(choice.equals("E.A. Portland Cement3")){url = "http://live.mystocks.co.ke/graphs/PORT.Chart?r=1100";}
        else if(choice.equals("K.P.L.C1")){url = "http://live.mystocks.co.ke/graphs/KPLC.Chart?r=370";}
        else if(choice.equals("K.P.L.C2")){url = "http://live.mystocks.co.ke/graphs/KPLC.Chart?r=740";}
        else if(choice.equals("K.P.L.C3")){url = "http://live.mystocks.co.ke/graphs/KPLC.Chart?r=1100";}
        else if(choice.equals("Total Kenya1")){url = "http://live.mystocks.co.ke/graphs/TOTL.Chart?r=370";}
        else if(choice.equals("Total Kenya2")){url = "http://live.mystocks.co.ke/graphs/TOTL.Chart?r=740";}
        else if(choice.equals("Total Kenya3")){url = "http://live.mystocks.co.ke/graphs/TOTL.Chart?r=1100";}
        else if(choice.equals("Eveready E.A.1")){url = "http://live.mystocks.co.ke/graphs/EVRD.Chart?r=370";}
        else if(choice.equals("Eveready E.A.2")){url = "http://live.mystocks.co.ke/graphs/EVRD.Chart?r=740";}
        else if(choice.equals("Eveready E.A.3")){url = "http://live.mystocks.co.ke/graphs/EVRD.Chart?r=1100";}
        else if(choice.equals("Kengen1")){url = "http://live.mystocks.co.ke/graphs/KEGN.Chart?r=370";}
        else if(choice.equals("Kengen2")){url = "http://live.mystocks.co.ke/graphs/KEGN.Chart?r=740";}
        else if(choice.equals("Kengen3")){url = "http://live.mystocks.co.ke/graphs/KEGN.Chart?r=1100";}
        a = new canvas();
        back = new Command("Back");
        f = new Form();
        f.addComponent(a.getchart(url));
        f.addCommand(back);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectindustrialandappliedstockanalysis a = new selectindustrialandappliedstockanalysis();
            }
        });
        f.setScrollableY(true);
        f.setScrollableX(true);
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}