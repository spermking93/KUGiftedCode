import time 
import tello 
def main(): 
    drone = None 
    
    try: 
        drone = tello.Tello() 
        print ('Battery : %d%%' % drone.battery()) 
    except RuntimeError: 
        print ('Failed to initialize the drone.\n') 
        print ('Please, check your Wi-Fi SSID.\n' )
        return
    drone.takeoff() 
    time.sleep(3) 
    drone.forward(50) 
    time.sleep(3) 
    drone.cw(90) 
    time.sleep(3)
    drone.flip('f') 
    time.sleep(3) 
    drone.land() 
    time.sleep(3)


    print ('Battery : %d%%' % drone.battery() )
    print ('Flight time: %s' % drone.flight_time()) 
    if __name__ == '__main__': 
        main()



