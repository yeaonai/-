class Settings():
    """储存《飞机大战》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bj_color = (230, 230, 230)

        # 飞机的设置
        self.ship_speed_factor = 1.5