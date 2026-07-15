import java.util.List;

public class PhysicsEngine {

    private final double G = 1.0;

    private static class State {
        Vectors2D position;
        Vectors2D velocity;
        double mass;

        State(Vectors2D p, Vectors2D v, double m) {
            this.position = p;
            this.velocity = v;
            this.mass = m;
        }
    }

    public void update(List<SpaceBody> bodies, double dt) {
        int n = bodies.size();
        if (n == 0) return;

        State[] initial = new State[n];


        for (int i = 0; i < n; i++) {
            SpaceBody b = bodies.get(i);
            initial[i] = new State(
                    new Vectors2D(b.position.x, b.position.y),
                    new Vectors2D(b.velocity.x, b.velocity.y),
                    b.mass
            );
        }

        //  Compute RK4 Coefficents (k1, k2, k3, k4)

        // k1:
        Vectors2D[] acc0 = computeAccelerations(initial);
        State[] k1 = derivatives(initial, acc0, dt);

        // k2:
        State[] step1 = step(initial, k1, 0.5);
        Vectors2D[] acc1 = computeAccelerations(step1);
        State[] k2 = derivatives(step1, acc1, dt);

        // k3:
        State[] step2 = step(initial, k2, 0.5);
        Vectors2D[] acc2 = computeAccelerations(step2);
        State[] k3 = derivatives(step2, acc2, dt);

        // k4:
        State[] step3 = step(initial, k3, 1.0);
        Vectors2D[] acc3 = computeAccelerations(step3);
        State[] k4 = derivatives(step3, acc3, dt);


        for (int i = 0; i < n; i++) {
            SpaceBody b = bodies.get(i);

            b.position = b.position.add(
                    k1[i].position
                            .add(k2[i].position.multiply(2.0))
                            .add(k3[i].position.multiply(2.0))
                            .add(k4[i].position)
                            .multiply(1.0 / 6.0)
            );

            b.velocity = b.velocity.add(
                    k1[i].velocity
                            .add(k2[i].velocity.multiply(2.0))
                            .add(k3[i].velocity.multiply(2.0))
                            .add(k4[i].velocity)
                            .multiply(1.0 / 6.0)
            );


            b.trail.add(new Vectors2D(b.position.x, b.position.y));
            if (b.trail.size() > 500) {
                b.trail.remove(0);
            }
        }
    }

    private Vectors2D[] computeAccelerations(State[] state) {
        int n = state.length;
        Vectors2D[] acc = new Vectors2D[n];

        for (int i = 0; i < n; i++) {
            acc[i] = new Vectors2D(0, 0);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;

                Vectors2D dir = state[j].position.subtract(state[i].position);
                double r = dir.magnitude();

                if (r < 0.01) r = 0.01;


                double force = (G * state[j].mass) / (r * r);

                Vectors2D a = dir.normalize().multiply(force);
                acc[i] = acc[i].add(a);
            }
        }
        return acc;
    }


    private State[] derivatives(State[] currentStep, Vectors2D[] acc, double dt) {
        int n = currentStep.length;
        State[] out = new State[n];

        for (int i = 0; i < n; i++) {
            Vectors2D dx = currentStep[i].velocity.multiply(dt);
            Vectors2D dv = acc[i].multiply(dt);

            out[i] = new State(dx, dv, currentStep[i].mass);
        }
        return out;
    }

    private State[] step(State[] base, State[] k, double scale) {
        int n = base.length;
        State[] out = new State[n];

        for (int i = 0; i < n; i++) {
            Vectors2D p = base[i].position.add(k[i].position.multiply(scale));
            Vectors2D v = base[i].velocity.add(k[i].velocity.multiply(scale));

            out[i] = new State(p, v, base[i].mass);
        }
        return out;
    }
}
