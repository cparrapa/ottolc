import tkinter
class Configtab():
    def __init__(self, master, app):
        self.app = app
        self.cbvar = tkinter.IntVar()
        self.servocb = tkinter.Checkbutton(
            master,
            variable=self.cbvar,
            text="enable servos",
            command=self.servos)
        self.servocb.grid(row=0,column=0)
        self.servocb.select()

        self.tll = tkinter.Scale(master, from_=0, to=180,
                                resolution=1, command=self.app.mov,
                                orient=tkinter.HORIZONTAL, label="trim left leg")

    def servos(self, _w = None):
    	if self.cbvar.get():
    		self.app._sendcmd("! servoson\n")
    	else:
    		self.app._sendcmd("! servosoff\n")
