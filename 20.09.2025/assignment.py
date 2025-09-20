def shutdown():
    choice = input("Do you want to shut down? (Yes/no): ")
    if choice == "Yes":
        print("shutting down.")
    elif choice == "no":
        print("abort shut down.")
    else:
        print("sorry.")

if __name__ == "__main__":
    shutdown()
