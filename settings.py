class Settings():
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 700
        # Назначение цвета фона.
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # Параметры пули.
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        # Настройки пришельцев.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 влево.
        self.fleet_direction = 1

