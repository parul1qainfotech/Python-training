class Chapter:
    def __init__(self,subject,pages,marks,name):
        self.subject = subject
        self.pages = pages
        self.marks = marks
        self.name = name
class Exam:
    def __init__(self,examName,chapterList):
        self.examName = examName
        self.chapterList = chapterList
    def findMaximumChapterByPage(self):
        max_obj = max(self.chapterList, key=lambda x:x.pages)
        return max_obj
    def sortChapterByMarks(self):
        ans1 = sorted(self.chapterList, key=lambda yy:yy.marks)
        ans2 = []
        for i in ans1:
            ans2.append(i.marks)
        if len(ans2)==0:
            return None
        else:
            return ans2
     
 
count = int(input())
chapterList = []
for i in range(count):
    subject = input()
    pages = int(input())
    marks = int(input())
    name = input()
    chap = Chapter(subject,pages,marks,name)
    chapterList.append(chap)
ex = Exam("ABC",chapterList)
x = ex.findMaximumChapterByPage()
y = ex.sortChapterByMarks()
print(x.subject)
print(x.pages)
print(x.marks)
print(x.name)
for i in range(len(y)):
    print(y[i])
