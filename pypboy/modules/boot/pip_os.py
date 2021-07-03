import pypboy
import pygame
import game
import config
import pypboy.ui


class Module(pypboy.SubModule):

    label = ""

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.pipos = Pipos()
        self.pipos.rect[0] = 0
        self.pipos.rect[1] = 0
        self.add(self.pipos)
        
    def handle_resume(self):
        self.pipos.top = 0
        self.pipos.line = 0
        self.pipos.char = 0
        self.pipos.y = 0
        self.pipos.current_time = 0
        self.pipos.image.fill((0,0,0))
        super(Module, self).handle_resume()

        
class Pipos(game.Entity):

    def __init__(self):
        super(Pipos, self).__init__()
        
        self.image = pygame.surface.Surface((config.WIDTH, config.HEIGHT))
        self.rect[1] = 0
        self.top = 0
        
        self.animation_time = 4
        self.current_time = 0

        self.text_array = [
                    "▯","▯","▯","~","~","~","~","~","▯","▯","▯","~","~","~","~","~","▯","▯","▯","~","~","~","~","~","▯","▯","▯","~","~","~","~","/",
                    "*************** PIP-05 (R) V7 .1.0.8 ************** ",
                    " ",
                    " ",
                    " ",
                    "COPYRIGHT 2075 ROBCO(R) ",
                    "LOADER VI.1 ",
                    "EXEC VERSION 41.10 ",
                    "264k RAM SYSTEM ",
                    "{gc.mem_free()} BYTES FREE ",
                    "NO HOLOTAPE FOUND ",
                    "LOAD ROM(1): DEITRIX 303 ",
                    "@","@","@","^","^","^","^","^","@","@","@","^","^","^","^","^","@","@","@","^","^","^","^","^","@","@","@","^","^","^","^","^",
                    ]
        self.line = 0
        self.char = 0
        self.y = 0
        
        # # Blink the cursor at the very end
        # i = 0
        # while i < 6:
        #     my_text.text = text + "▯"
        #     time.sleep(0.2)
        #     text = text.strip("▯")
        #     my_text.text = text
        #     time.sleep(0.2)
        #     i = i + 1

    # def update(self, *args, **kwargs):
        # super(Boot, self).update(self, *args, **kwargs)

    def update(self):
        if self.current_time >= self.animation_time:
            self.current_time = 0
           
            if self.line >= len(self.text_array): #Check if at the end of the paragraph
                self.line = 0 #This loops, need to replace with a stop function
                self.char = 0
                self.y = 0
                self.image.fill((0,0,0))
            
            self.text = self.text_array[self.line] #Get the line of text

            #This code is ugly but works
            if self.text == "▯": # Look for a special character to make starting blink
                text_to_blit = config.TechMono[26].render(self.text, True, (config.bright), (0,0,0))
                self.image.blit(text_to_blit, (0,0))
                self.line += 1 # Go to next line
            elif self.text == "~": # Look for a special character to make starting blink
                text_to_blit = config.TechMono[26].render(" ", True, (config.bright), (0,0,0))
                self.image.blit(text_to_blit, (0,0))
                self.line += 1 # Go to next line
            elif self.text == "/": # Look for a special character to make starting blink
                text_to_blit = config.TechMono[26].render(" ", True, (config.bright), (0,0,0))
                self.image.blit(text_to_blit, (0,0))
                self.char = 0
                self.line += 1 # Go to next line
            elif self.text == "^": # Look for a special character to make starting blink
                text_to_blit = config.TechMono[26].render(" ", True, (config.bright), (0,0,0))
                self.image.blit(text_to_blit, (337,241))
                self.line += 1 # Go to next line
            elif self.text == "@": # Look for a special character to make starting blink
                text_to_blit = config.TechMono[26].render("▯", True, (config.bright), (0,0,0))
                self.image.blit(text_to_blit, (337,241))
                self.line += 1 # Go to next line
            elif self.char >= len(self.text): #Check if at the end of the line
                self.char = 0 #Reset to first character
                self.line += 1 # Go to next line
                text_to_blit = config.TechMono[26].render(self.text, True, (config.bright), (0,0,0))
                self.image.blit(text_to_blit, (0,self.y))
                self.y += 24
                #self.text = self.text[:-1] #Strip the box character before moving on
            else:
                self.text = self.text[0:self.char] + "▯"  #Just get the characters up to now
                text_to_blit = config.TechMono[26].render(self.text, True, (config.bright), (0,0,0))
                self.image.blit(text_to_blit, (0,self.y))

            self.char += 1
        
        
    def render(self, *args, **kwargs):
        #self.top -= 5
        #self.rect[1] = self.top
        super(Pipos, self).render(self, *args, 
        **kwargs)
        self.current_time += 1
     
    def handle_resume(self):
        pass