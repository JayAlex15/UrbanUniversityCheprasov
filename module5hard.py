import time


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def add(self, *videos):
        for video in videos:
            self.videos.append(video)

    def get_videos(self, search_word):
        searched_videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                searched_videos.append(video.title)
        return searched_videos

    def watch_video(self, videotitle):
        if self.current_user != None:
            for video in self.videos:
                if videotitle == video.title:
                    if video.adult_mode:
                        if self.current_user.age >= 18:
                            for sec in range(video.duration):
                                video.time_now += 1
                                time.sleep(1)
                                print(video.time_now, end = " ")
                            print("Конец видео")
                        else:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

    def register(self, nickname, password, age):
        log_check = True
        for user in self.users:
            if nickname == user.nickname:
                log_check = False
        if log_check:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
