import javax.microedition.lcdui.Canvas;
import javax.microedition.lcdui.Graphics;
import javax.microedition.io.Connector;
import java.io.DataInputStream;
import com.sun.lwuit.Image;
import com.sun.lwuit.Label;
class canvas extends Canvas
{
    private Label label;
    private Image chart;
    private DataInputStream is;
    public void paint(Graphics g)
    {}
    public Label getchart(String url)
    {
        is = null;
        chart = null;
        label = null;
        try
        {
            is = Connector.openDataInputStream(url);
            chart = Image.createImage(is);
            is.close();
        }
        catch(Exception e){}
        label = new Label();
        label.setPreferredH(getHeight());
        label.setPreferredW(getWidth());
        if(getHeight() <= getWidth()){}
        else if(getWidth() < getHeight())
        {
           chart = chart.rotate(90);
        }
        chart = chart.scaled(label.getPreferredW(),label.getPreferredH());
        label.setIcon(chart);
        label.setIsScrollVisible(true);
        is = null;
        chart = null;
        return label;
    }
}