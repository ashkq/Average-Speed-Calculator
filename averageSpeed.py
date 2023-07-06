def averageSpeed():
    counter = 0
    while True:
        filename = input('Enter file name: ')
        file = safeOpen(filename)
        if file == None:
            counter += 1
            if counter == 2:
                print('Your file does not exist, program will quit')
                return
        else:
            average = 0
            i = 0
            for line in file:
                speeds = line.split()
                for speed in speeds:
                    speed = safeFloat(speed)
                    if speed < 2.0:
                        continue
                    else:
                        average += speed
                        i += 1
            average /= i
            print('Average speed is ', round(average, 2), ' miles per hour')
            return
