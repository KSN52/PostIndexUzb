from datetime import datetime


def main() -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Hello, World!")
    print(f"Текущее время: {current_time}")


if __name__ == "__main__":
    main()
