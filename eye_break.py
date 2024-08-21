import time
import subprocess
import logging

BREAK_INTERVAL = 20 * 60
BREAK_DURATION = 20
LOW_BRIGHTNESS = 0.1


def get_current_brightness():
    try:
        result = subprocess.run(
            ["brightness", "-l"], capture_output=True, text=True, check=True
        )
        return float(result.stdout.split("brightness")[1].strip())
    except Exception as e:
        logging.error(f"Failed to get current brightness: {e}")
        return None


def set_brightness(level):
    try:
        if 0.0 <= level <= 1.0:
            subprocess.run(["brightness", str(level)], check=True)
        else:
            logging.error("Brightness level must be between 0.0 and 1.0")
    except Exception as e:
        logging.error(f"Failed to set brightness: {e}")


def take_break():
    try:
        while True:
            start_time = time.time()
            time.sleep(BREAK_INTERVAL)

            logging.info(
                "work period finished. time elapsed: %.2f seconds",
                time.time() - start_time,
            )

            original_brightness = get_current_brightness()
            if not original_brightness:
                logging.error("Could not retrieve original brightness. Skipping break.")
                continue

            set_brightness(LOW_BRIGHTNESS)

            start_time = time.time()
            time.sleep(BREAK_DURATION)
            logging.info(
                "break period finished. time elapsed: %.2f seconds",
                time.time() - start_time,
            )

            set_brightness(original_brightness)

    except KeyboardInterrupt:
        logging.info("program interrupted.")
        set_brightness(original_brightness)


def main():

    logging.basicConfig(
        level=logging.INFO,
        filename="eye-break.log",
        filemode="w",
        format="%(asctime)s - %(message)s",
    )
    logging.info("starting eye break program.")
    take_break()


if __name__ == "__main__":
    main()
