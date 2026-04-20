def file_logger():
    filename = "user_logs.txt"

    print("=== Basic File Logger ===")
    print("Type 'exit' to stop logging.\n")

    while True:
        try:
            log_entry = input("Enter log message: ")

            if log_entry.lower() == "exit":
                print("Logging stopped.")
                break

            with open(filename, "a") as file:
                file.write(log_entry + "\n")

            print("Log saved successfully.\n")

        except IOError:
            print("Error: Unable to write to file.")
        except Exception as e:
            print("Unexpected error:", e)

file_logger()
