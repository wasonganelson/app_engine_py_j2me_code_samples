import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.Form;
import com.sun.lwuit.Command;
import com.sun.lwuit.animations.CommonTransitions;
import com.sun.lwuit.events.ActionListener;
import com.sun.lwuit.events.ActionEvent;
public class getcommercialandservicesstockanalysis implements Runnable
{
    private canvas a;
    private String url;
    private Form f;
    private Command back;
    private String choice;
    public getcommercialandservicesstockanalysis(String choice)
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
        if(choice.equals("AccessKenya1")){url = "http://live.mystocks.co.ke/graphs/ACCS.Chart?r=370";}
        else if(choice.equals("AccessKenya2")){url = "http://live.mystocks.co.ke/graphs/ACCS.Chart?r=740";}
        else if(choice.equals("AccessKenya3")){url = "http://live.mystocks.co.ke/graphs/ACCS.Chart?r=1100";}
        else if(choice.equals("Marshalls E.A.1")){url = "http://live.mystocks.co.ke/graphs/MASH.Chart?r=370";}
        else if(choice.equals("Marshalls E.A.2")){url = "http://live.mystocks.co.ke/graphs/MASH.Chart?r=740";}
        else if(choice.equals("Marshalls E.A.3")){url = "http://live.mystocks.co.ke/graphs/MASH.Chart?r=1100";}
        else if(choice.equals("Car and General1")){url = "http://live.mystocks.co.ke/graphs/C%2526G.Chart?r=370";}
        else if(choice.equals("Car and General2")){url = "http://live.mystocks.co.ke/graphs/C%2526G.Chart?r=740";}
        else if(choice.equals("Car and General3")){url = "http://live.mystocks.co.ke/graphs/C%2526G.Chart?r=1100";}
        else if(choice.equals("Kenya Airways1")){url = "http://live.mystocks.co.ke/graphs/KQ.Chart?r=370";}
        else if(choice.equals("Kenya Airways2")){url = "http://live.mystocks.co.ke/graphs/KQ.Chart?r=740";}
        else if(choice.equals("Kenya Airways3")){url = "http://live.mystocks.co.ke/graphs/KQ.Chart?r=1100";}
        else if(choice.equals("CMC Holdings1")){url = "http://live.mystocks.co.ke/graphs/CMC.Chart?r=370";}
        else if(choice.equals("CMC Holdings2")){url = "http://live.mystocks.co.ke/graphs/CMC.Chart?r=740";}
        else if(choice.equals("CMC Holdings3")){url = "http://live.mystocks.co.ke/graphs/CMC.Chart?r=1100";}
        else if(choice.equals("Nation Media Group1")){url = "http://live.mystocks.co.ke/graphs/NMG.Chart?r=370";}
        else if(choice.equals("Nation Media Group2")){url = "http://live.mystocks.co.ke/graphs/NMG.Chart?r=740";}
        else if(choice.equals("Nation Media Group3")){url = "http://live.mystocks.co.ke/graphs/NMG.Chart?r=1100";}
        else if(choice.equals("TPS (Serena)1")){url = "http://live.mystocks.co.ke/graphs/TPSE.Chart?r=370";}
        else if(choice.equals("TPS (Serena)2")){url = "http://live.mystocks.co.ke/graphs/TPSE.Chart?r=740";}
        else if(choice.equals("TPS (Serena)3")){url = "http://live.mystocks.co.ke/graphs/TPSE.Chart?r=1100";}
        else if(choice.equals("ScanGroup1")){url = "http://live.mystocks.co.ke/graphs/SCAN.Chart?r=370";}
        else if(choice.equals("ScanGroup2")){url = "http://live.mystocks.co.ke/graphs/SCAN.Chart?r=740";}
        else if(choice.equals("ScanGroup3")){url = "http://live.mystocks.co.ke/graphs/SCAN.Chart?r=1100";}
        else if(choice.equals("Standard Group1")){url = "http://live.mystocks.co.ke/graphs/SGL.Chart?r=370";}
        else if(choice.equals("Standard Group2")){url = "http://live.mystocks.co.ke/graphs/SGL.Chart?r=740";}
        else if(choice.equals("Standard Group3")){url = "http://live.mystocks.co.ke/graphs/SGL.Chart?r=1100";}
        else if(choice.equals("Safaricom1")){url = "http://live.mystocks.co.ke/graphs/SCOM.Chart?r=370";}
        else if(choice.equals("Safaricom2")){url = "http://live.mystocks.co.ke/graphs/SCOM.Chart?r=740";}
        else if(choice.equals("Safaricom3")){url = "http://live.mystocks.co.ke/graphs/SCOM.Chart?r=1100";}
        else if(choice.equals("Uchumi Supermarket1")){url = "http://live.mystocks.co.ke/graphs/UCHM.Chart?r=370";}
        else if(choice.equals("Uchumi Supermarket2")){url = "http://live.mystocks.co.ke/graphs/UCHM.Chart?r=740";}
        else if(choice.equals("Uchumi Supermarket3")){url = "http://live.mystocks.co.ke/graphs/UCHM.Chart?r=1100";}
        a = new canvas();
        back = new Command("Back");
        f = new Form();
        f.addComponent(a.getchart(url));
        f.addCommand(back);
        f.addCommandListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                selectcommercialandservicesstockanalysis a = new selectcommercialandservicesstockanalysis();
            }
        });
        f.setScrollableY(true);
        f.setScrollableX(true);
        f.setTransitionInAnimator(CommonTransitions.createFade(500));
        f.show();
    }
}