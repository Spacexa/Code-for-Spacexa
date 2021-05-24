import speech_recognition as sr
import pyttsx3


r=sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

engine_talk("Hello!! I am Spacexa, I can solve your query on space. Ask me")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Speak:")
    audio=r.listen(source)
    #Convert Voice Commands to Text
    command=r.recognize_google(audio)
    
    

                    
    if "star" in command:
        import pygame
        
        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        
        img = pygame.image.load("Images/star.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("A star is an astronomical object consisting of a luminous spheroid of plasma held together by its own gravity. The nearest star to Earth is the Sun. Many other stars are visible to the naked eye at night, but due to their immense distance from Earth they appear as fixed points of light in the sky.")
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
        print("Closing")
    elif "planets" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/plantes.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
    
        pygame.display.update()
            
        engine_talk("There are more planets than stars in our galaxy. The current count orbiting our star: eight. The inner, rocky planets are Mercury, Venus, Earth and Mars. ... The outer planets are gas giants Jupiter and Saturn and ice giants Uranus and Neptune.")  
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "earth" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/earth.jpeg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Earth, our home planet, is a world unlike any other. The third planet from the sun, Earth is the only place in the known universe confirmed to host life. With a radius of 3,959 miles, Earth is the fifth largest planet in our solar system, and it's the only one known for sure to have liquid water on its surface.")
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "moon" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/moon.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("The Moon is Earth's only natural satellite. At about one-quarter the diameter of Earth, it is the largest natural satellite in the Solar System relative to the size of its planet, the fifth largest satellite in the Solar System overall, and is larger than any dwarf planet.")
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "sun" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/sun.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("The Sun is the star at the center of the Solar System. It is a nearly perfect sphere of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating the energy mainly as visible light and infrared radiation. It is by far the most important source of energy for life on Earth.")
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "hottest planet" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/hot planet.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Venus is the hottest planet.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "venus" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/venus.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Venus is the second planet from the Sun. It is named after the Roman goddess of love and beauty. ... Venus is a terrestrial planet and is sometimes called Earth's sister planet because of their similar size, mass, proximity to the Sun, and bulk composition. It is radically different from Earth in other respect")
        
        while True:
             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "mercury" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/mercury.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Mercury is the smallest planet in our solar system. ... Along with Venus, Earth, and Mars, Mercury is one of the rocky planets. It has a solid surface that is covered with craters. It has no atmosphere, and it doesn't have any moons.")
        
        while True:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "mars" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/mars.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury. ... Mars is a terrestrial planet with a thin atmosphere, with surface features reminiscent of the impact craters of the Moon and the valleys, deserts and polar ice caps of Earth.")
        
        while True:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "Jupiter" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/jupiter.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass (more than) two and a half times that of all the other planets in the Solar System combined, but (a little) less than one-thousandth the mass of the Sun.")
        
        while True:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "saturn" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/saturn.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It only has one-eighth the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "uranus" in command:
        import pygame

        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/uranas.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Uranus is known as the “sideways planet” because it rotates on its side. Uranus was discovered in 1781 by William Herschel. Uranus was the first planet found using a telescope. Uranus is an Ice Giant planet and nearly four times larger than Earth.")
        
        while True:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
            
        print("Closing")
    elif "neptune" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/neptune.png")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Neptune is the eighth and farthest-known Solar planet from the Sun. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, slightly more massive than its near-twin Uranus.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "pluto" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/pluto.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Pluto (minor planet designation: 134340 Pluto) is a dwarf planet in the Kuiper belt, a ring of bodies beyond the orbit of Neptune. It was the first and the largest Kuiper belt object to be discovered. After Pluto was discovered in 1930, it was declared to be the ninth planet from the Sun.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "milky way" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/milky way.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("The Milky Way is a large barred spiral galaxy. All the stars we see in the night sky are in our own Milky Way Galaxy. ... These stars form a large disk whose diameter is about 100,000 light years. Our Solar System is about 25,000 light years away from the center of our galaxy – we live in the suburbs of our galaxy.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break  
    elif "black hole" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/black hole.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("A black hole is a region of spacetime where gravity is so strong that nothing—no particles or even electromagnetic radiation such as light—can escape from it. The theory of general relativity predicts that a sufficiently compact mass can deform spacetime to form a black hole.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break     
    elif "solar system" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/solar system.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("The Solar System also contains smaller objects. The asteroid belt, which lies between the orbits of Mars and Jupiter, mostly contains objects composed, like the terrestrial planets, of rock and metal.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "asteroid" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/asteroid.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("An asteroid is a minor planet of the inner Solar System. Historically, these terms have been applied to any astronomical object orbiting the Sun that did not resolve into a disc in a telescope and was not observed to have characteristics of an active comet such as a tail.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "meteroid" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/meteroid.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("A meteoroid is a small rocky or metallic body in outer space. Meteoroids are significantly smaller than asteroids, and range in size from small grains to one-meter-wide objects. Objects smaller than this are classified as micrometeoroids or space dust.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "asteroid belt" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/as belt.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("The asteroid belt is a torus-shaped region in the Solar System, located roughly between the orbits of the planets Jupiter and Mars. It contains a great many solid, irregularly shaped bodies, of many sizes but much smaller than planets, called asteroids or minor planets. ")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "universe" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/universe.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("The universe is all of space and time and their contents, including planets, stars, galaxies, and all other forms of matter and energy. ... At the largest scale, galaxies are distributed uniformly and the same in all directions, meaning that the universe has neither an edge nor a center.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "galaxy" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/galaxy.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas, dust, and dark matter. The word galaxy is derived from the Greek galaxias, literally milky , a reference to the Milky Way.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif "white hole" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/white hole.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("in general relativity, a white hole is a hypothetical region of spacetime and singularity that cannot be entered from the outside, although energy-matter, light and information can escape from it.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif"largest planet" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/lp.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Jupiter is the largest planet.")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif"animal that can survive in space" in command:
        import pygame

        Width = 1500
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        img = pygame.image.load("Images/animal in space.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("Tardigrades, known colloquially as water bears or moss piglets, are a phylum of eight-legged segmented micro-animals. They were first described by the German zoologist Johann August Ephraim Goeze in 1773, who called them little water bears")
        
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
    elif"magnetic field" in command:
        import pygame
        
        Width = 1520
        Height = 760
        
        pygame.init()
        
        screen = pygame.display.set_mode((Width,Height))
        
        pygame.display.set_caption("Spacexa")
        
        
        img = pygame.image.load("Images/magnetic field.jpg")
        
        screen.blit(img,(0,0))
        
        EventStatus = "None"
        
        pygame.display.update()
        engine_talk("There are magnetic fields in space, but their strength depends on where you are. The spiral arms of the Milky Way seem to have some very large-scale organized magnetic field on the basis of studies of large numbers of pulsars and the polarization of their radio signals.")
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus = "Quit"
                    break
        
                
            if EventStatus == "Quit":
                break
            
        print("Closing")
    else:
        print("Sorry I couldn't understand it.")
        engine_talk("Sorry, I couldn't understand it.")