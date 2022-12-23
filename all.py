def main():
    is_connected = True
    has_electricity = True
    has_paid_bills = True

    requirements = [is_connected, has_electricity, has_paid_bills]

    if all(requirements):
        print("Your internet is active!")
    else:
        print("Please contact your provider for more information...")


if __name__ == "__main__":
    main()
