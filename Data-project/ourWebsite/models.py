
from django.db import models
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


# Create your models here.


class Uni(models.Model):
    @abstractmethod
    def createMajors():
        pass

    @abstractmethod
    def createTuitionFees():
        pass


class LAU(Uni, models.Model):

    def __init__():
        return

    def createMajors():
        return LAUMajors().getMajors()

    def createTuitionFees():
        return LAUMajors().getFees()


class USEK(Uni, models.Model):

    def __init__():
        return

    def createMajors():
        return USEKMajors().getMajors()

    def createTuitionFees():
        return USEKMajors().getFees()


class UOB(Uni, models.Model):

    def __init__():
        return

    def createMajors():
        return UOBMajors().getMajors()

    def createTuitionFees():
        return UOBMajors().getFees()


class NDU(Uni, models.Model):

    def __init__():
        return

    def createMajors():
        return NDUMajors().getMajors()

    def createTuitionFees():
        return NDUMajors().getFees()


class MU(Uni, models.Model):

    def __init__():
        return

    def createMajors():
        return MUMajors().getMajors()

    def createTuitionFees():
        return MUMajors().getFees()


class AUB(Uni, models.Model):

    def __init__():
        return

    def createMajors():
        return AUBMajors().getMajors()

    def createTuitionFees():
        return AUBMajors().getFees()


class Majors(models.Model):
    pass


class Fees(models.Model):
    pass


class LAUMajors(Majors, models.Model):

    def __init__(self):
        self.majors = list()
        self.fees = list()
        url = "https://www.lau.edu.lb/fees/2022-2023/"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        tbody = doc.find_all("tbody")
        trs1 = tbody[0].contents

        x = len(trs1)
        for i in range(1, x-1, 2):
            tds = trs1[i].contents
            major = tds[1].text
            price = tds[7].text
            if (i == 25) or (i == 73) or (i == 1):
                major = major[5:]
                price = price[5:]
            else:
                major = major[1:]
                price = price[5:]
            self.majors.append(major)
            self.fees.append(price)

    def getMajors(self):
        return self.majors

    def getFees(self):
        return self.fees


class LAUTuitionFees(Fees, models.Model):
    def getFees():
        return LAUMajors.getFees


class USEKMajors(Majors, models.Model):

    def __init__(self):
        self.majors = list()
        self.fees = list()
        url = "https://www.usek.edu.lb/en/university-fees/undergraduate-studies-1"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        tbodys = doc.find_all("tbody")

        y = len(tbodys)
        for j in range(2, y):
            trs1 = tbodys[j].contents
            x = len(trs1)
            for i in range(1, x-1, 2):
                tds = trs1[i].contents
                maj = tds[1].text
                major = maj[0:len(maj)-14]
                p = tds[3].text
                if (not "Cost" in p):
                    self.majors.append(major)
                    self.fees.append(p)

    def getMajors(self):
        return self.majors

    def getFees(self):
        return self.fees


class USEKTuitionFees(Fees, models.Model):
    def getFees():
        return USEKMajors.getFees


class UOBMajors(Majors, models.Model):

    def __init__(self):
        self.majors = list()
        url = "http://home.balamand.edu.lb/english/MajorsFrame.asp?id=1426&fid=49&PageName=Majors"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        tbody = doc.find_all("tbody")
        trs = tbody[0].contents
        x = len(trs)
        for i in range(7, x, 2):
            tds = trs[i].contents
            major = tds[1].text
            if ("\r\n\xa0" in major):
                t = major.index('\xa0')
                major = major[:t]
            if ("-\xa0" in major):
                major = major[3:]
            if ("\xa0-\xa0" in major):
                n = major.index('\xa0-\xa0')
                major = major[:n]
            if ("and\xa0" in major):
                m = major.index('and\xa0')
                major = major[:m-1]
            if (major != "\n" and not "Faculty" in major and major != ""):
                self.majors.append(major)
                self.majors = list(map(lambda a: a.strip(), self.majors))
                self.majors = list(filter(None, self.majors))

    def getMajors(self):
        return self.majors

    def getFees(self):
        return


class UOBTuitionFees(Fees, models.Model):
    def getFees():
        return UOBMajors.getFees


class NDUMajors(Majors, models.Model):

    def __init__(self):
        self.majors = list()
        self.fees = list()
        url1 = "https://www.ndu.edu.lb/about-ndu/administration/offices/office-of-finance/tuition-and-fees"
        result1 = requests.get(url1)
        doc1 = BeautifulSoup(result1.text, "html.parser")
        tbody1 = doc1.find_all("tbody")
        trs1 = tbody1[0].contents
        x = len(trs1)
        for i in range(1, x, 2):

            td = trs1[i].contents
            major = td[1].text
            price = td[5].text
            self.majors.append(major)
            self.fees.append(price)

        url2 = "https://www.ndu.edu.lb/academics/fields-of-study"
        result2 = requests.get(url2)
        doc2 = BeautifulSoup(result2.text, "html.parser")
        tbody2 = doc2.find_all("tbody")
        trs2 = tbody2[0].contents
        y = len(trs2)
        for i in range(1, y, 2):
            td = trs2[i].contents
            maj = td[1].text
            maj = maj[1:len(maj)]

            if ("\xa0" in maj):
                t = maj.index('\xa0')
                maj = maj[:t]

            self.majors.append(maj)
            if 'engineer' in maj.lower():
                self.fees.append("470")
            elif 'business' in maj.lower():
                self.fees.append("395")
            elif 'architecture' in maj.lower():
                self.fees.append("440")
            else:
                self.fees.append("380")

    def getMajors(self):
        return self.majors

    def getFees(self):
        return self.fees


class NDUTuitionFees(Fees, models.Model):
    def getFees():
        return NDUMajors.getFees


class MUMajors(Majors, models.Model):

    def __init__(self):
        self.majors = list()
        self.fees = list()
        url = "http://www.mu.edu.lb/en/study-at-mu/mu-tuition-fees/"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        tbody = doc.find_all("tbody")
        trs1 = tbody[0].contents

        x = len(trs1)
        for i in range(1, x, 2):

            tds = trs1[i].contents
            major = tds[1].text
            maj = major[1:len(major)-1]
            price = tds[3].text
            p = price[1:len(price)-1]
            self.majors.append(maj)
            self.fees.append(p)

    def getMajors(self):
        return self.majors

    def getFees(self):
        return self.fees


class MUTuitionFees(Fees, models.Model):
    def getFees():
        return MUMajors.getFees


class AUBMajors(Majors, models.Model):

    def __init__(self):
        self.majors = ['Agri-Business', 'Agriculture', 'Applied Mathematices', 'Arabic', 'Archeology', 'Architecture', 'Art History', ' Biology', 'Business Administration', 'Chemical Engineering', 'Chemistry', 'Civil and Environmental Engineering', 'Computer and Communications Engineering', 'Computer Science', 'Construction Engineering', 'Economics', 'Electrical and Computer Engineering', 'Elementary Education', 'English Language', 'English Literature', 'Environmental Health', 'Food Sciences and Management',
                       'Geology', 'Graphic Design', 'Health Communication', 'History', 'Industrial Engineering', 'Landscape Architecture', 'Mathematics', 'Mechanical Engineering', 'Media and Communication', 'Medical Audiology Sciences', 'Medical Imaging Sciences', 'Medical Laboratory Sciences', 'Nursing', 'Nutrition and Dietetics', 'Petroleum Geosciences', 'Philosophy', 'Physics', 'Political Studies', 'Psychology', 'Public Administration', 'Sociology-Anthropology', 'Statistics', 'Studio Arts']

    def getMajors(self):
        return self.majors


class AUBTuitionFees(Fees, models.Model):
    def getFees():
        return
