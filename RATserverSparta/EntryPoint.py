class main:
    def __init__(self):
        print("there")
        sck = Socket.Create()
        sckdata = Socket.accept(sck)

main()