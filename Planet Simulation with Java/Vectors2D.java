import java.util.Vector;

public class Vectors2D {
    public double x;
    public double y;

    public Vectors2D(double x, double y){
        this.x = x;
        this.y = y;
    }
    public Vectors2D add(Vectors2D vector){
        double newx;
        double newy;

        newx = this.x + vector.x;
        newy = this.y + vector.y;

        Vectors2D newVector = new Vectors2D(newx, newy);
        return newVector;
    }

    public Vectors2D subtract(Vectors2D vector){
        double newx;
        double newy;

        newx = this.x - vector.x;
        newy = this.y - vector.y;

        Vectors2D newVector = new Vectors2D(newx, newy);
        return newVector;
    }
    public Vectors2D multiply(double scalar){
        double newx = this.x * scalar;
        double newy = this.y * scalar;

        return new Vectors2D(newx, newy);
    }

    public Vectors2D divide(double scalar){
        double newx = this.x /scalar;
        double newy = this.y /scalar;

        return new Vectors2D(newx, newy);
    }

    public double magnitude (){
        double magn = Math.sqrt(x*x + y*y);
        return magn;
    }

    public Vectors2D normalize(){
        double mag = magnitude();

        if (mag == 0){
            return new Vectors2D(0,0);
        }
        return divide(mag);
    }


}
