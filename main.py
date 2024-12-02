# importing the pygame library
import pygame
from random import randint
from random import shuffle
pygame.init()

# setting the screen and dimensions
win = pygame.display.set_mode((1280, 720))

# titling the window
pygame.display.set_caption("Retrieval of the Death Mask")

# LOADING IMAGES
    # characters
walkRightModern = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeftModern = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkRightAncient = [pygame.image.load('R1A.png'), pygame.image.load('R2A.png'), pygame.image.load('R3A.png'), pygame.image.load('R4A.png'), pygame.image.load('R5A.png'), pygame.image.load('R6A.png'), pygame.image.load('R7A.png'), pygame.image.load('R8A.png'), pygame.image.load('R9A.png')]
walkLeftAncient = [pygame.image.load('L1A.png'), pygame.image.load('L2A.png'), pygame.image.load('L3A.png'), pygame.image.load('L4A.png'), pygame.image.load('L5A.png'), pygame.image.load('L6A.png'), pygame.image.load('L7A.png'), pygame.image.load('L8A.png'), pygame.image.load('L9A.png')]
walkLeftDirector = [pygame.image.load('L1D.png'), pygame.image.load('L2D.png'), pygame.image.load('L3D.png')]
walkRightDirector = [pygame.image.load('R1D.png'), pygame.image.load('R2D.png'), pygame.image.load('R3D.png')]
walkRightSet = pygame.image.load('set_enemy_right.png')
walkLeftSet = pygame.image.load('set_enemy_left.png')

    # backgrounds
mainMenuBg = pygame.image.load('mainmenu_bg.jpg')
officeBg = pygame.image.load('office_bg.jpg')
timeMachineModernBg1 = pygame.image.load('timemachine_modern_bg_1.jpg')
timeMachineModernBg2 = pygame.image.load('timemachine_modern_bg_2.jpg')
timeMachineAncientBg = pygame.image.load('timemachine_ancient.jpg')
desert = pygame.image.load('desert1.jpg')
settingsBg = pygame.image.load('settings_screen.png')
instructionsBg = pygame.image.load('instructions_menu.png')
hieroglyphicsMiniGameBg = pygame.image.load('hieroglyphics_minigame_bgg.png')
battleGroundBg = pygame.image.load('battleground_1.png')
landscapeBg1 = pygame.image.load('landscape_1.png')
landscapeBg2 = pygame.image.load('landscape_2.png')
landscapeBg3 = pygame.image.load('landscape_3.png')
landscapeBg4 = pygame.image.load('battleground_2.png')
valleyOfTheKingsOutside1 = pygame.image.load('valleyofthekings_outside_1.png')
valleyOfTheKingsOutside2 = pygame.image.load('valleyofthekings_outside_2.png')
quizBg = pygame.image.load('quiz_screen.png')
shopBg = pygame.image.load('shop_background.png')
findingTombBg = pygame.image.load('finding_tomb.png')
foundTombBg = pygame.image.load('found_tomb.png')
tombCoffinBg = pygame.image.load('tomb_coffin.png')
maskMuseumBg = pygame.image.load('mask_museum.png')
ayMummificationBg = pygame.image.load('ay_mummification.png')

# buttons
playButton = pygame.image.load('play_button.png')
loadSavedDataButton = pygame.image.load('load_saved_data.png')
settingsButton = pygame.image.load('settings.png')
exitGameButton = pygame.image.load('exitgame_button.png')
instructionsButton = pygame.image.load('instructions_button.png')
backButton = pygame.image.load('back_button.png')
ok = pygame.image.load('ok_button.png')
yes = pygame.image.load('yes.png')
no = pygame.image.load('no.png')
    #quiz
startQuizButton = pygame.image.load('start_quiz.png')
cancel = pygame.image.load('cancel.png')
ra = pygame.image.load('ra_button.png')
osiris = pygame.image.load('osiris_button.png')
anubis = pygame.image.load('anubis_button.png')
tutankhamun = pygame.image.load('tutankhamun_button.png')
cleopatra = pygame.image.load('cleopatra_button.png')
cats = pygame.image.load('cats_button.png')
falcon = pygame.image.load('falcon_button.png')
hippo = pygame.image.load('hippo_button.png')
nubians = pygame.image.load('nubians_button.png')
setGod = pygame.image.load('set_button.png')
khufu = pygame.image.load('khufu_button.png')
canopic_jars = pygame.image.load('canopic_jars_button.png')
afterlife = pygame.image.load('afterlife_button.png')
offerings = pygame.image.load('offerings_button.png')
kemet = pygame.image.load('kemet_button.png')
burial_chambers = pygame.image.load('burial_chambers_button.png')
eleven = pygame.image.load('eleven_button.png')
nefertiti = pygame.image.load('nefertiti_button.png')
crocodile = pygame.image.load('crocodile_button.png')
the_british = pygame.image.load('the_british_button.png')
mummification = pygame.image.load('mummification_button.png')
five = pygame.image.load('five_button.png')
akhenaten = pygame.image.load('akhenaten.png')
    #shop
glaive_button = pygame.image.load('glaive_button.png')
dagger_button= pygame.image.load('dagger_button.png')
spear_button = pygame.image.load('spear_button.png')
khopesh_button = pygame.image.load('khopesh_button.png')
ceremonial_axe_button = pygame.image.load('ceremonialaxe_button.png')
battle_axe_button = pygame.image.load('battleaxe_button.png')
shopbutton = pygame.image.load('shop.png')
buybutton = pygame.image.load('buy.png')
closebutton = pygame.image.load('close.png')
equipbutton = pygame.image.load('equip.png')

    # weapons
glaive = pygame.image.load('glaive.png')
dagger = pygame.image.load('dagger.png')
spear = pygame.image.load('spear.png')
khopesh = pygame.image.load('khopesh.png')
ceremonial_axe = pygame.image.load('ceremonialaxe.png')
battle_axe = pygame.image.load('battleaxe.png')


    # facts
fact1 = pygame.image.load('fact1.png')
fact2 = pygame.image.load('fact2.png')
fact3 = pygame.image.load('fact3.png')
fact4 = pygame.image.load('fact4.png')
fact5 = pygame.image.load('fact5.png')
fact6 = pygame.image.load('fact6.png')
fact7 = pygame.image.load('fact7.png')
fact8 = pygame.image.load('fact8.png')




    # other
logo = pygame.image.load('logo.png')
hieroglyphicsWall = pygame.image.load('hieroglyphics_wall.png')
hieroglyphics = pygame.image.load('hieroglyphics.png')
moneyBar = pygame.image.load('money_bar.png')
heart = pygame.image.load('heart.png')
winnerText = pygame.image.load('congratulatory_hieroglyphics_message.png')
option = pygame.image.load('option.png')
not_enough= pygame.image.load('not_enough.png')
item_purchased = pygame.image.load('item_purchased.png')
equip_message = pygame.image.load('equipped.png')
hieroglyphicsInTomb = pygame.image.load('hieroglyphics_in_tomb.png')
maskRetrieved = pygame.image.load('mask_retrieved.png')
endScreen = pygame.image.load('end.png')
deadScreen = pygame.image.load('dead.png')
enemy_instructions = pygame.image.load('enemy.png')

clock = pygame.time.Clock()

# CLASSES

    # button class
class Button():
    def __init__(self, x, y, image, scale, answer_id=None):
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((int(width * scale)), (int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.clicked = False
        self.answer_id = answer_id
        self.show_weapon = False

    def drawButton(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check if mouse is colliding with button
        if self.rect.collidepoint(pos):
            # 1 here means a left click
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                
        # draw the button on screen
        win.blit(self.image, (self.rect.x, self.rect.y))

        return action

    # player class

class Player():
    def __init__(self, x, y, width, height, listL, listR, leftboundary, rightboundary):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.listL = listL
        self.listR = listR
        # velocity
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.leftboundary = leftboundary
        self.rightboundary = rightboundary
        self.showWeapon = False
        self.hit = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  

    def drawPlayer(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(self.listL[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.listR[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(self.listL[0], (self.x, self.y))
            elif self.right:
                win.blit(self.listR[0], (self.x, self.y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.leftboundary:
            self.left = True
            self.right = False
            self.standing = False
            self.x -= self.vel
        elif keys[pygame.K_RIGHT] and self.x < self.rightboundary:
            self.left = False
            self.right = True
            self.standing = False
            self.x += self.vel
        else:
            self.standing = True
            self.walkCount = 0

        # update the player's rectangle position
        self.rect.topleft = (self.x, self.y)

        if self.showWeapon:
            if shopScreen.equipped:
                win.blit(shopScreen.selected_item['picture'], (self.x + 60, self.y + 80))

    def hitEnemy(self):
        if self.rect.colliderect(enemySet.rect) == True:
            self.hit = True
        
        if self.hit == True:
            healthBar.hp -= 10
            if healthBar.hp <= 0:
                win.blit(deadScreen, (0, 0))  
                if okButton.drawButton():
                    self.hit = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and enemySet.visible == True:
            enemySet.enemyHealthBar.hp -= 10
            if enemySet.enemyHealthBar.hp <= 0:
                enemySet.visible = False
            print('shoot')




class Npc():
    def __init__(self, x, y, width, height, leftList, rightList, num):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num = num
        self.walkCount = 0
        self.leftList = leftList
        self.rightList = rightList
        self.left = False
        self.right = False

    def drawNpc(self):
        win.blit(self.leftList[0], (self.x, self.y))

    def move(self):
        for i in range(self.num):
            if self.right:
                win.blit(self.rightList[self.walkCount], (self.x, self.y))
                self.x += 1
                self.walkCount +=1
            elif self.left:
                win.blit(self.leftList[self.walkCount], (self.x, self.y))
                self.x -= 1 
                self.walkCount += 1
            if self.walkCount == 3:
                self.walkCount = 0
    

class text():
    def __init__(self, font, colour, message, size, x, y):
        self.font = font
        self.colour = colour
        self.message = message
        self.size = size
        self.x = x
        self.y = y
        self.counter = 0
        self.speed = 2
        self.done = False

    def blitText(self):
        font = pygame.font.Font(self.font, self.size)
        snip = font.render('', True, self.colour)
        if self.counter < self.speed * len(self.message):
            self.counter += 1
        elif self.counter >= self.speed * len(self.message):
            self.done = True
        snip = font.render(self.message[0:self.counter // self.speed], True, self.colour)
        win.blit(snip, (self.x,self.y))
        pygame.display.flip()

    def drawText(self):
        font = pygame.font.Font(self.font, self.size)
        snip = font.render('', True, self.colour)
        if self.counter < self.speed * len(self.message):
            self.counter += 1
        elif self.counter >= self.speed * len(self.message):
            self.done = True
        snip = font.render(self.message[0:self.counter // self.speed], True, self.colour)

class prop():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((int(width * scale)), (int(height * scale))))
        self.x = x
        self.y = y
        self.scale = scale

    def drawProp(self):
        win.blit(self.image, (self.x, self.y))

class Money:
    def __init__(self, x, y, initial_amount=0):
        self.total = initial_amount
        self.x = x
        self.y = y

    def drawMoneyBar(self):
        win.blit(moneyBar, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 25)
        total_amount = font.render(str(self.total), True, '#2D220A')
        win.blit(total_amount, (self.x, self.y))

    def addMoney(self, amount): # add money to total
        self.total += amount

    def loseMoney(self, amount): # subtract money from total
        if self.total >= amount:
            self.total -= amount
            return True
        else:
            return False


    def resetMoney(self, amount=0): # resets amount of money to a specific value
        self.total = amount
        print(f"Money total reset to {self.total}")




class HealthBar():
    def __init__(self, x, y, width, height, max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = max_hp
        self.max_hp = max_hp

    def drawHealthBar(self):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(win, 'red', (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, 'green', (self.x, self.y, self.width * ratio, self.height))
        win.blit(heart, (700, -10))



class Quiz():
    def __init__(self, number, state):
        self.number = number  # quiz number
        self.state = state  # whether the quiz is optional or compulsory
        self.quizQuestions = [
            {'question': 'Who was the God of the Sun?', 'category': 'gods', 'correct_answer': 'ra'},
            {'question': 'Who was the God of the underworld?', 'category': 'gods', 'correct_answer': 'anubis'},
            {'question': 'Who was the God of the dead?', 'category': 'gods', 'correct_answer': 'osiris'},
            {'question': 'Who became Pharaoh at age 9?', 'category': 'important people', 'correct_answer': 'tutankhamun'},
            {'question': 'Which ruler was known for her close relations with Julius Caesar and Mark Antony?', 'category': 'important people', 'correct_answer': 'cleopatra'},
            {'question': 'Which Pharaoh restored Ancient Egyptian religion and practices after it was set aside by his predecessor?', 'category': 'important people', 'correct_answer': 'tutankhamun'},
            {'question': 'What animal was considered sacred?', 'category': 'animals', 'correct_answer': 'cats'},
            {'question': 'What animal is Ra\'s head?', 'category': 'animals', 'correct_answer': 'falcon'},
            {'question': 'Which animal inhabited the Nile?', 'category': 'animals', 'correct_answer': 'hippo'},
            {'question': 'Who were Ancient Egyptians invaded by at some point?', 'category': 'enemies', 'correct_answer': 'nubians'},
            {'question': 'Who killed Osiris beyond the possibility of resurrection?', 'category': 'enemies', 'correct_answer': 'set'},
            {'question': 'Who was known as the cruellest leader Ancient Egypt had?', 'category': 'enemies', 'correct_answer': 'khufu'},
            {'question': 'What are organs placed in during mummification?', 'category': 'religious', 'correct_answer': 'canopic_jars'},
            {'question': 'Where did Ancient Egyptians believe you go after death?', 'category': 'religious', 'correct_answer': 'afterlife'},
            {'question': 'What did people take to temples to give to the gods?', 'category': 'religious', 'correct_answer': 'offerings'},
            {'question': 'What was Egypt commonly referred to before?', 'category': 'landmarks', 'correct_answer': 'kemet'},
            {'question': 'What is typically inside of pyramids?', 'category': 'landmarks', 'correct_answer': 'burial_chambers'},
            {'question': 'How many countries does the River Nile go through?', 'category': 'landmarks', 'correct_answer': 'eleven'}
        ]
        

        self.quizAnswers = {
            0: [Button(200, 300, ra, 0.5, 'ra'),                          Button(400, 300, osiris, 0.5, 'osiris'), Button(600, 300, anubis, 0.5, 'anubis'), Button(800, 300, setGod, 0.5, 'set')],
            1: [Button(200, 300, osiris, 0.5, 'osiris'),             Button(400, 300, ra, 0.5, 'ra'), Button(600, 300, setGod, 0.5, 'set'), Button(800, 300, anubis, 0.5, 'anubis')],
            2: [Button(200, 300, anubis, 0.5, 'anubis'),             Button(400, 300, osiris, 0.5, 'osiris'), Button(600, 300, setGod, 0.5, 'set'), Button(800, 300, ra, 0.5, 'ra')],
            3: [Button(200, 300, tutankhamun, 0.5, 'tutankhamun'),   Button(400, 300, cleopatra, 0.5, 'cleopatra'), Button(600, 300, akhenaten, 0.5, 'akhenaten'), Button(800, 300, khufu, 0.5, 'khufu')],
            4: [Button(200, 300, cleopatra, 0.5, 'cleopatra'),       Button(400, 300, tutankhamun, 0.5, 'tutankhamun'), Button(600, 300, akhenaten, 0.5, 'akhenaten'), Button(800, 300, nefertiti, 0.5, 'nefertiti')],
            5: [Button(200, 300, tutankhamun, 0.5, 'tutankhamun'),   Button(400, 300, cleopatra, 0.5, 'cleopatra'), Button(600, 300, akhenaten, 0.5, 'akhenaten'), Button(800, 300, nefertiti, 0.5, 'nefertiti')],
            6: [Button(200, 300, cats, 0.5, 'cats'),                 Button(400, 300, falcon, 0.5, 'falcon'), Button(600, 300, hippo, 0.5, 'hippo'), Button(800, 300, crocodile, 0.5, 'crocodile')],
            7: [Button(200, 300, falcon, 0.5, 'falcon'),             Button(400, 300, cats, 0.5, 'cats'), Button(600, 300, hippo, 0.5, 'hippo'), Button(800, 300, crocodile, 0.5, 'crocodile')],
            8: [Button(200, 300, hippo, 0.5, 'hippo'),               Button(400, 300, cats, 0.5, 'cats'), Button(600, 300, falcon, 0.5, 'falcon'), Button(800, 300, crocodile, 0.5, 'crocodile')],
            9: [Button(200, 300, nubians, 0.5, 'nubians'),           Button(400, 300, setGod, 0.5, 'set'), Button(600, 300, khufu, 0.5, 'khufu'), Button(800, 300, the_british, 0.5, 'the_british')],
           10: [Button(200, 300, setGod, 0.5, 'set'),                Button(400, 300, nubians, 0.5, 'nubians'), Button(600, 300, khufu, 0.5, 'khufu'), Button(800, 300, the_british, 0.5, 'the_british')],
           11: [Button(200, 300, khufu, 0.5, 'khufu'),               Button(400, 300, nubians, 0.5, 'nubians'), Button(600, 300, setGod, 0.5, 'set'), Button(800, 300, the_british, 0.5, 'the_british')],
           12: [Button(200, 300, canopic_jars, 0.5, 'canopic_jars'), Button(400, 300, afterlife, 0.5, 'afterlife'), Button(600, 300, offerings, 0.5, 'offerings'), Button(800, 300, afterlife, 0.5, 'afterlife')],
           13: [Button(200, 300, afterlife, 0.5, 'afterlife'),       Button(400, 300, canopic_jars, 0.5, 'canopic_jars'), Button(600, 300, offerings, 0.5, 'offerings'), Button(800, 300, mummification, 0.5, 'mummification')],
           14: [Button(200, 300, offerings, 0.5, 'offerings'),       Button(400, 300, canopic_jars, 0.5, 'canopic_jars'), Button(600, 300, afterlife, 0.5, 'afterlife'), Button(800, 300, mummification, 0.5, 'mummification')],
           15: [Button(200, 300, kemet, 0.5, 'kemet'),               Button(400, 300, five, 0.5, 'five'), Button(600, 300, burial_chambers, 0.5, 'burial_chambers'), Button(800, 300, eleven, 0.5, 'eleven')],
           16: [Button(200, 300, burial_chambers, 0.5, 'burial_chambers'), Button(400, 300, five, 0.5, 'five'), Button(600, 300, eleven, 0.5, 'eleven'), Button(800, 300, kemet, 0.5, 'kemet')],
           17: [Button(200, 300, eleven, 0.5, 'eleven'), Button(400, 300, five, 0.5, 'five'), Button(600, 300, burial_chambers, 0.5, 'burial_chambers'), Button(800, 300, kemet, 0.5, 'kemet')]            

        }

        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.optionalText = self.font.render('Optional quiz ' + str(self.number), True, '#2D220A')
        self.compulsoryText = self.font.render('Compulsory quiz', True, '#2D220A')
        self.active = False
        self.random_number = randint(0, len(self.quizQuestions) - 1)
        self.current_question_index = self.random_number  # Start from the first question
        self.answered_questions = 0
        self.max_questions = 10
        self.score = 0  # Track the number of correct answers
        self.correct = False

    def drawQuiz(self):
        if not self.active:
            win.blit(option, (0, 0))
            if self.state == 'optional':
                win.blit(self.optionalText, (500, 250))
                if startQuiz.drawButton() == True:
                    self.active = True
                elif cancelButton.drawButton() == True:
                    return 'backToPrevious'
            elif self.state == 'compulsory':
                win.blit(self.compulsoryText, (500, 200))
                if startQuiz.drawButton() == True:
                    self.active = True
            else:
                print('Invalid state')
        if self.active == True:
            print('answered questions: ' , self.answered_questions)
            if self.answered_questions < self.max_questions:
                win.blit(quizBg, (0, 0))
                self.generateQuestion()
                pygame.display.update()
            else:
                self.showResults()
                return 'backToPrevious'


    def generateQuestion(self):
        question_data = self.quizQuestions[self.current_question_index]  
        question_text = question_data['question']
        question_surface = self.font.render(question_text, True, pygame.Color('white'))
        win.blit(question_surface, (200, 200))
        self.generateAnswers()

    def generateAnswers(self):
        answer_buttons = self.quizAnswers[self.current_question_index] 
        real_answer_id = self.quizQuestions[self.current_question_index]['correct_answer']
        print('answer current question index: ' , self.current_question_index)
        print('real answer ID: ' , real_answer_id)
        

        for button in answer_buttons:
            if button.drawButton() == True:
                if button.answer_id == real_answer_id:
                    self.correct = True
                    self.score += 1
                    self.nextQuestion()
                else:
                    self.correct = False
                    self.nextQuestion()
            

    def nextQuestion(self):
        if self.answered_questions < self.max_questions:
            self.answered_questions += 1
            self.generateQuestion()
        else:
            self.active = False
        

    def showResults(self):
        result_text = f'You got {self.score} out of {self.max_questions} correct.'
        result_surface = self.font.render(result_text, True, pygame.Color('white'))
        coins_gained = f'You have earned {self.score*10} coins in your balance.'
        coins_surface = self.font.render(coins_gained, True, pygame.Color('white'))
        win.blit(result_surface, (200, 200))
        win.blit(coins_surface, (200,300))

class Shop:
    def __init__(self):
        self.balance = moneyStats.total
        self.items = [
            {'name': 'Glaive', 'price': 0, 'button': glaiveButton, 'image': glaive_button, 'purchased': False, 'picture': glaive},
            {'name': 'Dagger', 'price': 30, 'button': daggerButton, 'image': dagger_button, 'purchased': False, 'picture': dagger},
            {'name': 'Spear', 'price': 40, 'button': spearButton, 'image': spear_button, 'purchased': False, 'picture': spear},
            {'name': 'Khopesh', 'price': 60, 'button': khopeshButton, 'image': khopesh_button, 'purchased': False, 'picture': khopesh},
            {'name': 'Ceremonial axe', 'price': 50, 'button': ceremonialAxeButton, 'image': ceremonial_axe_button, 'purchased': False, 'picture': ceremonial_axe},
            {'name': 'Battle axe', 'price': 40, 'button': battleAxeButton, 'image': battle_axe_button, 'purchased': False, 'picture': battle_axe}
        ]
        self.selected_item = None  # keep track of selected item
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.name_font = pygame.font.Font('freesansbold.ttf', 30)
        self.small_font = pygame.font.Font('freesansbold.ttf', 15)
        self.storage = []
        self.equipped = ''

    def drawShop(self):
        win.blit(shopBg, (0, 0))
        self.displayNames()
        if closeButton.drawButton():
            return 'close'

        # check for item selection
        for item in self.items:
            if item['button'].drawButton():
                self.selected_item = item

        # display selected item and handle purchase or equip
        if self.selected_item:
            self.displaySelectedItem()
            if self.selected_item['purchased']:
                if equipButton.drawButton():
                    self.equipped = self.selected_item['name']
                    print(f'Currently equipped: {self.equipped}')
                    return 'equipped'
            else:
                if buyButton.drawButton():
                    return self.buyItem()

    def displayNames(self):
        for item in self.items:
            smallName = self.small_font.render(item['name'], True, 'white')
            win.blit(smallName, (item['button'].x + 50, item['button'].y + 200))

    def displaySelectedItem(self):
        win.blit(self.selected_item['image'], (900, 200))
        nameText = self.name_font.render(self.selected_item['name'], True, pygame.Color('white'))
        win.blit(nameText, (900, 450))
        priceText = self.font.render(str(self.selected_item['price']) + ' coins', True, pygame.Color('white'))
        win.blit(priceText, (900, 400))

    def buyItem(self):
        cost = self.selected_item['price']
        if moneyStats.loseMoney(cost):
            self.balance -= cost  # update balance
            print(f"Bought {self.selected_item['name']}. Balance now: {self.balance}")
            self.selected_item['purchased'] = True  # mark the item as purchased
            self.itemInStorage()
            return 'bought'
        else:
            print(f'Not enough money. Balance now: {self.balance}')
            return 'not_enough'

    def itemInStorage(self):
        self.storage.append(self.selected_item['name'])
        print("Items in storage:", self.storage)

class enemy():    
    def __init__(self, x, y, width, height, right_pic, left_pic):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = False # whether the enemy has been hit yet or not
        self.vel = 3
        self.visible = True # whether enemy is visible or invisible
        self.walkRight = right_pic
        self.walkLeft = left_pic
        self.right = True
        self.left = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.enemyHealthBar = HealthBar(self.x, self.y, 100, 50, 100)

    def drawEnemy(self):
        if self.visible == True:
            if self.right:
                win.blit(self.walkRight, (self.x, self.y))
                self.x += self.vel
                if self.x >= 500:
                    self.left = True
                    self.right = False
                self.enemyHealthBar.drawHealthBar()

            elif self.left:
                win.blit(self.walkLeft, (self.x,self.y))
                self.x -= self.vel
                if self.x <= 0:
                    self.right = True
                    self.left = False
    
            self.rect.topleft = (self.x, self.y) # updating the enemy rect
        else:
            return 'battleground_two'
        
        


              

# FUNCTIONS / SUBROUTINES 

def drawMainMenu():
    win.blit(mainMenuBg, (0,0))
    # place logo at centre of screen by halfing the dimensions of win and taking away half the dimensions of the logo
    win.blit(logo, (115,100))
    if play.drawButton() == True:
        return 'play_game'
    if loadSavedData.drawButton() == True:
        # LOAD SAVED DATA CODE
        print('LOAD SAVED DATA')
    if settings.drawButton() == True:
        return 'settings' 
    pygame.display.update()
    return 'main_menu'

def Settings():
    # setting the background
    win.blit(settingsBg, (0,0))
    # instructions menu button
    if instructions.drawButton() == True:
        return 'instructions'
    # back button
    if back.drawButton() == True:
        return 'back'
    # exit game button
    if exitGame.drawButton() == True:
        pygame.quit()
    pygame.display.update()
    return 'settings'

def drawShop():
    result = shopScreen.drawShop()
    if result == 'close':
        return 'closeShop'
    elif result == 'not_enough':
        return 'not_enough_money'
    elif result == 'bought':
        return 'bought_message'
    elif result == 'equipped':
        return 'equipmessage'
    pygame.display.update()
    return 'shop' 


def drawOffice():
    win.blit(officeBg, (0,0))
    # drawing character on to screen
    mcModern.drawPlayer()
    directorNpc.drawNpc()
    # settings button
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcModern.rightboundary = 600
    message1.blitText()
    # showing text on screen one by one
    if message1.done == True:
        message2.blitText()
    if message2.done == True:
        message3.blitText()
    if message3.done == True:
        arrowPropOffice.drawProp()
        directorNpc.right = True
        directorNpc.move()
        if directorNpc.x >= 1280 and mcModern.x <= 10:
            return 'time_machine'
    pygame.display.update()
    return 'play_game'

def timeMachine():
    win.blit(timeMachineModernBg1, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    win.blit(fact1, (100,100))
    # drawing characters on to screen
    directorNpc.drawNpc()
    directorNpc.x = 100
    directorNpc.right = True
    directorNpc.move()
    if directorNpc.x == 500:
        win.blit(walkRightDirector[0], (500, 400))
    mcModern.drawPlayer()
    # drawing text on to screen
    message4.blitText()
    mcModern.rightboundary = 400
    if message4.done:
        mcModern.rightboundary = 1000
    if mcModern.x == 500 and message4.done == True:
        return 'time_machine_2'
    pygame.display.update()
    return 'time_machine'

def timeMachine2():
    win.blit(timeMachineModernBg2, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    directorNpc.drawNpc()
    mcModern.drawPlayer()
    message5.blitText()
    mcModern.rightboundary = 600
    if message5.done == True:
        mcModern.rightboundary = 1000
        arrowPropTimeMachine.drawProp()
        for i in range(10):
            directorNpc.x -= 1
    if mcModern.x == 900 and message5.done == True:
        return 'time_machine_ancient'
    pygame.display.update()
    return 'time_machine_2'

def timeMachineAncient():
    win.blit(timeMachineAncientBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    mcAncient.showWeapon = True
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    win.blit(fact2, (200, 50))
    mcAncient.drawPlayer()
    message6.blitText()
    if message6.done == True:
        arrowPropOffice.drawProp()
        if mcAncient.x <= 5:
            return 'desert_1'
    pygame.display.update()
    return 'time_machine_ancient'

def drawDesert():
    show = False
    win.blit(desert, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    if mcAncient.x >= 100:
        mcAncient.rightboundary = 480
        show = True
    win.blit(hieroglyphicsWall, (0,0))
    if show == True:
        message7.blitText()
    if message7.done == True:
        message8.blitText()
    if message8.done == True:
        return 'hieroglyphics_mini_game'
    pygame.display.update()
    return 'desert_1'

def hieroglyphicsMiniGame():
    # settings button
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'

    # background
    win.blit(hieroglyphicsMiniGameBg, (0, 0))
    moneyStats.drawMoneyBar()
    message9.blitText()
    win.blit(hieroglyphics, (200, 200))
    
    # fonts
    font = pygame.font.Font(None, 36)
    tryAgainText = font.render('Try again.', True, '#2D220A')

    # input box variables
    input_box = pygame.Rect(700, 200, 300, 80)
    colour_inactive = pygame.Color('white')
    colour_active = pygame.Color('yellow')
    colour = colour_inactive

    active = False
    text = ''
    showTryAgain = False

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # checking for mouse input (clicks, etc)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # changing the box outline colour depending on whether it is active or inactive 
                colour = colour_active if active else colour_inactive

            # checking for keyboard input (backspace, enter, typing answer)
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:  # enter
                        if text.lower() == 'boy king': 
                            done = True  # exit loop if answer is correct
                        else:
                            showTryAgain = True  
                            text = ''  # clear text for another input
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]  # backspace button
                    else:
                        text += event.unicode  # adding typed input to text variable

        # clearing screen
        win.blit(hieroglyphicsMiniGameBg, (0, 0))
        moneyStats.drawMoneyBar()
        message9.blitText()
        win.blit(hieroglyphics, (200, 200))

        # rendering current text into text box
        txt_surface = font.render(text, True, pygame.Color('white'))
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(win, colour, input_box, 2)

        if showTryAgain == True:
            win.blit(tryAgainText, (325, 300))

        pygame.display.update()

    return 'winner_screen'


def winnerScreen():
    win.blit(hieroglyphicsMiniGameBg, (0, 0))
    moneyStats.addMoney(20)
    win.blit(winnerText, (0, 0))
    if okButton.drawButton() == True:
        return 'desert_2'
    pygame.display.update()
    return 'winner_screen'

def drawDesert2():
    win.blit(desert, (0,0))
    win.blit(hieroglyphicsWall, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    win.blit(fact3, (50, 400))
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    mcAncient.leftboundary = 500
    mcAncient.rightboundary = 1100
    if mcAncient.x >= 1050:
        return 'landscape_1'
    pygame.display.update()
    return 'desert_2'


def landscape1():
    win.blit(landscapeBg1, (0,0))
    mcAncient.leftboundary = 5
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    # OPTIONAL QUIZ 1
    if mcAncient.x == 1280/2:
        return 'optional_quiz_1'
    if mcAncient.x <= 10:
        return 'landscape_2'
    pygame.display.update()
    return 'landscape_1'

def optionalQuiz1():
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    if optionalQuiz_1.drawQuiz() == 'backToPrevious':
        mcAncient.x = 400
        return 'landscape_1'
    pygame.display.update()
    return 'optional_quiz_1'

def landscape2():
    win.blit(landscapeBg2, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    win.blit(fact4, (100, 100))
    win.blit(fact5, (500, 100))
    mcAncient.drawPlayer()
    if mcAncient.x >= 1050:
        return 'battleground'
    pygame.display.update()
    return 'landscape_2'

def battleground():
    win.blit(battleGroundBg, (0, 0))
    win.blit(enemy_instructions, (0,0))
    if settings.drawButton():
        return 'settings'
    if shopButton.drawButton():
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer() 
    mcAncient.hitEnemy()
    if enemySet.drawEnemy() == 'battleground_two':
        return 'battleground_2'
    pygame.display.update()
    return 'battleground'


def battleground2():
    win.blit(battleGroundBg, (0, 0))
    if settings.drawButton():
        return 'settings'
    if shopButton.drawButton():
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    if mcAncient.x <= 10:
        return 'landscape_3'
    pygame.display.update()
    return 'battleground_2'



def landscape3():
    win.blit(landscapeBg3, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    message10.blitText()
    win.blit(fact8, (100, 100))
    if mcAncient.x >= 1050:
        return 'valleyofthekings_outside1'
    pygame.display.update()
    return 'landscape_3'

def valleyofthekings_outside1():
    win.blit(valleyOfTheKingsOutside1, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    message11.blitText()
    # OPTIONAL QUIZ 2 HERE
    if mcAncient.x == 1280/2:
        return 'optional_quiz_2'
    if mcAncient.x <= 10:
        return 'valleyofthekings_outside2'
    pygame.display.update()
    return 'valleyofthekings_outside1'

def optionalQuiz2():
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    if optionalQuiz_2.drawQuiz() == 'backToPrevious':
        mcAncient.x = 400
        return 'valleyofthekings_outside1'
    pygame.display.update()
    return 'optional_quiz_2'

def valleyofthekings_outside2():
    win.blit(valleyOfTheKingsOutside2, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    win.blit(fact6, (700, 100))
    message14.blitText()
    if mcAncient.x >= 1050:
        return 'finding_tomb'
    pygame.display.update()
    return 'valleyofthekings_outside2'

def findingTomb():
    win.blit(findingTombBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    if mcAncient.x <= 10:
        return 'found_tomb'
    pygame.display.update()
    return 'finding_tomb'

def foundTomb():
    win.blit(foundTombBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    mcAncient.rightboundary = 400
    message13.blitText()
    if message13.done == True:
        win.blit(hieroglyphicsInTomb, (0,0))
        message15.blitText()
        if message15.done == True:
            message16.blitText()
            if message16.done == True:
                return 'coffin'
    pygame.display.update()
    return 'found_tomb'


def coffin():
    win.blit(tombCoffinBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    mcAncient.rightboundary = 1100
    # COMPULSORY QUIZ
    if mcAncient.x >= 500: # quiz starts
        return 'compulsory_quiz'
    message17.blitText()
    pygame.display.update()
    return 'coffin'

def compulsoryQuiz():
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    if compulsoryQuiz_1.drawQuiz() == 'backToPrevious':
        return 'congratulatory_screen'
    pygame.display.update()
    return 'compulsory_quiz'

def congratulatoryScreen():
    win.blit(maskRetrieved, (0,0))
    if backButtonAfterPurchase.drawButton():
        return 'coffin2'
    pygame.display.update()
    return 'congratulatory_screen'

def coffin2():
    win.blit(tombCoffinBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    mcAncient.rightboundary = 1100
    arrowPropOffice.drawProp()
    if mcAncient.x <= 10:
        return 'ay_mummification'
    pygame.display.update()
    return 'coffin2'

def ayMummification():
    win.blit(ayMummificationBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    message18.blitText()
    if mcAncient.x >= 1100:
        mcAncient.x = 5
        return 'time_machine_ancient2'
    pygame.display.update()
    return 'ay_mummification'

def timeMachineAncient2():
    win.blit(timeMachineAncientBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcAncient.drawPlayer()
    message19.blitText()
    if mcAncient.x >= 900 and message19.done == True:
        return 'mask_in_museum'
    pygame.display.update()
    return 'time_machine_ancient2'

def maskInMuseum():
    win.blit(maskMuseumBg, (0,0))
    if settings.drawButton() == True:
        return 'settings'
    if shopButton.drawButton() == True:
        return 'shop'
    moneyStats.drawMoneyBar()
    healthBar.drawHealthBar()
    mcModern.drawPlayer()
    directorNpc.drawNpc()
    directorNpc.x = 100
    directorNpc.right = True
    mcModern.leftboundary = 800
    message20.blitText()
    if message20.done == True:
        message21.blitText()
        if message21.done == True:
            return 'end_game'
    pygame.display.update()
    return 'mask_in_museum'


def endGame():
    win.blit(endScreen, (0,0))
    if yesButton.drawButton():
        return 'main_menu'
    elif noButton.drawButton():
        pygame.quit()
    pygame.display.update()
    return 'end_game'




# MAIN LOOP

    # INSTANTIATION, ETC
play = Button(640-100-100, 400, playButton, 0.5)
loadSavedData = Button(640-100-100, 550, loadSavedDataButton, 0.5)
settings = Button(0, 600, settingsButton, 1)
mcModern = Player(200, 410, 40, 40, walkLeftModern, walkRightModern, 5 , 900)
instructions = Button(640-100-100, 200, instructionsButton, 0.5)
exitGame = Button(640-100-100, 400, exitGameButton, 0.5)
back = Button(560, 550, backButton, 0.1)
backButtonForInstructions = Button(590, 590, backButton, 0.08)
directorNpc = Npc(1080, 400, 46, 46, walkLeftDirector, walkRightDirector, 3)
message1 = text('freesansbold.ttf', 'white', 'There has been an emergency.' , 24, 130, 600)
message2 = text('freesansbold.ttf', 'white', 'Pharaoh Tutankhamun\'s mask has been stolen from our premises.' , 24, 130, 630)
message3 = text('freesansbold.ttf', 'white', 'You must retrieve the Death Mask by using the top secret time machine. Go to the room next door.' , 24, 130, 660)
arrowPropOffice = prop(500, 200, backButton, 0.2)
mcAncient = Player(900, 410, 40, 40, walkLeftAncient, walkRightAncient, 5, 1100)
message4 = text('freesansbold.ttf', 'white', 'This is the top secret time machine. Go forward and look at it.', 24, 130, 600)
message5 = text('freesansbold.ttf', 'white', 'From now on you are on your own. Good luck.', 24, 130, 630)
message6 = text('freesansbold.ttf', 'white', 'Where am I... And what am I wearing?', 24, 130, 600)
arrowPropTimeMachine = prop(1000, 400, backButton, 0.2)
message7 = text('freesansbold.ttf', 'white', 'There\'s a wall? How am I supposed to get over it...', 24, 130, 600)
message8 = text('freesansbold.ttf', 'white', 'Hieroglyphics...', 24, 130, 630)
message9 = text('freesansbold.ttf', '#2D220A', 'Decipher the message from hieroglyphics into English.', 24, 300, 150)
message10 = text('freesansbold.ttf', 'white', 'I have to be quick and discreet... Where is the Valley of the Kings?', 24, 130, 600)
message11 = text('freesansbold.ttf', 'white', 'I think that\'s it!', 24, 130, 600)
message12 = text('freesansbold.ttf', 'white', 'This is it! Now to find Tutankhamun\'s tomb...', 24, 130, 600)
message13 = text('freesansbold.ttf', 'white', 'So this is the tomb...', 24, 130, 600)
message14 = text('freesansbold.ttf', 'white', 'It\'s already night time.', 24, 130, 600)
message15 = text('freesansbold.ttf', 'white', f'The hieroglyphics in Tutankhamun\'s tomb show his names and praise him. Hieroglyphics are written in tombs to help', 20, 130, 630)
message16 = text('freesansbold.ttf', 'white', 'the Pharaohs in the afterlife and to also help relay their stories.', 20, 130, 650)
message17 = text('freesansbold.ttf', 'white', 'That\'s the mask!', 24, 130, 600)
message18 = text('freesansbold.ttf', 'white', 'Pharaoh Ay is being mummified in the background right now.', 20, 130, 600)
message19 = text('freesansbold.ttf', 'white', 'I made it!', 24, 130, 600)
message20 = text('freesansbold.ttf', 'white', 'Good job on retrieveing the Death Mask.', 20, 130, 600)
message21 = text('freesansbold.ttf', 'white', 'We have now restored it in the Egyptian museum for years to come.', 20, 130, 630)
enemySet = enemy(200, 410, 40, 40, walkRightSet, walkLeftSet)


moneyStats = Money(1190, 35)
healthBar = HealthBar(750, 20, 250, 40, 100)
okButton = Button(0, 0, ok, 1)
startQuiz = Button(400, 400, startQuizButton, 0.5)
cancelButton = Button(700, 400, cancel, 0.5)
optionalQuiz_1 = Quiz(1, 'optional')
yesButton = Button(300, 400, yes, 0.6)
noButton = Button(600, 400, no, 0.6)
optionalQuiz_2 = Quiz(2, 'optional')
compulsoryQuiz_1 = Quiz(1, 'compulsory')
#shop
shopButton = Button(100, 600, shopbutton, 1)
glaiveButton = Button(150, 100, glaive_button, 1)
daggerButton = Button(350, 100, dagger_button, 1)
spearButton = Button(550, 100, spear_button, 1)
khopeshButton = Button(150, 400, khopesh_button, 1)
ceremonialAxeButton = Button(350, 400, ceremonial_axe_button, 1)
battleAxeButton = Button(550, 400, battle_axe_button, 1)
shopScreen = Shop()
buyButton = Button(900, 500, buybutton, 1)
closeButton = Button(900, 560, closebutton, 1)
backButtonAfterPurchase = Button(560, 400, backButton, 0.1)
equipButton = Button(900, 500, equipbutton, 1)

current_screen = 'main_menu'
history = []
run = True
while run == True:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # main menu
    if current_screen == 'main_menu':
        current_screen = drawMainMenu()
        history.append(current_screen)
        # main game
    elif current_screen == 'play_game':
      current_screen = drawOffice()
      history.append(current_screen)
    elif current_screen == 'time_machine':
        current_screen = timeMachine()
        history.append(current_screen)
    elif current_screen == 'time_machine_2':
        current_screen = timeMachine2()
        history.append(current_screen)
    elif current_screen == 'time_machine_ancient':
        current_screen = timeMachineAncient()
        history.append(current_screen)
    elif current_screen == 'desert_1':
        current_screen = drawDesert()
        history.append(current_screen)
    elif current_screen == 'hieroglyphics_mini_game':
        current_screen = hieroglyphicsMiniGame()
        history.append('desert_1')
        history.append(current_screen)
    elif current_screen == 'winner_screen':
        current_screen = winnerScreen()
        history.append(current_screen)
    elif current_screen == 'desert_2':
        current_screen = drawDesert2()
        history.append(current_screen)
    elif current_screen == 'landscape_1':
        current_screen = landscape1()
        history.append(current_screen)
    elif current_screen == 'optional_quiz_1':
        current_screen = optionalQuiz1()
        history.append(current_screen)
    elif current_screen == 'landscape_2':
        current_screen = landscape2()
        history.append(current_screen)
    elif current_screen == 'battleground':
        current_screen = battleground()
        history.append(current_screen)
    elif current_screen == 'battleground_2':
        current_screen = battleground2()
        history.append(current_screen)
    elif current_screen == 'landscape_3':
        current_screen = landscape3()
        history.append(current_screen)
    elif current_screen == 'valleyofthekings_outside1':
        current_screen = valleyofthekings_outside1()
        history.append(current_screen)
    elif current_screen == 'optional_quiz_2':
        current_screen = optionalQuiz2()
        history.append(current_screen)
    elif current_screen == 'valleyofthekings_outside2':
        current_screen = valleyofthekings_outside2()
        history.append(current_screen)
    elif current_screen == 'finding_tomb':
        current_screen = findingTomb()
        history.append(current_screen)
    elif current_screen == 'found_tomb':
        current_screen = foundTomb()
        history.append(current_screen)
    elif current_screen == 'coffin':
        current_screen = coffin()
        history.append(current_screen)
    elif current_screen == 'compulsory_quiz':
        current_screen = compulsoryQuiz()
        history.append(current_screen)
    elif current_screen == 'congratulatory_screen':
        current_screen = congratulatoryScreen()
        history.append(current_screen)
    elif current_screen == 'coffin2':
        current_screen = coffin2()
        history.append(current_screen)
    elif current_screen == 'ay_mummification':
        current_screen = ayMummification()
        history.append(current_screen)
    elif current_screen == 'time_machine_ancient2':
        current_screen = timeMachineAncient2()
        history.append(current_screen)
    elif current_screen == 'mask_in_museum':
        current_screen = maskInMuseum()
        history.append(current_screen)
    elif current_screen == 'end_game':
        current_screen = endGame()
        history.append(current_screen)
        # settings
    elif current_screen == 'settings':
        current_screen = Settings()
    elif current_screen == 'instructions':
         win.blit(instructionsBg, (0,0))
         if backButtonForInstructions.drawButton() == True:
             current_screen = 'settings'
    elif current_screen == 'back':
        current_screen = history.pop()
        current_screen = history.pop() # the front of the stack
        # shop
    elif current_screen == 'shop':
        current_screen = drawShop()
    elif current_screen == 'bought_message':
        win.blit(item_purchased, (0,0))
        if backButtonAfterPurchase.drawButton():
            current_screen = 'shop'
    elif current_screen == 'equipmessage':
        win.blit(equip_message, (0,0))
        if backButtonAfterPurchase.drawButton():
            current_screen = 'shop'
    elif current_screen == 'not_enough_money':
        win.blit(not_enough, (0, 0))
        if backButtonAfterPurchase.drawButton():
            current_screen = 'shop'
    elif current_screen == 'closeShop':
        current_screen = history.pop()
        current_screen = history.pop()
        
    pygame.display.update()
           
pygame.quit()
