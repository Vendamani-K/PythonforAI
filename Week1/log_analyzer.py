
import csv


def analyze_logs(filename):
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    total_entries = 0
    errors = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(maxsplit=3)

                if len(parts) < 3:
                    continue

                timestamp = parts[0] + " " + parts[1]
                level = parts[2]
                message = parts[3] if len(parts) > 3 else ""

                if level in log_counts:
                    log_counts[level] += 1
                    total_entries += 1

                if level == "ERROR":
                    errors.append([timestamp, level, message])

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    print("\n===== LOG ANALYZER =====")
    print("Total log entries:", total_entries)
    print("INFO messages:", log_counts["INFO"])
    print("WARNING messages:", log_counts["WARNING"])
    print("ERROR messages:", log_counts["ERROR"])

    with open("errors.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Level", "Message"])
        writer.writerows(errors)

    print("\nError report exported to errors.csv")


def main():
    filename = input("Enter log filename: ")
    analyze_logs(filename)


if __name__ == "__main__":
    main()
