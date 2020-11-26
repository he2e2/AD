class Action:

    def __init__(self):
        self.hunger = 50
        self.clean = 50
        self.tired = 50
        self.study_cnt = 0
        self.age = 1
        self.stress = 50
        self.all = 50

        self.currentHunger = "■" * (self.hunger) + str(self.hunger) + "%"
        self.currentClean = "■" * (self.clean) + str(self.clean) + "%"
        self.currentTired = "■" * (self.tired) + str(self.tired) + "%"
        self.currentStress = "■" * (self.stress) + str(self.stress) + "%"
        self.currentAll = "■" * (self.all) + str(self.all) + "%"

    def feeding(self, food):
        if (self.hunger + int(food) <= 100 and self.hunger + int(food) >= 0):
            self.hunger += int(food)
            self.currentHunger = "■" * (self.hunger) + str(self.hunger) + "%"
            return self.currentHunger
        else:
            self.endingLife()

        # 배부름 게이지를 종합 게이지에 반영
        if (self.all < 0):
            self.endingLife()
        if (self.hunger >= 70):
            if (self.all + 10 >= 100):
                self.all = 100
            else:
                self.all += 10
        elif (self.hunger < 30):
            if (self.all - 10 >= 100):
                self.all = 100
            else:
                self.all -= 10

        self.currentAll = "■" * (self.all) + str(self.all) + "%"

    def washing(self, wash):
        if (self.clean + int(wash) < 0):
            self.endingLife()
        elif (self.clean + int(wash) >= 100):
            self.clean = 100
        else:
            self.clean += int(wash)

        # 청결 게이지를 종합 게이지에 반영
        if (self.all < 0):
            self.endingLife()
        if (self.clean >= 70):
            if (self.all + 10 >= 100):
                self.all = 100
            else:
                self.all += 10
        elif (self.clean < 30):
            if (self.all - 10 >= 100):
                self.all = 100
            else:
                self.all -= 10

        self.currentAll = "■" * (self.all) + str(self.all) + "%"
        self.currentClean = "■" * (self.clean) + str(self.clean) + "%"
        return self.currentClean

    def sleeping(self, sleep):
        if (self.tired - int(sleep) > 100):
            self.endingLife()
        elif (self.tired - int(sleep) <= 0):
            self.tired = 0
        else:
            self.tired -= int(sleep)

        # 피로 게이지를 종합 게이지에 반영
        if (self.all < 0):
            self.endingLife()
        if (self.tired >= 70):
            if (self.all - 10 <= 0):
                self.all = 0
            else:
                self.all -= 10
        elif (self.tired < 30):
            if (self.all + 10 >= 100):
                self.all = 100
            else:
                self.all += 10

        self.currentAll = "■" * (self.all) + str(self.all) + "%"
        self.currentTired = "■" * (self.tired) + str(self.tired) + "%"
        return self.currentTired

    def studying(self):
        self.study_cnt += 1  # 공부 횟수 카운팅
        # 스트레스 게이지바 업데이트
        if (self.stress + 30 > 100):
            self.endingLife()
        else:
            self.stress += 30
            self.currentStress = "■" * (self.stress) + str(self.stress) + "%"
            return self.currentStress

        # 스트레스 게이지를 종합 게이지에 반영
        if (self.all < 0):
            self.endingLife()
        if (self.stress >= 70):
            if (self.all - 10 <= 0):
                self.all = 0
            else:
                self.all -= 10
        elif (self.stress < 30):
            if (self.all + 10 >= 100):
                self.all = 100
            else:
                self.all += 10

        self.currentAll = "■" * (self.all) + str(self.all) + "%"

        # 공부 7번 하면 나이 + 1
        if self.study_cnt % 7 == 0:
            self.age += 1

    def playing(self):
        if (self.stress - 15 <= 0):
            self.stress = 0
        else:
            self.stress -= 15

        # 스트레스 게이지를 종합 게이지에 반영
        if (self.all < 0):
            self.endingLife()
        if (self.stress >= 70):
            if (self.all - 10 <= 0):
                self.all = 0
            else:
                self.all -= 10
        elif (self.stress < 30):
            if (self.all + 10 >= 100):
                self.all = 100
            else:
                self.all += 10

        self.currentAll = "■" * (self.all) + str(self.all) + "%"
        self.currentStress = "■" * (self.stress) + str(self.stress) + "%"
        return self.currentStress


    def endingLife(self):
        pass
        # self.character_text.setText("Game Over,,, 너 때문이야,,,༼ つ ◕_◕ ༽つ༼ つ ◕_◕ ༽つ")