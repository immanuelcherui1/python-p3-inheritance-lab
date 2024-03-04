#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, first_name, last_name):
        User.__init__(self, first_name, last_name)
        self.knowledge = []
        
        
    def learn(self, Knowledge):
        if isinstance(Knowledge, str):
            self.knowledge.append(Knowledge)