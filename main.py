
import json
import os
import sys

GENERAL_CFG = {
    "v_path" : f"C:/Users/{os.environ["username"]}/.vlab",
    "global_config" : "vconfig.cfg",
}

FALLBACK_CFG = {
    "self_path" : "vSetEx",
    "save_location" : "cfg_files",
    "binding_tracker" : "bindings.json"
}

'''
macOS & Windows each know their software and their config location
cloud doesn't know anything except config files and the binder which knows what config goes with what software.
vSetEx makes the relation between cloud and local information and paths.
'''



class Config:
    def __init__( self,
                  software_path :str,
                  config_path :str) -> None:
        self.software = software_path
        self.config_path = config_path

    #end __init__



class Software:
    def __init__( self,
                  name:str,
                  saved_configs :list[str] | str ) -> None:

        self.name = name
        self.saved_configs = saved_configs

    #end __init__



class Binding:
    def __init__( self,
                  name: str,
                  config_path :str,
                  software :Software ) -> None:

        self.name = name
        self.config_path = config_path
        self.software = software

    #end __init__



class VSetEx:
    def __init__( self ) -> None:
        self.general_cfg = GENERAL_CFG
        self.cfg = self.gather_config()

        self.bindings :list[Binding]
        self.softwares :list[Software]

    #end __init__


    def gather_config( self ) -> dict:

        try:
            with open( GENERAL_CFG['v_path'].join(GENERAL_CFG['global_config']), "r" ) as file:
                cfg = json.load( file )

                return cfg["vSetEx"]

        except KeyError:
            print( "WARNING -- No vSetEx config found in vconfig.cfg. First Time using vSetEx ?")

            try:
                with open(GENERAL_CFG['v_path'].join(GENERAL_CFG['global_config']), "w" ) as file:
                    cfg = json.load( file )

                    cfg["vSetEx"] = FALLBACK_CFG
                    file.write( json.dumps( cfg ) )

                    print( f"INFO -- vSetEx config added to vconfig.cfg at {GENERAL_CFG['v_path']}")

                    return FALLBACK_CFG

            except FileNotFoundError:
                self._config_file_not_found_error_response()

        except FileNotFoundError:
            self._config_file_not_found_error_response()


    @staticmethod
    def _config_file_not_found_error_response() -> dict:
        print( "WARNING -- No vconfig.cfg found. First Time using a vScript ?" )

        try:
            os.mkdir( GENERAL_CFG['v_path'] )

        except FileExistsError:
            pass

        finally:
            with open( GENERAL_CFG[ 'v_path' ].join( GENERAL_CFG[ 'general_config' ] ), "w" ) as file:
                cfg = GENERAL_CFG
                cfg[ "vSetEx" ] = FALLBACK_CFG

                file.write( json.dumps( cfg ) )



    #end gather_config



if __name__ == "__main__":
    # "C:/Users/v.labrousse/AppData/Roaming//JetBrains//PyCharm2025/codestyles/Default.xml"
    setex = VSetEx()


    pass