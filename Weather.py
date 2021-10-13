from pyowm import OWM

owm = OWM('a464f9ec8c423ca4231d871fa1820406')
mgr = owm.weather_manager()
while True:
    try:
        place = input('Select your city: ')

        observation = mgr.weather_at_place(place)
        w = observation.weather

        t = w.temperature('celsius')['temp']

        humi = w.humidity

        time = w.reference_time('iso')

        print(place+': '+w.detailed_status+' now.\nTemperature is '+str(t)+' celsius.\nHumidity: '+str(humi)+'%\nUpdated:'+time)
        break

    except:
        print('Please, enter the correct value.')

