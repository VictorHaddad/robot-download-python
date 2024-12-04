import platform

def verificar_bits():
    architecture = platform.architecture()[0]
    
    if 'bit' in architecture:
      architecture = architecture.replace('bit', '-bit')
    
    return architecture
