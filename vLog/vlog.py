from colour import *

# You can modify logger config in your main file and then use it to log things !
class Logger:
    def __init__(self,
                 main_colour=WHITE,
                 second_colour=GRAYED,
                 user_colour=SKY):
        self.main_colour = main_colour
        self.second_colour = second_colour
        self.user_colour = user_colour

    # Different possible logEvents
    def info( self, tit: str, msg: str | list[ str ] = None ) -> None:
        InfoLog( "INFO", BLUE ).log( tit, msg )

    def error( self, tit: str, msg: str | list[ str ], clue: str | list[ str ] = None ) -> None:
        ExceptionLog( "ERROR", BLOOD ).log( tit, msg, clue )

    def clue( self, msg: str | list[ str ] ) -> None:
        ClueLog( "CLUE", MAGENTA ).log( "", msg )

    def warning( self, tit: str, msg: str | list[ str ] = None ) -> None:
        ExceptionLog( "WARNING", GOLD ).log( tit, msg )

    def dump( self, tit: str, msg: str | list[ str ] = None ) -> None:
        DumpLog( "DUMP", WHITE ).log( tit, msg )

    def title( self, tit: str, msg: str | list[ str ] = None ) -> None:
        TitleLog( "TITLE", SKY ).log( tit )

    def help( self, msg: str | list[ str ] ) -> None:
        HelpLog( "HELP", H_GREEN ).log( "", msg )

    def debug( self, tit: str, msg: str | list[ str ] = None ) -> None:
        DebugLog( "DEBUG", GRAYED ).log( tit, msg )


# Main class, generally good
class LogEvent:
    def __init__( self, prefix: str ="", main_colour: int =INDIGO) -> None:
        self.prefix = prefix
        self.main_colour = main_colour
        self.second_colour = get_second_colour()

    def class_error( self ) -> None:
        tmp = [ self.prefix, self.main_colour, self.second_colour ]
        self.prefix = f"{col( BLOOD, INVERTED )}EXCEPTION"
        self.main_colour = BLOOD
        self.second_colour = RED

        self.log( "Wrong Log Arguments",
                  [ "You tried to log with no title nor messages.",
                    "Nothing to log.",
                    "",
                    f"  {col( PINK, UNDERLINE )}CLUE{col( PINK )}:",
                    f"{col( MAGENTA, ITALIC )}You may have filled log() with one or two {col( MAGENTA, BOLD )}None{col( RESET )}{col( MAGENTA, ITALIC )} variables."
                    ]
                  )
        self.prefix, self.main_colour, self.second_colour = tmp

    # Printing
    def print_title( self, title: str ) -> None:
        print( self.title( title ) )

    def print_messages( self, msg: str | list[ str ] ) -> None:
        if type( msg ) is str: msg = [ msg ]

        for m in msg:
            print( self.message( m ) )

    def log( self, title: str | None,
             msg: str | list[ str ] | None = None,
             write_to_file: bool = True ) -> None:
        """Logs your message in terminal. Also sends it to the log files if not specified to not do it."""
        if title is None and msg is None:
            self.class_error()

        if title is not None: self.print_title( title )
        if msg is not None: self.print_messages( msg )

    # May be overridden
    def title( self, title: str ) -> str:
        """Prints the title: Log-type + your title \"title\""""
        return f"{col( self.main_colour, INVERTED, True )} {self.prefix}]{col( RESET )} {col( self.main_colour, UNDERLINE )}{title}"

    def message( self, msg: str ) -> str:
        """Prints all messages inside "msg" list line by line."""
        return f" {col( self.main_colour )}| {msg}{col( RESET )}"


# Create all log objects
class InfoLog( LogEvent ):
    def title( self, title: str ) -> str:
        return f"{col( self.main_colour, INVERTED, True )} {self.prefix}]{col( RESET )} {col( self.main_colour, UNDERLINE )}{title}{col( RESET )}"


class DumpLog( LogEvent ):
    def message( self, msg: str ) -> str:
        return f" {col( self.main_colour )}{msg}{col( RESET )}"


class DebugLog( LogEvent ):
    def title( self, title: str ) -> str:
        return f"{col( self.main_colour, INVERTED )} {self.prefix}]{col( WHITE )} {title}{col( RESET )}"

    def message( self, msg: str ) -> str:
        return f" {col( self.main_colour )}| {col( WHITE )}{msg}{col( RESET )}"


class ExceptionLog( LogEvent ):
    def title( self, title: str ) -> str:
        return f"{col( self.main_colour, INVERTED )} {self.prefix} /!\\ {col( RESET )} {col( self.main_colour, UNDERLINE )}{title}{col( RESET )}"

    def log( self,
             title: str | None,
             msg: str | list[ str ] | None = "There is an error and someone forgot to tell you what ?",
             clue_msg: str | list[ str ] | None = None ) -> None:
        if title is None and msg is None:
            self.class_error()

        if title is not None:
            self.print_title( title )
        if msg is not None:
            self.print_messages( msg )
        if clue_msg is not None:
            print( f"{col( self.main_colour )} |" )
            Logger.Clue( clue_msg )


class ClueLog( LogEvent ):
    def title( self, title: str ) -> str:
        return f" {col( self.main_colour )}|   {col( UNDERLINE, self.main_colour )}{self.prefix}{col( self.main_colour )}:{col( RESET )}"

    def message( self, msg: str | list[ str ] ) -> str:
        return f" {col( self.second_colour )}| {msg}{col( RESET )}"


class TitleLog( LogEvent ):
    def title( self, title: str ) -> str:
        return f"{col( self.main_colour )} {title}{col( RESET )}"

    def message( self, msg: str | list[ str ] ) -> str:
        return f"     {col( self.main_colour )}{msg}{col( RESET )}"


class AssertionLog( LogEvent ):
    def title( self, title: str ) -> str:
        return f"{col( self.main_colour )} {self.prefix} {col( self.main_colour, UNDERLINE )}{title}{col( RESET )}"


class HelpLog( LogEvent ):
    def title( self, title: str ) -> str:
        return f"{col( self.main_colour, contrast_correction=True )} {self.prefix}]{col( RESET )}"

    def message( self, msg: str ) -> str:
        return f" {col( self.second_colour )}| {col( WHITE )}{msg}{col( RESET )}"


class Result:
    def __init__( self, result, status: tuple[ bool, str ] = (True, "Ok") ):
        self.result = result
        self.status = status