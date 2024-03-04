#Source: https://stackoverflow.com/questions/76734843/attributeerror-module-os-has-no-attribute-killpg
if __name__ == "__main__":
    try:
        main()
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)
        os.killpg(0, signal.SIGKILL)

    exit(0)