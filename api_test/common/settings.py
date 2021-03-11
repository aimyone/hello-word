'''全局变量'''
import os
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#文件绝对路径,逐渐取出文件夹
LOG_PATH=os.path.join(BASE_PATH,'logs')#log路径
REPORT_PATH=os.path.join(BASE_PATH,'report')#报告的路径
CASE_PATH=os.path.join(BASE_PATH,'cases')#存放用例的路径
CORE_CASE_PATH=os.path.join(BASE_PATH,'bin')#生成用例的路径
CORE_CASE_PATH1=os.path.join(BASE_PATH,'api_verify')#生成的用例的存放路径
FILE_PATH = os.path.join(BASE_PATH,'core')
TOOLS_PATH = os.path.join(BASE_PATH,'tools')
# phone=
# username=
# passwd=
# code=
# SCHEME='http'
# SCHEME_S='https'
# print(LOG_PATH,aa,bb)