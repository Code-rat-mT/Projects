import java.awt.*;
import java.util.ArrayList;
import java.util.Random;

public class Simulation {

    public ArrayList <SpaceBody> bodies;

    private PhysicsEngine physicsEngine;

    public Simulation(){
        bodies  = new ArrayList<>();
        physicsEngine = new PhysicsEngine();

        initializeBodies();
    }

    //Scaling
    //AU ratios
    private void initializeBodies(){
        SpaceBody sun = new SpaceBody(
                         "Sun",
                          1,
                          50,
                          new Vectors2D(0,0),
                          new Vectors2D(0,0), // fixed
                          Color.YELLOW
        );
        SpaceBody earth = new SpaceBody(
                "Earth",
                0.000003,
                10,
                new Vectors2D(1,0),
                new Vectors2D(0,1), // fixed
                Color.BLUE
        );
        SpaceBody mercury = new SpaceBody(
                "Mercury",
                0.00000032,
                8,
                new Vectors2D(0.39,0),
                new Vectors2D(0,1.6), // fixed
                Color.GRAY
        );

        SpaceBody venus = new SpaceBody(
                "Venus",
                0.0000024,
                10,
                new Vectors2D(0.72,0),
                new Vectors2D(0,1.18), // fixed
                Color.ORANGE
        );
        SpaceBody mars = new SpaceBody(
                "Mars",
                0.0000032,
                8,
                new Vectors2D(1.52,0),
                new Vectors2D(0,0.81), // fixed
                Color.RED
        );

        SpaceBody jupiter = new SpaceBody(
                "Jupiter",
                0.000954,
                18,
                new Vectors2D(5.20,0),
                new Vectors2D(0,0.438), // fixed
                new Color(210, 180, 140)
        );

        SpaceBody saturn = new SpaceBody(
                "Saturn",
                0.000286,
                15,
                new Vectors2D(9.58,0),
                new Vectors2D(0,0.323), // fixed
                new Color(238, 232, 205)
        );

        SpaceBody neptune = new SpaceBody(
                "Neptune",
                0.0000515,
                13,
                new Vectors2D(30.07,0),
                new Vectors2D(0,0.182), // fixed
                new Color(65, 105, 225)
        );


        bodies.add(sun);
        bodies.add(mercury);
        bodies.add(earth);
        bodies.add(venus);
        bodies.add(mars);
        bodies.add(jupiter);
        bodies.add(saturn);
        bodies.add(neptune);

        Random rand = new Random();
        int numberofAsteriods = 150;

        for (int i = 0; i<numberofAsteriods; i++){
            double r = 2.2 + (rand.nextDouble() * 1.0);
            double angle = rand.nextDouble() * 2 * Math.PI;

            double posX = r * Math.cos(angle);
            double posY = r * Math.sin(angle);

            double orbitalVelocityMagn = Math.sqrt(1/r);

            double velX = -Math.sin(angle)*orbitalVelocityMagn;
            double velY = Math.cos(angle)*orbitalVelocityMagn;

            double asteroidMass = 1e-12;
            int visualSize = 3;

            SpaceBody asteriod = new SpaceBody(
                    "A",
                    asteroidMass,
                    visualSize,
                    new Vectors2D(posX, posY),
                    new Vectors2D(velX, velY),
                    Color.LIGHT_GRAY
            );
             bodies.add(asteriod);
        }

    }
    public void update(double dt){
        synchronized (bodies) {
            physicsEngine.update(bodies, dt);
        }
    }

}
