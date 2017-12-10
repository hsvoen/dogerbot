import time
import types

class Alarm:

    def __init__(self,weekday,hour,minute,every_day = False, action=None):
        ''' Sets parameters for the alarm.

        Input:
        weekday: Values 0-6, going from monday to sunday. Only used if every_day flag is not set
        hour: Values 0-23. Which hour of the day the alarm is set to.
        minute: values 0-59. Which minute in the hour the alarm is set to trigger
        every_day: Boolean value. If the alarm should trigger every day at the given time, set this to true
        action: The action that will be taken when an alarm is triggered. It is ignored if None, printed if a string and called if a function
        '''

        self.weekday = weekday
        self.hour = hour
        self.minute = minute
        self.every_day = every_day
        self.triggered_today = False #Flag saying if the alarm have allready triggered today or not.
        self.last_triggered = time.struct_time((0,0,0,0,0,0,0,0,0,0)) # stores the last time the alarm was triggered
        self.action = action

    def do_action(self):
        '''
            Calls the action given by the constructor.

            If action is none, it is ignored, it will be printed if a string, and called if a function. Other input is ignored.
        '''
        
        if self.action == None:
            return
        elif type(self.action) == "<class 'str'>":
            print(self.action)
        elif callable(self.action):
            self.action()

    def check_alarm(self):
        ''' Checks if the alarm should trigger or not. Returns true on alarm trigger and false otherwise 

        '''
        cur_time = time.localtime()

        if self.triggered_today and (self.last_triggered.tm_mday != cur_time.tm_mday):
            triggered_today = False

        if self.triggered_today: #Alarm have allready been triggered.
            return False


        if self.every_day or ( not selv.every_day and self.weekday == cur_time.tm_wday): #If the alarm is every day or it is the right day
            #print("self hour: {}, current hour: {}, self min: {}, cur min: {}".format(self.hour,cur_time.tm_hour,self.minute,cur_time.tm_min))
            if cur_time.tm_hour == self.hour and cur_time.tm_min == self.minute:
                self.triggered_today = True
                self.last_triggered = cur_time
                self.do_action()
                return True
            else:
                return False
        
        else:
            return False

    def print_alarm(self):
        ''' prints a formated string of the alarm parameters 
        '''
        if self.every_day:
            print("{}:{}".format(self.hour,self.minute))
        else:
            print("{}:{} on day {}".format(self.hour,self.minute, self.weekday))



class AlarmClock:

    def __init__(self):
        self.alarms = []

    def set_alarm(self,weekday,hour,minute,every_day=False, action=None):
        self.alarms.append(Alarm(weekday,hour, minute,every_day, action))

    def clear_alarms(self):
        self.alarms = []

    def print_alarms(self):
        for al in self.alarms:
           al.print_alarm() 

    def check_alarms(self):
        for al in self.alarms:
            if al.check_alarm():
                return True

        return False




if __name__ == '__main__':
    alarm = AlarmClock()
    
    cur_time = time.localtime()

#    alarm.set_alarm(0,cur_time.tm_hour,cur_time.tm_min+1,True,"Alarm triggered")
    alarm.set_alarm(0,cur_time.tm_hour,cur_time.tm_min+1,True,lambda: print("Alarm triggered"))
    
#alarm.print_alarms()
   
    while(True):
        #print(time.localtime())
        if(alarm.check_alarms()):
            #print("Alarm triggered")
            break
