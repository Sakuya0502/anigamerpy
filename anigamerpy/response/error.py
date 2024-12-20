#錯誤訊息

class ErrorType:
    #無結果
    def no_result():
        return 'No result.'
    
    #爬取失敗
    def status_error(error_code):
        return 'Requests failed: {}'.format(str(error_code))