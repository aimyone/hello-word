import flask,json
server = flask.Flask(__name__)
@server.route('/login')
#通联支付回调：acct=2088912532062181&appid=00201254&chnltrxid=2021031122001462181422084378&cmid=2088010464285785&cusid=55261107013HUPE&cusorderid=806712433697017984&fee=0&outtrxid=806712433697017984&paytime=20210311170324&sign=65A1303B1E98B06E67379C82FF7F26F1&signtype=MD5&termauthno=112149370002215860&termrefnum=2021031122001462181422084378&termtraceno=0&trxamt=1&trxcode=VSP511&trxdate=20210311&trxid=112149370002215860&trxstatus=0000
#前端回调接口：https://api-beta.yjyz.com/erp.transaction.api/collection/getPaidCollection
#第三方请求回调接口：http://api-beta.yjyz.com/collection/allinPayNotify

# @server.route('/login')
# def welcome():
#     data = {'code':0,'msg':'ganziwen登陆成功11','session_id':'sdf234sdsdfsdfs'}
#     return json.dumps(data,ensure_ascii=False, indent = 4)
#
# server.run(host='127.0.0.1',port=8888,debug=True) #5000

@server.route('/urldata') #get请求，参数在url里面的
def urlData():
    u = flask.request.args.get('ces')
    p = flask.request.args.get('ree')
    data  = {'username':u,'password':p}
    return json.dumps(data,ensure_ascii=False)

server.run(host='127.0.0.1',port=8888,debug=True) #5000