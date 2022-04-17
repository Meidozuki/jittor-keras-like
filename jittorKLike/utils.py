import os
def silent_preload_jittor():
    log_silent=os.environ.get("log_silent")
    var_name='log_silent'
    os.environ[var_name]='1'

    import jittor
    
    if log_silent is None:
        os.environ.pop(var_name)
    else:
        os.environ[var_name]=log_silent
        
data_format='BCHW'
if data_format == 'BCHW': cAxis=1
elif data_format == 'BCHW': cAxis=-1