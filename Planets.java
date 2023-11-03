import javax.swing.*;
import java.awt.*;

public class Planets extends JPanel implements Runnable {
    int WIDTH=800;
    int HEIGHT=800;
    final int SUN_RADIUS=100;

    final int MERCURY_ORBIT=150;
    final int MERCURY_RADIUS=10;

    final int VENUS_ORBIT=210;
    final int VENUS_RADIUS=28;

    final int EARTH_RADIUS=30;
    final int EARTH_ORBIT=270;

    final int MARS_RADIUS=15;
    final int MARS_ORBIT= 340;

    final int JUPITER_RADIUS=50;
    final int JUPITER_ORBIT= 420;

    final int SUTURN_ORBIT= 520;
    final int SUTURN_RADIUS= 40;
    final int SUTURN_RING_RADIUS= 55;

    final int URANUS_ORBIT=600;
    final int URANUS_RADIUS=20;

    final int NEPTUNE_ORBIT= 700;
    final int NEPTUNE_RADIUS= 35;

    final int MAX_ANGLE=360;
    final int MERCURY_SPEED=15;
    final int VERNUS_SPEED=13;
    final int EARTH_SPEED=9;
    final int MARS_SPEED= 7;
    final int JUPITER_SPEED=5;
    final int SUTURN_SPEED=3;
    final int URANUS_SPEED=2;
    final int NEPTUNE_SPEED=1;


    boolean running =true;
    //starting points for the planet posititions
    int mecAngle=0;
    int venAngle=0;
    int earthAngle=0;
    int marsAngle=60;
    int jupAngle=200;
    int sutAngle=30;
    int urAngle =0;
    int neptAngle=120;
    String planets[]={"Mercury", "Venus", "Earth","Mars", "Jupiter", "Saturn",
            "Uranus","Neptune"};
    Font font;
    Point center;
    Point currentPosition;
    Point prevPosition;
    public Planets(){
        this.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        center = new Point(WIDTH/2, HEIGHT/2);
        currentPosition= new Point(0,0);
        prevPosition=new Point(0,0);
        font = new Font("Ink Free", Font.PLAIN, 14);
        this.setBackground(Color.black);
        Thread thread = new Thread(this, "myThread");
        thread.start();
    }
    public void paint(Graphics g){
        super.paint(g);
        Graphics2D g2= (Graphics2D)g;
        WIDTH=this.getWidth();
        HEIGHT= this.getHeight();
        center = new Point(WIDTH/2, HEIGHT/2);
        g2.setFont(new Font("Ink Free", Font.PLAIN, 40));

        g2.drawLine(center.x, 0, center.x, HEIGHT);
        g2.drawLine(0, center.y, WIDTH, center.y);

        g2.setPaint(Color.orange);
        g2.fillOval(center.x-SUN_RADIUS/2, center.y-SUN_RADIUS/2, SUN_RADIUS, SUN_RADIUS);
        //use one font for the rest of the planets
        g2.setFont(font);

        g2.drawOval(center.x-MERCURY_ORBIT/2
                ,center.y-MERCURY_ORBIT/2, MERCURY_ORBIT, MERCURY_ORBIT);

        g2.drawOval(center.x-VENUS_ORBIT/2
                ,center.y-VENUS_ORBIT/2, VENUS_ORBIT, VENUS_ORBIT);

        g2.drawOval(center.x-EARTH_ORBIT/2
                ,center.y-EARTH_ORBIT/2, EARTH_ORBIT, EARTH_ORBIT);

        g2.drawOval(center.x-MARS_ORBIT/2
                ,center.y-MARS_ORBIT/2, MARS_ORBIT, MARS_ORBIT);

        g2.drawOval(center.x-JUPITER_ORBIT/2
                ,center.y-JUPITER_ORBIT/2, JUPITER_ORBIT, JUPITER_ORBIT);

        g2.drawOval(center.x-SUTURN_ORBIT/2
                ,center.y-SUTURN_ORBIT/2, SUTURN_ORBIT, SUTURN_ORBIT);

        g2.drawOval(center.x-URANUS_ORBIT/2
                ,center.y-URANUS_ORBIT/2, URANUS_ORBIT, URANUS_ORBIT);

        g2.drawOval(center.x-NEPTUNE_ORBIT/2
                ,center.y-NEPTUNE_ORBIT/2, NEPTUNE_ORBIT, NEPTUNE_ORBIT);



        int mecOriginX=(int)(MERCURY_ORBIT/2*Math.cos(Math.PI * mecAngle/180));
        int mecOriginY=(int)(MERCURY_ORBIT/2*Math.sin(Math.PI * mecAngle/180));

        int venOriginX=(int)(VENUS_ORBIT/2*Math.cos(Math.PI * venAngle/180));
        int venOriginY=(int)(VENUS_ORBIT/2*Math.sin(Math.PI * venAngle/180));

        int earthOriginX=(int)(EARTH_ORBIT/2*Math.cos(Math.PI * earthAngle/180));
        int earthOriginY=(int)(EARTH_ORBIT/2*Math.sin(Math.PI *earthAngle/180));

        int marsOriginX=(int)(MARS_ORBIT/2*Math.cos(Math.PI * marsAngle/180));
        int marsOriginY=(int)(MARS_ORBIT/2*Math.sin(Math.PI * marsAngle/180));

        int jupOriginX=(int)(JUPITER_ORBIT/2*Math.cos(Math.PI * jupAngle/180));
        int jupOriginY=(int)(JUPITER_ORBIT/2*Math.sin(Math.PI * jupAngle/180));

        int sutOriginX=(int)(SUTURN_ORBIT/2*Math.cos(Math.PI * sutAngle/180));
        int sutOriginY=(int)(SUTURN_ORBIT/2*Math.sin(Math.PI * sutAngle/180));

        int urOriginX=(int)(URANUS_ORBIT/2*Math.cos(Math.PI * urAngle/180));
        int urOriginY=(int)(URANUS_ORBIT/2*Math.sin(Math.PI * urAngle/180));

        int neptOriginX=(int)(NEPTUNE_ORBIT/2*Math.cos(Math.PI * neptAngle/180));
        int neptOriginY=(int)(NEPTUNE_ORBIT/2*Math.sin(Math.PI * neptAngle/180));

        System.out.println(earthOriginX+": "+earthOriginY);

        g2.setPaint(Color.white);
        g2.drawString(planets[0],center.x+mecOriginX-MERCURY_RADIUS/2,
                center.y+mecOriginY-MERCURY_RADIUS/2);

        g2.setPaint(Color.gray);
        g2.fillOval(center.x+mecOriginX-MERCURY_RADIUS/2,
                center.y+mecOriginY-MERCURY_RADIUS/2,
                MERCURY_RADIUS, MERCURY_RADIUS);


        g2.setPaint(Color.white);
        g2.drawString(planets[1],center.x+venOriginX-VENUS_RADIUS/2,
                center.y+venOriginY-VENUS_RADIUS/2);

        g2.fillOval(center.x+venOriginX-VENUS_RADIUS/2,
                center.y+venOriginY-VENUS_RADIUS/2,
                VENUS_RADIUS, VENUS_RADIUS);

        g2.setPaint(Color.white);
        g2.drawString(planets[2], center.x+earthOriginX-EARTH_RADIUS/2,
                center.y+earthOriginY-EARTH_RADIUS/2 );
        g2.setPaint(Color.blue);
        g2.fillOval(center.x+earthOriginX-EARTH_RADIUS/2,
                center.y+earthOriginY-EARTH_RADIUS/2,
                EARTH_RADIUS, EARTH_RADIUS);

        g2.setPaint(Color.white);
        g2.drawString(planets[3], center.x+marsOriginX-MARS_RADIUS/2,
                center.y+marsOriginY-MARS_RADIUS/2);
        g2.setPaint(Color.red);
        g2.fillOval(center.x+marsOriginX-MARS_RADIUS/2,
                center.y+marsOriginY-MARS_RADIUS/2,
                MARS_RADIUS, MARS_RADIUS);
        g2.setPaint(Color.white);
        g2.drawString(planets[4], center.x+jupOriginX-JUPITER_RADIUS/2,
                center.y+jupOriginY-JUPITER_RADIUS/2);
        g2.setPaint(new Color(12, 41, 60));
        g2.fillOval(center.x+jupOriginX-JUPITER_RADIUS/2,
                center.y+jupOriginY-JUPITER_RADIUS/2,
                JUPITER_RADIUS, JUPITER_RADIUS);

        g2.setPaint(Color.white);
        g2.drawString(planets[5], center.x+sutOriginX-SUTURN_RADIUS/2,
                center.y+sutOriginY-SUTURN_RADIUS/2 );

        //draw the ring around saturn
        g2.setPaint(new Color(80, 18, 100));
        g2.setStroke(new BasicStroke(3));
        g2.drawOval(center.x+sutOriginX-SUTURN_RING_RADIUS/2,
                center.y+sutOriginY-SUTURN_RING_RADIUS/2,
                SUTURN_RING_RADIUS, SUTURN_RING_RADIUS);
        //draw the planet saturn
        g2.setPaint(new Color(100, 96, 18));
        g2.fillOval(center.x+sutOriginX-SUTURN_RADIUS/2,
                center.y+sutOriginY-SUTURN_RADIUS/2,
                SUTURN_RADIUS, SUTURN_RADIUS);
        g2.setStroke(new BasicStroke(1));

        g2.setPaint(Color.white);
        g2.drawString(planets[6],center.x+urOriginX-URANUS_RADIUS/2,
                center.y+urOriginY-URANUS_RADIUS/2
        );
        g2.setPaint(Color.cyan);
        g2.fillOval(center.x+urOriginX-URANUS_RADIUS/2,
                center.y+urOriginY-URANUS_RADIUS/2,
                URANUS_RADIUS, URANUS_RADIUS);


        g2.setPaint(Color.white);
        g2.drawString(planets[7],center.x+neptOriginX-NEPTUNE_RADIUS/2,
                center.y+neptOriginY-NEPTUNE_RADIUS/2
        );

        g2.setPaint(Color.magenta);
        g2.fillOval(center.x+neptOriginX-NEPTUNE_RADIUS/2,
                center.y+neptOriginY-NEPTUNE_RADIUS/2,
                NEPTUNE_RADIUS, NEPTUNE_RADIUS);


    }
    public void run(){
        while(running){

            mecAngle -=MERCURY_SPEED;
            venAngle +=VERNUS_SPEED;
            earthAngle-=EARTH_SPEED;
            marsAngle-=MARS_SPEED;
            jupAngle-=JUPITER_SPEED;
            sutAngle -=SUTURN_SPEED;
            urAngle -=URANUS_SPEED;
            neptAngle -=NEPTUNE_SPEED;

            if(earthAngle<=-MAX_ANGLE){
                earthAngle=0;
            }
            if(mecAngle <=-MAX_ANGLE){
                mecAngle=0;
            }
            if(venAngle >=MAX_ANGLE){
                venAngle=0;
            }
            if(marsAngle <=-MAX_ANGLE){
                marsAngle=0;
            }
            if(jupAngle <=-MAX_ANGLE){
                jupAngle=0;
            }
            if(sutAngle <=-MAX_ANGLE){
                sutAngle=0;
            }
            if(neptAngle<=-MAX_ANGLE){
                neptAngle=0;
            }
            if(urAngle<=-MAX_ANGLE){
                urAngle=0;
            }
            try{
                Thread.sleep(100);
            }catch(InterruptedException e){
                e.printStackTrace();
            }
            repaint();
        }
    }


    public static void main(String args[]){
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Planets");
        frame.setBackground(Color.black);
        frame.add(new Planets());
        frame.pack();
        // frame.setResizable(false);
        frame.setVisible(true);
    }
}
