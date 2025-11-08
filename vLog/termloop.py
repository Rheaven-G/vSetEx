
from src.logger.logger import *
from requester import *


class TermLoop:
    def __init__ ( self, name:str, colour:int =1, header:str =""):
        self.name = name
        self.colour = colour
        self.header = header
        self.logger = Logger()
        self.requester = Requester( self.colour, GRAYED )

    def deco_prefix( self, func ):
        def wrapper( *args, **kwargs ):
            print( f"{col( self.colour, INVERTED )} {self.header}]{col( RESET )}", end='' )
            func_output = func( *args, **kwargs )
            return func_output

        return wrapper

    def deco_suffix( self,  func ):
        def wrapper( *args, **kwargs ):
            func_output = func( *args, **kwargs )
            print( f"{col( RESET )}", end='' )
            return func_output

        return wrapper

    @deco_suffix
    @deco_prefix
    @property
    def log( self ):
        return self.log

    @deco_suffix
    @deco_prefix
    def request( self, msg:str ):
        return self.request.ask(msg)


    # Content and program Loop
    def start( self ):
        pass

    def loop( self ):
        pass

    def end( self ):
        pass