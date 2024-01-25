import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def loginuser():
        lusername = config.get('commonInfo', 'Luser')
        return lusername

    @staticmethod
    def loginPassword():
        lpassword = config.get('commonInfo', 'Lpwd')
        return lpassword

    @staticmethod
    def signupusername():
        suser = config.get('commonInfo', 'suser')
        return suser
    @staticmethod
    def signuppassword():
        spwd = config.get('commonInfo', 'spwd')
        return spwd
