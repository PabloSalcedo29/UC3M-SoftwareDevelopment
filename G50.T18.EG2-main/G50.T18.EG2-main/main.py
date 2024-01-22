from secureAll import AccessManager


def main():
    mng = AccessManager()
    res = mng.readaccessrequestfromJSON("test.json")
    print(res)


if __name__ == "__main__":
    main()
