import threading
import timer
from enum import Enum
# Session response means the seesion with a query and response
# It could answer the question which is asked by users
# And it could give feedback to the QA pairs.
class SessionState(Enum):
    hello = 0
    asksuccess = 1
    askfail = 2
    postask = 3

reply_array=['您好,欢迎使用小助手,描述您的问题并带上表情/:?即可提问,快来试试吧!',
'',
'出错了,请尽快联系小助手开发者!'
]

'''
Stu: hi
Agent: 您好,欢迎使用小助手,描述您的问题并带上表情/:?即可提问,快来试试吧!
Stu: 请问verilog中assign 和 always有什么区别呢/:?
Agent: 您好，以下是为您检索到的答案:
标题:verilog 语法问题
原问题:verilog 中 assign 和 always区别
原答案:
1. assign 用于组合逻辑
2. always 用于时序逻辑
查看原文:
http://xxx.cn

如果该回答未解决你的问题，你可以使用
Stu:
'''
class SessionList():
    # SessionList stores all sessions connected
    session_list = {}
    def SessionList(self):
        return None
    def handle_input(self,_user_id,_input):
        valid_input = _input
        # default reply message
        response_query = reply_array[-1]
        # /:? means input is a question
        if '/:?' in _input:
            # get the valid query string
            valid_input = _input.replace('/:?','').strip()
            result = self.ask(_user_id,valid_input)
            response_query = reply_array[result[0]] + '\n' + result[1]
        elif '/:strong' in _input:
            # /:strong means auto-post to forum
            valid_post_content = _input.replace('/:strong','').strip()
            result = self.post(_user_id,valid_post_content)


    def hello(self,_user_id):
        self.session_list.update(_user_id,DialogueSession())
        # return hello state
        return reply_array[SessionState.hello]
    def ask(self,_user_id,_query):
        if not self.session_list.has_key(_user_id):
            self.session_list[_user_id] = DialogueSession()
        self.session_list[_user_id].query = _query
        return SessionState.asked
    def post(self,_user_id,_post_content):
        
    def post_title(self,_user_ud,_post_title):
    
        

class DialogueSession():
    # session_id is the identifier of a session
    session_id = None
    # user_id means 
    user_id = None
    # query means the question asked by user
    query = None
    # time to live in
    time_to_live = 10
    def isLive(self):
        if self.time_to_live <= 0:
            return False
        else:
            return True