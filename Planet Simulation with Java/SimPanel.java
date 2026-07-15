import java.awt.*;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.*;
public class SimPanel extends JPanel {
    private Simulation simulation;
    public Camera camera;

    private static class Star {
        int screenX;
        int screenY;
        int brightness; // Used to create realistic variation in twinkling/depth

        Star(int x, int y, int b) {
            this.screenX = x;
            this.screenY = y;
            this.brightness = b;
        }
    }

    private ArrayList<Star> stars;

    public SimPanel(Simulation simulation) {
        this.camera = new Camera();
        this.simulation = simulation;
        setBackground(Color.BLACK);

        stars = new ArrayList<>();
        Random rand = new Random();
        int totalStars = 400;
        for (int i = 0; i < totalStars; i++) {
            int sx = rand.nextInt(2500) - 500;
            int sy = rand.nextInt(2500) - 500;
            int brightness = 100 + rand.nextInt(155);
            stars.add(new Star(sx, sy, brightness));
        }

        this.addMouseWheelListener(new MouseWheelListener() {
            @Override
            public void mouseWheelMoved(MouseWheelEvent e) {
                int clicks = e.getWheelRotation();

                double zoomspeed = camera.zoom * 0.12;

                if (clicks<0){
                    camera.adjustZoom(zoomspeed);
                }else{
                    camera.adjustZoom(-zoomspeed);
                }
                repaint();
            }
        });
    }
    //paint the panel

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        for (Star star : stars) {
            g2.setColor(new Color(star.brightness, star.brightness, star.brightness));


            int starSize = (star.brightness > 220) ? 2 : 1;
            g2.fillRect(star.screenX, star.screenY, starSize, starSize);
        }

        synchronized (simulation.bodies) {

            for (SpaceBody body : simulation.bodies) {
                 double perspective = camera.getDepthScale(body.position.y);

                if (!body.name.startsWith("A")) {
                    g2.setColor(body.color);
                    for (Vectors2D point : body.trail) {
                        int tx = camera.worldToScreenX(point.x, getWidth());
                        int ty = camera.worldToScreenY(point.y, getHeight());

                        g2.fillOval(tx, ty, 2, 2);
                    }
                }

                int x = camera.worldToScreenX(body.position.x, getWidth());
                int y = camera.worldToScreenY(body.position.y, getHeight());

                int radius = (int) body.radius;

                g2.setColor(body.color);

                g2.fillOval(x - radius / 2, y - radius / 2, radius, radius); //centering

                //drawing the label

                if (body.name.equals("Saturn")){
                    int ringWidth = (int) (radius * 2.2);
                    int ringHeight = (int) (ringWidth * camera.tilt);
                    g2.setColor(new Color(218, 160, 180));
                    g2.setStroke(new BasicStroke(2));
                    g2.drawOval(x - ringWidth/2, y - ringHeight/2, ringWidth, ringHeight);
                }
                g2.setColor(Color.WHITE);
                if (!body.name.startsWith("A")) {
                    g2.drawString(body.name,
                            x + 10, //offsetting the x - coord
                            y);
                }
            }
        }
    }
}