import javax.swing.*;

public class Main {
    public static void main(String args[]){
        Simulation simulation = new Simulation();
        SimPanel panel = new SimPanel(simulation);

        JFrame frame = new JFrame("Solar System");
        frame.add(panel);
        frame.setSize(1000,1000);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setVisible(true);

        //simulation loop

         final double dt = 0.03;

         while (true){
             simulation.update(dt);

             panel.repaint();

             try{
                 Thread.sleep(16);

             }catch(InterruptedException e){
                 e.printStackTrace();
             }
         }

    }
}