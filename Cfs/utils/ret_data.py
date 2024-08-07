from django.http.response import JsonResponse


class ResponseData():
    def __init__(self, code=0, msg='', count=0, data=None):
        if data is None:
            data = []
        self.code = code,
        self.msg = msg,
        self.count = count,
        self.data = data,
        # 这里还没写完，记得要处理一下

    def to_json_response(self):
        return JsonResponse(self.__dict__, safe=True)
