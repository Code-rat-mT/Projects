import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Graph extends JFrame {
    GraphPanel graph;
    JTextField first, second, third, equation;
    JLabel firstC, secondC, thirdC;
    JButton submit;
    final int WIDTH = 700;
    final int HEIGHT = 700;

    public Graph() {
        this.setTitle("Graph");
        this.setSize(WIDTH, HEIGHT);
        this.setResizable(false);
    }

    public void createAndShowGUI() {

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(null);
        graph = new GraphPanel();
        graph.setBounds(0, 0, this.getWidth(), HEIGHT);
        this.getContentPane().add(graph);
        setVisible(true);
        System.out.println(this.getWidth() + "X" + this.getHeight());
    }

    public static void main(String args[]) {
        (new Graph()).createAndShowGUI();
    }


    private class GraphPanel extends JPanel {
        int WIDTH = 600;
        int HEIGHT = 500;
        final int MAX_POINTS = 100;
        final int SCALE_FACTOR = 5;
        final int STEP = 50;

        int xValues[];
        int yValues[];
        double constants[];
        boolean showGrid = false;
        Point center;
        InputPanel input;
        GraphPanel() {
            input = new InputPanel();
            setPreferredSize(new Dimension(WIDTH, HEIGHT));
            setBackground(Color.black);
            center = new Point(WIDTH / 2, HEIGHT / 2);
            xValues = new int[MAX_POINTS];
            yValues = new int[MAX_POINTS];
            constants = new double[3];
            setLayout(null);
            input.setBounds(0, 620, 700,50);
            fillX(xValues);
            fillY(xValues, yValues, constants);
            add(input);
        }

        GraphPanel(double a, double b, double c) {
            constants[0] = -a;
            constants[1] = -b;
            constants[2] = -c;
        }

        public void setConstants(double a, double b, double c) {
            constants[0] = -a;
            constants[1] = -b;
            constants[2] = -c;
            fillX(xValues);
            fillY(xValues, yValues, constants);
            repaint();
        }

        public void paint(Graphics g) {

            super.paint(g);
            Graphics2D g2 = (Graphics2D) g;
            // draw the x and y axes
            g2.setFont(new Font("Ink Free", Font.ITALIC, 20));
            String coeffi = "y = " + -constants[0] + "x^2 + " + -constants[1] + "x + " + -constants[2];
            HEIGHT = this.getHeight();
            WIDTH = this.getWidth();
            g2.setPaint(Color.white);
            g2.drawString(coeffi, 50, 50);
            //draw a grid system
            if (showGrid) {
                for (int i = 0; i < (HEIGHT * 2); i += STEP) {
                    g2.drawLine(i, 0, i, HEIGHT);
                }
                for (int i = 0; i < (WIDTH * 2); i += STEP) {
                    g2.drawLine(0, i, WIDTH, i);
                }
            }

            //draw the axes
            g2.setStroke(new BasicStroke(4));
            g2.setPaint(new Color(67, 77, 100));
            g2.drawLine(WIDTH / 2, 0, WIDTH / 2, HEIGHT);
            g2.drawLine(0, HEIGHT / 2, WIDTH, HEIGHT / 2);
            //draw the quadratic graph
            g2.setPaint(new Color(54, 250, 42));
            g2.setStroke(new BasicStroke(2));
            for (int i = 0; i < MAX_POINTS - 1; i++) {
                g2.drawLine((xValues[i] * SCALE_FACTOR + WIDTH / 2), yValues[i] + HEIGHT / 2,
                        (xValues[i + 1] * SCALE_FACTOR + WIDTH / 2), yValues[i + 1] + HEIGHT / 2);
            }
        }

        public void fillX(int[] xValues) {
            for (int i = 0; i < MAX_POINTS; i++) {
                xValues[i] = i - MAX_POINTS / 2;
            }
        }

        public void fillY(int[] xValues, int yValues[], double[] constants) {
            for (int i = 0; i < MAX_POINTS; i++) {
                yValues[i] = (int) (constants[0] * Math.pow(xValues[i], 2) + constants[1] * xValues[i] + constants[2]);
            }
        }

        public void isShowGrid(boolean show) {
            showGrid = show;
            repaint();
        }

        private class InputPanel extends JPanel implements ActionListener {
            final int WIDTH = 500;
            final int HEIGHT = 50;

            public InputPanel() {
                Font font = new Font("Ink Free", Font.BOLD, 20);
                equation = new JTextField( "y=0x^2+5x-10", 10);
                first = new JTextField("0.0", 3);
                second = new JTextField("0.0", 3);
                third = new JTextField("0.0", 3);
                firstC = new JLabel("a: ");
                secondC = new JLabel("b: ");
                thirdC = new JLabel("c: ");
                submit = new JButton("Submit");

                equation.setFont(font);
                first.setFont(font);
                second.setFont(font);
                third.setFont(font);

                first.setEditable(false);
                second.setEditable(false);
                third.setEditable(false);

                firstC.setFont(new Font("Ink Free", Font.BOLD, 15));
                secondC.setFont(new Font("Ink Free", Font.BOLD, 15));
                thirdC.setFont(new Font("Ink Free", Font.BOLD,  15));
                submit.addActionListener(this);

                setPreferredSize(new Dimension(WIDTH, HEIGHT));
                JButton show = new JButton("Show Grid");
                show.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        if (showGrid) {
                            isShowGrid(false);
                            show.setText("Show Grid");
                        } else {
                            isShowGrid(true);
                            show.setText("Hide Grid");
                        }
                    }
                });
                add(equation);
                add(firstC);
                add(first);
                add(secondC);
                add(second);
                add(thirdC);
                add(third);
                add(submit);
                add(show);
            }


            public double getA() {
                return Double.parseDouble(first.getText());
            }

            public double getB() {
                return Double.parseDouble(second.getText());
            }

            public double getC() {
                return Double.parseDouble(third.getText());
            }

            public void changeBackground(Color background) {
                this.setBackground(background);
            }

            @Override
            public void actionPerformed(ActionEvent e) {
                boolean aset=false, bset=false, cset=false, powerset=false;
                String equat=equation.getText();
                String av, bv, cv;
                if(!equation.getText().equals("")){

                    String value= equation.getText();
                    av=value.substring(value.indexOf("=")+1,value.indexOf("x"));
                    value=value.substring(value.indexOf("^")+2);
                    bv=value.substring(value.indexOf("2")+1, value.indexOf("x"));
                    value=value.substring(value.indexOf("x")+1);
                    cv=value;

                    first.setText(""+av);
                    second.setText(""+bv);
                    third.setText(""+cv);
                }

                setConstants(Double.parseDouble(first.getText()),
                        Double.parseDouble(second.getText()),
                        Double.parseDouble(third.getText()));
            }
        }
    }

}




