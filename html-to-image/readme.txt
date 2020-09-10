html->img 모듈 사용방법은

ex) test=CONVERT('1300', '20200902', 'E:/mod_cnts/1300.jpeg')
    row=test.get_info()
    test.convert_html(row)

    CONVERT('SN', 'D_CRT", 'path') 입력한다.

혹시나 img 파일을 옮길 경우 
html_img.py 에서 config = img.config(wkhtmltoimage="C:/Users/PycharmProject/Test03/img/wkhtmltopdf/bin/wkhtmltoimage.exe") 에서 
경로 수정을 해줘야 한다.
    