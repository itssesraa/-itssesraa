#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;
int main() {
    // Bomber coordinates from the original Lab 3 case study, t = 0..12.
    const int MAX_TIME = 12;
    const double bomberX[MAX_TIME + 1] =
        {80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180};
    const double bomberY[MAX_TIME + 1] =
        {0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17};
    // Modified assumptions:
    const double fighterSpeed = 25.0; // km per minute
    const int directionUpdateInterval = 2; // minutes
    const double catchDistance = 8.0; // km
    double fighterX = 0.0;
    double fighterY = 50.0;
    double headingX = 0.0, headingY = 0.0;
    cout << fixed << setprecision(2);
    cout << "Modified Pursuit Problem Simulation\n";
    cout << "Speed = " << fighterSpeed << " km/min, direction update = every "
         << directionUpdateInterval << " min, catch distance = "
         << catchDistance << " km\n\n";
    cout << "t\tFighter X\tFighter Y\tBomber X\tBomber Y\tDistance\n";
    for (int t = 0; t <= MAX_TIME; ++t) {
        double dx = bomberX[t] - fighterX;
        double dy = bomberY[t] - fighterY;
        double distance = sqrt(dx * dx + dy * dy);
        cout << t << "\t" << fighterX << "\t\t" << fighterY << "\t\t"
             << bomberX[t] << "\t\t" << bomberY[t] << "\t\t"
             << distance << "\n";
        if (distance <= catchDistance) {
            cout << "\nRESULT: Fighter catches the bomber at t = " << t
                 << " minutes.\n";
            cout << "Distance at interception = " << distance << " km.\n";
            return 0;
        }
        if (t == MAX_TIME) break;
        // Change heading only at t = 0, 2, 4, 6, ... .
        // The current heading is held constant during the next minute.
        if (t % directionUpdateInterval == 0) {
            double magnitude = sqrt(dx * dx + dy * dy);
            if (magnitude > 0.0) {
                headingX = dx / magnitude;
                headingY = dy / magnitude;
            }
        }

        fighterX += fighterSpeed * headingX;
        fighterY += fighterSpeed * headingY;
    }

    cout << "\nRESULT: Bomber escapes; no interception within "
         << MAX_TIME << " minutes.\n";
    return 0;
}
