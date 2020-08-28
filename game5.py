#记录学科成绩与学分
def secondYear():
    #输入
    name=input('请输入科目名称：')
    credit=input('请输入学分：')
    grade=input('请输入成绩：')
    #分割
    nameList=name.split(' ')
    creditList=credit.split(' ')
    gradeList=grade.split(' ')
    #打包
    result=list(zip(nameList,creditList,gradeList))
    print(result)

secondYear()
