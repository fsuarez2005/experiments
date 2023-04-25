
verbose_print_enabled = True
debug_print_enabled = True
var_print_enabled = True

def verbose_print( s ):
    if verbose_print_enabled:
        print("VERBOSE: "+str(s))
    
def debug_print( s ):
    if debug_print_enabled:
        print("DEBUG: "+str(s))
    

def var_print(var_name,var_value):
    if var_print_enabled:
        print(f"VAR: {var_name} = {var_value}")