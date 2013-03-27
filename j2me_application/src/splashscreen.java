import com.sun.lwuit.Form;
import com.sun.lwuit.layouts.CoordinateLayout;
import com.sun.lwuit.Label;
import com.sun.lwuit.plaf.UIManager;
import com.sun.lwuit.util.Resources;
public class splashscreen
{
    private Form f;
    private canvas a;
    private Label label;
    public splashscreen()
    {
        try
        {
            Resources r = Resources.open("/res/splash.res");
            UIManager.getInstance().setThemeProps(r.getTheme(r.getThemeResourceNames()[0]));
        }
        catch (java.lang.Exception e){}
        f = new Form();
        a=new canvas();
        f.setLayout(new CoordinateLayout(a.getWidth(),a.getHeight()));
        label=new Label("");
        label.setX(a.getWidth()/11*5);
        label.setY(0);
        label.setPreferredW(a.getWidth()/2);
        label.setPreferredH(a.getHeight()/2);
        f.addComponent(label);
        f.show();
    }
}