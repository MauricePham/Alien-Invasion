class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (16,16,54)
        # Ship settings
        self.ship_speed = 7.0
        self.ship_limit = 3


        # Bullet settings
        self.bullet_speed = 8.5
        self.bullet_width = 2.5
        self.bullet_height = 15
        self.bullet_color = (102,204,0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # fleet direction of 1 represents right, -1 means left
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        self.ship_speed = 7.0 
        self.bullet_speed = 8.5
        self.alien_speed = 1.0 
        self.fleet_direction = 1 
        # Score settings
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

        
       

