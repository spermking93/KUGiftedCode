from time import sleep
import tellopy

def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def test():
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

        #드론에 연결
        drone.connect()
        drone.wait_for_connection(60.0)
        
        #드론이륙
        drone.takeoff()
        #명령을 수행하는데 시간이 걸리기 때문에 딜레이를 추가해줍니다. 3~5초가 적절합니다.
        sleep(5)
        #drone_command.txt를 참조하여 적절한 명령을 추가합니다.
        drone.clockwise(30)
        sleep(5)
        drone.flip_left()
        sleep(5)
        drone.land()
        sleep(5)
    
    #에러가 발생했을경우 처리하는 에러문구를 출력합니다.
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()