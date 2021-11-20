mass=[]

class OlimpTask:
    def __init__(self):
        self.name=0
        self.count_all=0
        self.count_complate=0
    def get_name(self):
        return self.name
    def get_count_all(self):
        return self.count_all
    def get_count_complate(self):
        return self.count_complate
    def set_name(self,nm):
        self.name=nm
    def set_count_all(self,all):
        self.count_all=all
    def set_count_complate(self,comp):
        self.count_complate=comp

class TheMoreTheBetter(OlimpTask):


    def __init__(self):
        super().__init__()
        self.max_point=0

    def get_max_point(self):
        return  self.max_point

    def set_max_point(self,max):
        self.max_point=max

    def CalcPoint(self):
        return ((self.get_count_complate()*self.get_max_point())/self.get_count_all())

    def __str__(self):
        return "Ім'я - {}  " \
               "Кількість прикладів = {}   " \
               "Кількість вирішених = {}    " \
               "Максимальна кількість балів = {}    " \
               "Отримані бали = {}".format(mass[i].get_name(),
                                            mass[i].get_count_all(),
                                            mass[i].get_count_complate(),
                                            mass[i].get_max_point(),
                                            round(mass[i].CalcPoint(),2))

class TheFasterTheBetter(OlimpTask):

    def __init__(self):
        super().__init__()
        self.user_time=0
        self.best_time=0
        self.percent=0
        self.max_point=0

    def get_user_time(self):
        return self.user_time

    def get_best_time(self):
        return self.best_time

    def get_percent(self):
        return self.percent

    def get_max_point(self):
        return self.max_point

    def set_user_time(self,time):
        self.user_time=time

    def set_best_time(self,best):
        self.best_time=best

    def set_percent(self,perc):
        self.percent = perc

    def set_max_point(self, max):
        self.max_point = max

    def CalcPoint(self):
        if self.get_max_point() - ((self.get_user_time()-self.get_best_time())*self.get_percent())>0:
            return (self.get_max_point() - ((self.get_user_time()-self.get_best_time())*self.get_percent()))
        else:
            return 0

    def __str__(self):
        return "Ім'я - {}  " \
               "Час виконання = {}  " \
               "Найкращий час = {}  " \
               "Відсоток зниження за хв  = {}   " \
               "Максимальна кількість балів = {}    " \
               "Отримані бали = {}".format(mass[i].get_name(),
                                           mass[i].get_user_time(),
                                           mass[i].get_best_time(),
                                           mass[i].get_percent(),
                                           mass[i].get_max_point(),
                                           round(mass[i].CalcPoint(), 2))


max = int(input("Максимальна кількість балів для учасників олімпіади\n"))
perc = float(input("Відсоток зниження за хвилину відставання\n"))
best_time=9999999
menu = 1
while menu == 1:
    a = 1
    n = int(input("Виберіть дію \n"
                  "1-додати об'єкт класу TheMoreTheBetter\n"
                  "2-додати об'єкт класу TheFasterTheBetter\n"
                  "3-вивести список \n"
                  "4-відсортувати по сумі балів\n"
                  "5-сума балів, які здобули всі учасники\n"
                  "0-вийти з програми\n"))

    if(n==1):
        while a==1:
            name = str(input("ім'я\n"))
            all = int(input("кількість прикладів\n"))
            comp = int(input("кількість вирішених\n"))
            b=1
            while b == 1:
                if int(all)>=int(comp):
                    obj = TheMoreTheBetter()
                    obj.set_name(name)
                    obj.set_count_all(all)
                    obj.set_count_complate(comp)
                    obj.set_max_point(max)
                    mass.append(obj)
                    b=0
                else:
                    comp = input("кількість вирішених, не може бути більшою за загальну введіть ще раз\n")
                    b=1
            a = int(input("Продовжити - 1\n"))

    if (n == 2):
        while a == 1:
            name = str(input("ім'я\n"))
            time = int(input("час в хвилинах\n"))

            if time<best_time:
                best_time=time
                for i in range(len(mass)):
                    if type(mass[i]) == TheFasterTheBetter:
                        mass[i].set_best_time(best_time)

            obj = TheFasterTheBetter()
            obj.set_name(name)
            obj.set_user_time(time)
            obj.set_best_time(best_time)
            obj.set_percent(perc)
            obj.set_max_point(max)
            mass.append(obj)
            a = int(input("Продовжити - 1\n"))

    if (n == 3):
        for i in range (len(mass)):
            print (mass[i])
    if (n == 4):
        N = len(mass)
        for i in range(N - 1):
            m = mass[i].CalcPoint()
            p = i
            for j in range(i + 1, N):
                if m > mass[j].CalcPoint():
                    m = mass[j].CalcPoint()
                    p = j
            if p != i:
                t = mass[i]
                mass[i] = mass[p]
                mass[p] = t

        print("Відсортовані учасники по балах")
        for i in range (len(mass)):
            print(mass[i])

    if (n == 5):
        print("Сума всіх балів набраних учасниками")
        sumall=0
        for i in range (len(mass)):
            sumall+=mass[i].CalcPoint()
        print(str(round(sumall,2)))
    if (n == 0):
        menu=0

