import time, sys
def loadingfn():
    
    for i in range(0, 200):
        time.sleep(0.007)
        width = (i + 50) / 4
        bar = "[ " + "#" * int(width) + " " * (62 - int(width)) + " ]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    
    