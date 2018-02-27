#coding:utf-8
'''实现班级的增删改查'''
from cfg import vcode,SchoolClassSearchUrl
import requests
class SchoolClassLib():
    def __init__(self):
        self.gvode=vcode
    def list_school_class(self,gradeid):
        '''查询课程'''
        if gradeid==None:
           param = {
                  'vcode':self.gvode,
                   'action':'list_classes_by_schoolgrade'
           }  #字典-参数列表
        else :
            param={
                'vcode': self.gvode,
                'action': 'list_classes_by_schoolgrade',
                'gradeid':  gradeid
            }
            responses=requests.get(SchoolClassSearchUrl,params=param)
            bodyDict=responses.json()
            return bodyDict
    def add_class(self,grade,name,studentlimit):
        '''增加课程'''
        parm={
            'vcode':self.gvode,
            'action':'add',
            'grade':int(grade),
            'name':name,
            'studentlimit':int(studentlimit)
        }
        reponses=requests.post(SchoolClassSearchUrl,params=parm)
        return  reponses.json()
    def delete_school_class(self,classid):
        '''删除课程'''
        parm={
            'vcode':self.gvode,
            'classid':classid
        }
        reponses=requests.delete(SchoolClassLib,params=parm)
        return reponses.json()

    def modify_school_class(self,classid,name,studentlimit):
      '''修改课程'''
      parm={
          'vcode':self.gvode,
          'action': 'modify',
          'classid':int(classid),
          'name':name,
          'studentlimit':int(studentlimit)
        }
      reponses=requests.put(SchoolClassSearchUrl,params=parm)
      return  reponses.json()

if __name__==  '__main__':
    school=SchoolClassLib()
    ret=school.add_class(3,"实验1班",80)