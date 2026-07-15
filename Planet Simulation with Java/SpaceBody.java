import java.awt.*;
import java.util.ArrayList;

public class SpaceBody {
    public String name;
    public double mass;
    public double radius;

    public Vectors2D position;
    public Vectors2D velocity;
    public Vectors2D acceleration;

    public Color color;

    public ArrayList<Vectors2D> trail;

    //Constructor
    public SpaceBody(
              String name,
              double mass,
              double radius,
              Vectors2D position,
              Vectors2D velocity,
              Color color
    ){
        this.name = name;
        this.mass = mass;
        this.radius = radius;

        this.position = position;
        this.velocity = velocity;

        this.acceleration = new Vectors2D(0,0);
        this.color = color;
         this.trail = new ArrayList<>();
    }

}
