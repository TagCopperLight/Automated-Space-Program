class PID:
    def __init__(self, kp=1, ki=1, kd=1):
        self.__Kp = kp
        self.__Ki = ki
        self.__Kd = kd

        self.__total_error = 0
        self.__previous_error = 0

    def update(self, error):
        error = -error
        p = error
        i = self.__total_error + error
        d = error - self.__previous_error
        self.__previous_error = error
        self.__total_error += error
        return self.__Kp * p + self.__Ki * i + self.__Kd * d