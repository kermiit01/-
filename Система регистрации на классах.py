
class User:
    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
class Video:

    def __init__(self,title,duration,time_now=0,adult_mode=False):
        self.title = title
        self.duration = duration
        if time_now != 0:
            self.time_now = time_now
        else:
            self.time_now = 0
        if adult_mode != False:
            self.adult_mode = adult_mode
        else:
            self.adult_mode = False
class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self,nickname,password):
        if nickname in self.users:
            if hash(password) == hash(self.users[nickname]):
                self.current_user = nickname
    def register(self,nickname,password,age):
        if age < 18:
            print('По правилам сайта, вы слишком малы, для того что бы быть его пользователем')
        elif nickname not in self.users:
            self.users[nickname] = password, age
            print(f'Регистрация пройдена, {nickname} добро пожаловать!')
            self.current_user = nickname
        else:
            print('Пользователь с таким ником уже существует')

    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта')

    def add(self,*args):
        for a in args:
            self.videos.append(a)

    def get_videos(self,search):
        find=[]
        for i in self.videos:
            g=i.title
            if search.lower() in g.lower():
                find.append(i.title)
        print('Найденные видео:',find)
    def watch_video(self,video_title):
        if self.current_user == None:
            print('Видео доступны только для авторизованных пользователей')
        else:
            for video in self.videos:
                if video_title == video.title:
                    print(f'Начинается просмотр видео:"{video_title}"')
                    second = video.duration
                    while video.time_now != video.duration:
                        print(video.time_now+1)
                        video.time_now+=1



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.log_out()
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
