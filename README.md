# Eye Break

The Eye Break Program helps prevent [computer vision syndrome](https://en.wikipedia.org/wiki/Computer_vision_syndrome) by reminding you to take breaks using the [20-20 rule](https://www.healthline.com/health/eye-health/20-20-20-rule). It darkens your screen brightness every 20 minutes for 20 seconds to remind you to take a break. The current version only works on macOS.

## Installation & Running

1. **Install `brightness`**

   Download and install the `brightness` command from [here](https://github.com/nriley/brightness).

2. **Run the following commands in the terminal**

   ```bash
   git clone https://github.com/mhdirnjbr/eye-break.git
   cd eye-break
   python eye_break.py
   ```

## Configuration
You can edit these values directly in the `eye_break.py` script:
   - `BREAK_INTERVAL`: Time between breaks in seconds. Default is 1200 seconds (20 minutes).
   - `BREAK_DURATION`: Duration of the break in seconds. Default is 20 seconds.
   - `LOW_BRIGHTNESS`: Brightness level during the break. Default is 0.1.
