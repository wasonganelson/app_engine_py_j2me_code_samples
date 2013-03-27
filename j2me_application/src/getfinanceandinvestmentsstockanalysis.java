import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getfinanceandinvestmentsstockanalysis implements Runnable
{
    private canvas a;
    private String url;
    private Form f;
    private Command back;
    private String choice;
    public getfinanceandinvestmentsstockanalysis(String choice)
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
        if(choice.equals("Barclays Bank1")){url = "http://live.mystocks.co.ke/graphs/BBK.Chart?r=370";}
        else if(choice.equals("Barclays Bank2")){url = "http://live.mystocks.co.ke/graphs/BBK.Chart?r=740";}
        else if(choice.equals("Barclays Bank3")){url = "http://live.mystocks.co.ke/graphs/BBK.Chart?r=1100";}
        else if(choice.equals("CFC Stanbic Bank1")){url = "http://live.mystocks.co.ke/graphs/CFC.Chart?r=370";}
        else if(choice.equals("CFC Stanbic Bank2")){url = "http://live.mystocks.co.ke/graphs/CFC.Chart?r=740";}
        else if(choice.equals("CFC Stanbic Bank3")){url = "http://live.mystocks.co.ke/graphs/CFC.Chart?r=1100";}
        else if(choice.equals("CFC Insurance1")){url = "http://live.mystocks.co.ke/graphs/CFCI.Chart?r=370";}
        else if(choice.equals("CFC Insurance2")){url = "http://live.mystocks.co.ke/graphs/CFCI.Chart?r=740";}
        else if(choice.equals("CFC Insurance3")){url = "http://live.mystocks.co.ke/graphs/CFCI.Chart?r=1100";}
        else if(choice.equals("Housing Finance1")){url = "http://live.mystocks.co.ke/graphs/HFCK.Chart?r=370";}
        else if(choice.equals("Housing Finance2")){url = "http://live.mystocks.co.ke/graphs/HFCK.Chart?r=740";}
        else if(choice.equals("Housing Finance3")){url = "http://live.mystocks.co.ke/graphs/HFCK.Chart?r=1100";}
        else if(choice.equals("Centum Investments1")){url = "http://live.mystocks.co.ke/graphs/ICDC.Chart?r=370";}
        else if(choice.equals("Centum Investments2")){url = "http://live.mystocks.co.ke/graphs/ICDC.Chart?r=740";}
        else if(choice.equals("Centum Investments3")){url = "http://live.mystocks.co.ke/graphs/ICDC.Chart?r=1100";}
        else if(choice.equals("Kenya Commercial Bank1")){url = "http://live.mystocks.co.ke/graphs/KCB.Chart?r=370";}
        else if(choice.equals("Kenya Commercial Bank2")){url = "http://live.mystocks.co.ke/graphs/KCB.Chart?r=740";}
        else if(choice.equals("Kenya Commercial Bank3")){url = "http://live.mystocks.co.ke/graphs/KCB.Chart?r=1100";}
        else if(choice.equals("National Bank1")){url = "http://live.mystocks.co.ke/graphs/NBK.Chart?r=370";}
        else if(choice.equals("National Bank2")){url = "http://live.mystocks.co.ke/graphs/NBK.Chart?r=740";}
        else if(choice.equals("National Bank3")){url = "http://live.mystocks.co.ke/graphs/NBK.Chart?r=1100";}
        else if(choice.equals("Pan African Insurance1")){url = "http://live.mystocks.co.ke/graphs/PAFR.Chart?r=370";}
        else if(choice.equals("Pan African Insurance2")){url = "http://live.mystocks.co.ke/graphs/PAFR.Chart?r=740";}
        else if(choice.equals("Pan African Insurance3")){url = "http://live.mystocks.co.ke/graphs/PAFR.Chart?r=1100";}
        else if(choice.equals("Diamond Trust Bank1")){url = "http://live.mystocks.co.ke/graphs/DTK.Chart?r=370";}
        else if(choice.equals("Diamond Trust Bank2")){url = "http://live.mystocks.co.ke/graphs/DTK.Chart?r=740";}
        else if(choice.equals("Diamond Trust Bank3")){url = "http://live.mystocks.co.ke/graphs/DTK.Chart?r=1100";}
        else if(choice.equals("Jubilee Insurance1")){url = "http://live.mystocks.co.ke/graphs/JUB.Chart?r=370";}
        else if(choice.equals("Jubilee Insurance2")){url = "http://live.mystocks.co.ke/graphs/JUB.Chart?r=740";}
        else if(choice.equals("Jubilee Insurance3")){url = "http://live.mystocks.co.ke/graphs/JUB.Chart?r=1100";}
        else if(choice.equals("Standard Chartered Bank1")){url = "http://live.mystocks.co.ke/graphs/SCBK.Chart?r=370";}
        else if(choice.equals("Standard Chartered Bank2")){url = "http://live.mystocks.co.ke/graphs/SCBK.Chart?r=740";}
        else if(choice.equals("Standard Chartered Bank3")){url = "http://live.mystocks.co.ke/graphs/SCBK.Chart?r=1100";}
        else if(choice.equals("NIC Bank1")){url = "http://live.mystocks.co.ke/graphs/NIC.Chart?r=370";}
        else if(choice.equals("NIC Bank2")){url = "http://live.mystocks.co.ke/graphs/NIC.Chart?r=740";}
        else if(choice.equals("NIC Bank3")){url = "http://live.mystocks.co.ke/graphs/NIC.Chart?r=1100";}
        else if(choice.equals("Equity Bank1")){url = "http://live.mystocks.co.ke/graphs/EQTY.Chart?r=370";}
        else if(choice.equals("Equity Bank2")){url = "http://live.mystocks.co.ke/graphs/EQTY.Chart?r=740";}
        else if(choice.equals("Equity Bank3")){url = "http://live.mystocks.co.ke/graphs/EQTY.Chart?r=1100";}
        else if(choice.equals("Olympia Capital1")){url = "http://live.mystocks.co.ke/graphs/OCH.Chart?r=370";}
        else if(choice.equals("Olympia Capital2")){url = "http://live.mystocks.co.ke/graphs/OCH.Chart?r=740";}
        else if(choice.equals("Olympia Capital3")){url = "http://live.mystocks.co.ke/graphs/OCH.Chart?r=1100";}
        else if(choice.equals("Co-operative Bank1")){url = "http://live.mystocks.co.ke/graphs/COOP.Chart?r=370";}
        else if(choice.equals("Co-operative Bank2")){url = "http://live.mystocks.co.ke/graphs/COOP.Chart?r=740";}
        else if(choice.equals("Co-operative Bank3")){url = "http://live.mystocks.co.ke/graphs/COOP.Chart?r=1100";}
        else if(choice.equals("Kenya Re-Insurance1")){url = "http://live.mystocks.co.ke/graphs/KNRE.Chart?r=370";}
        else if(choice.equals("Kenya Re-Insurance2")){url = "http://live.mystocks.co.ke/graphs/KNRE.Chart?r=740";}
        else if(choice.equals("Kenya Re-Insurance3")){url = "http://live.mystocks.co.ke/graphs/KNRE.Chart?r=1100";}
        a = new canvas();
        back = new Command("Back");
        f = new Form();
        f.addComponent(a.getchart(url));
        f.addCommand(back);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectfinanceandinvestmentsstockanalysis a = new selectfinanceandinvestmentsstockanalysis();
            }
        });
        f.setScrollableY(true);
        f.setScrollableX(true);
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}