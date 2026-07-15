public class Camera {
    public double x = 0;
    public double y = 0;

    public double zoom = 60;
    public double tilt = 0.45;

    public void adjustZoom(double amount){
        this.zoom +=amount;

        if (this.zoom < 5) this.zoom = 5;
        if (this.zoom > 600) this.zoom = 600;
    }
    public int worldToScreenX(double worldX, int width){
        return (int)((worldX - x)  * zoom + width/2);
    }
    public int worldToScreenY(double worldY, int height){
        return (int)(((worldY - y) * tilt) * zoom + height/2);
    }

    public double getDepthScale(double worldY){
        double relativeY = worldY - y;
        double perspectiveIntensity = 0.15;

        return 1.0 + (relativeY * perspectiveIntensity);
    }
}
