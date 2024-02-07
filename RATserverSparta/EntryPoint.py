from Socket.Create import Socket
from Socket.Accept import Socket
def main():
    print("there")
    sck = Socket.Create()
    sckdata = Socket.accept(sck)

if __name__ == "__main__":
    # This block will only be executed if the script is run directly
    main()