class morse:
    def __init__(self, s = "di dit dah"):
        self.res = "."
        string = s.split()
        self.flag_end = True
        self.flag_tilda = False
        self.flag_words = False
        self.flag = False
        if len(string) > 1:
            self.flag_words = True
        else:
            string = s
            self.res = ""
        if len(string) == 2:
            self.plus = string[0]
            self.plusdot = string[0]
            self.minus = string[1]
        elif len(string) >= 3:
            self.plus = string[0]
            self.plusdot = string[1]
            self.minus = string[2]
            if s[-1] == " ":
                self.res = " "
            if len(string) == 4:
                self.res = string[-1]
    def __pos__(self):
        if self.flag_words == True:
            if self.flag_end == True and self.flag_tilda == False:
                self.res = self.plusdot + self.res
            elif self.flag_tilda == True:
                self.res = self.plusdot + self.res
                self.flag_tilda = False
            else:
                self.res = self.plus + " " + self.res
        else:
            if self.flag_end == True and self.flag_tilda == False:
                self.res = self.plusdot + self.res
            elif self.flag_tilda == True:
                self.res = self.plusdot + self.res
                self.flag_tilda = False
            else:
                self.res = self.plus + self.res
        self.flag_end = False
        return self
    def __neg__(self):
        if self.flag_words == True:
            if self.flag_end == True and self.flag_tilda == False:
                self.res = self.minus + self.res
            elif self.flag_tilda == True:
                self.res = self.minus + self.res
                self.flag_tilda = False
            else:
                self.res = self.minus + " " + self.res
        else:
            if self.flag_end == True and self.flag_tilda == False:
                self.res = self.minus + self.res
            elif self.flag_tilda == True:
                self.res = self.minus + self.res
                self.flag_tilda = False
            else:
                self.res = self.minus + self.res
        self.flag_end = False
        return self
    
    def __invert__(self):
        self.flag_tilda = True
        if self.flag_words == True:
            self.res = ", " + self.res
        else:
            self.res = " " + self.res
        return self
            
    def __repr__(self):
        return self.res

