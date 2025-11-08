
from colours import *

class Requester:
    def __init__( self, pg_colour:int, usr_colour:int) -> None:
        self.pg_colour = pg_colour
        self.usr_colour = usr_colour
        self.answer = self.ask()

    def ask( self, msg:str ):
        return input( f"{col( self.pg_colour )}{msg} ~ {col( self.usr_colour )}" )