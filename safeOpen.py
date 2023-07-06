def safeOpen(filename):
    try:
        return open(filename)
    except FileNotFoundError:
         return None

                    
            
    
        
    
        
    
