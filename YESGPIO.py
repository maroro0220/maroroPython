import RPi.GPIO as GPIO
import time

class GPIO_Base:
    def __init__( self, pin ):
        GPIO.setmode( GPIO.BCM )
        GPIO.setwarnings( False )
        self.pin = pin
        self.pwm_start = 0

    def set_output( self, pin ):
        GPIO.setup( pin, GPIO.OUT )

    def set_input( self, pin ):
        GPIO.setup( pin, GPIO.IN )

    def set_PWM( self, pwm_start):
        self.pwm_start = pwm_start
        self.PWM = GPIO.PWM( self.pin, self.pwm_start )

class LedControl( GPIO_Base ):
    LEDS = [ 14, 15 ]

    def __init__( self ):
        super().__init__( self.LEDS )
        super().set_output( self.LEDS )
        GPIO.output( self.pin, False )

    def led1_on( self ):
        GPIO.output( self.pin[0], True )

    def led2_on( self ):
        GPIO.output( self.pin[1], True )

    def leds_on( self ):
        GPIO.output( self.pin, True)

    def led1_off( self ):
        GPIO.output( self.pin[0], False )

    def led2_off( self ):
        GPIO.output( self.pin[1], False )

    def leds_off( self ):
        GPIO.output( self.pin, False)

    def led_jog( self ):
        self.jog = JogSwitch()
        while True:
            dir = self.jog.check_jog()
            time.sleep(1)
            if dir == 'up':
                print(dir)
                self.led1_on()
            elif dir == 'down':
                print(dir)
                self.led2_on()
            elif dir == 'left' or dir == 'center':
                print(dir)
                self.leds_on()
            elif dir == 'right':
                print(dir)
                self.leds_off()

class DCMotor( GPIO_Base ):
    MOTOR_PIN = { 'm_pwm': 12, 'm_p' : 4, 'm_n' : 25 }

    def __init__( self ):
        super().__init__( self.MOTOR_PIN['m_pwm'] )
        super().__init__( self.MOTOR_PIN['m_p'] )
        super().__init__( self.MOTOR_PIN['m_n'] )
        super().set_output( self.MOTOR_PIN['m_pwm'] )
        super().set_output( self.MOTOR_PIN['m_p'] )
        super().set_output( self.MOTOR_PIN['m_n'] )
        self.EN = super().set_PWM( self.MOTOR_PIN['m_pwm'], 100 )
        self.EN.start(100)

    def cw( self ):
        GPIO.output( self.pin['m_pwm'], True )
        GPIO.output( self.pin['m_p'], True )
        GPIO.output( self.pin['m_n'], False )

    def ccw( self ):
        GPIO.output( self.pin['m_pwm'], True )
        GPIO.output( self.pin['m_p'], False )
        GPIO.output( self.pin['m_n'], True )

    def stop( self ):
        GPIO.output( self.pin['m_pwm'], False )
        GPIO.output( self.pin['m_p'], False )
        GPIO.output( self.pin['m_n'], False )

    def changespeed( self, duty ):
        self.EN.ChangeDutyCycle( duty )

class JogSwitch( GPIO_Base ):
    #jog  [ up, dn, lt, rt, cen]
    JOG = [  5,  6, 16, 20,  21]
    DIR = [ 'up', 'down', 'left', 'right', 'center']
    STAT = [  0,  0,  0,  0,  0]

    def __init__( self ):
        for x in self.JOG:
            super().__init__( x )
            super().set_input( x )

    def check_jog( self ):
        while True:
            for i in range( 5 ):
                if GPIO.input( self.JOG[i] ):
                    return self.DIR[i]



class CharacterLCD( GPIO_Base ):
    LCD_RS  = 23
    LCD_RW  = 24
    LCD_E   = 26
    LCD_D4  = 17
    LCD_D5  = 18
    LCD_D6  = 27
    LCD_D7  = 22

    #define some device constants
    LCD_WIDTH   = 16
    LCD_CHR     = True
    LCD_CMD     = False

    LCD_LINE_1 = 0x80
    LCD_LINE_2 = 0xC0

    #Time constants
    E_PULSE = 0.0005
    E_DELAY = 0.0005

    def __init__( self ):
        super().__init__( self.LCD_RS )
        super().__init__( self.LCD_RW )
        super().__init__( self.LCD_E )
        super().__init__( self.LCD_D4 )
        super().__init__( self.LCD_D5 )
        super().__init__( self.LCD_D6 )
        super().__init__( self.LCD_D7 )


    def main( self ):
        GPIO.setwarnings( False )
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( self.LCD_E, GPIO.OUT )
        GPIO.setup( self.LCD_RS, GPIO.OUT )
        GPIO.setup( self.LCD_D4, GPIO.OUT )
        GPIO.setup( self.LCD_D5, GPIO.OUT )
        GPIO.setup( self.LCD_D6, GPIO.OUT )
        GPIO.setup( self.LCD_D7, GPIO.OUT )

        #initialize display
        self.lcd_init()

        while True:
            #Send some text
            self.lcd_string( "Raspberry Pi", self.LCD_LINE_1 )
            self.lcd_string( "16x2 LCD Test", self.LCD_LINE_2 )
            time.sleep( 3 )

            #Send some text
            self.lcd_string("1234567890123456", self.LCD_LINE_1 )
            self.lcd_string("abcdefghijklmnop", self.LCD_LINE_2 )
            time.sleep( 3 )

    def lcd_init( self ):
        #initialize display
        self.lcd_byte(0x33, self.LCD_CMD ) # 00110011 initialze
        self.lcd_byte(0x32, self.LCD_CMD ) # 00110010 initialze
        self.lcd_byte(0x06, self.LCD_CMD ) # 00000110 cursor move direction
        self.lcd_byte(0x0C, self.LCD_CMD ) # 00001101 display on cursor off blink off
        self.lcd_byte(0x28, self.LCD_CMD ) # 00101000 data length, number of lines, font size
        self.lcd_byte(0x01, self.LCD_CMD ) # 00000001 clear display
        time.sleep( self.E_DELAY )

    def lcd_byte( self, bits, mode ):
        # send byte to data pins
        # bits = data
        # mode = True for character
        #        False for command

        GPIO.output( self.LCD_RS, mode )

        #High bits
        GPIO.output( self.LCD_D4, False )
        GPIO.output( self.LCD_D5, False )
        GPIO.output( self.LCD_D6, False )
        GPIO.output( self.LCD_D7, False )

        if bits & 0x10 == 0x10:
            GPIO.output( LCD_D4, True )
        if bits & 0x20 == 0x20:
            GPIO.output( LCD_D5, True )
        if bits & 0x40 == 0x40:
            GPIO.output( LCD_D6, True )
        if bits & 0x80 == 0x80:
            GPIO.output( LCD_D7, True )

        #Toggle 'Enable' pin
        lcd_toggle_enable()

        #Low bits
        GPIO.output( LCD_D4, False )
        GPIO.output( LCD_D5, False )
        GPIO.output( LCD_D6, False )
        GPIO.output( LCD_D7, False )

        if bits & 0x01 == 0x01:
            GPIO.output( LCD_D4, True )
        if bits & 0x02 == 0x02:
            GPIO.output( LCD_D5, True )
        if bits & 0x04 == 0x04:
            GPIO.output( LCD_D6, True )
        if bits & 0x08 == 0x08:
            GPIO.output( LCD_D7, True )

        #Toggle 'Enable' pin
        lcd_toggle_enable()

    def lcd_toggle_enable():
        #Toggle enable
        time.sleep( E_DELAY )
        GPIO.output( LCD_E, True )
        time.sleep( E_PULSE )
        GPIO.output( LCD_E, False )
        time.sleep( E_DELAY )

    def lcd_string( message, line ):
        #send string to display
        message = message.ljust( LCD_WIDTH, " ")
        lcd_byte( line, LCD_CMD )
        for i in range( LCD_WIDTH ):
            lcd_byte( ord(message[i]), LCD_CHR )
            # 파이썬 내장 함수, ord(): 아스키코드값 리턴해주는 함수
