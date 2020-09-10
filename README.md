# html-to-image

## 해당 모듈은 기존 방식인 RTBL_MOD_CNTS_ATYPE의 MOD_SN, D_MOD_CRT와 저장 경로를 parameter값에 해당하는 html코드를 jpeg로 해당 경로에 저장하는 모듈이다.

설정단계
---
1. html_img.py의 66번줄에서 config = img.config(wkhtmltoimage="E:/Test03/html-to-image/wkhtmltopdf/bin/wkhtmltoimage.exe")에서 wkhtmltoimage 값의 경로를 해당 경로에 맞게 수정
2. import 하기 전 import sys를 하고, sys.path.insert(0, 'html-to-image.py 경로')




사용 예시
==
<pre>
<code>
import sys
sys.path.insert(0, 'C:\\Users\\KimJeongho\\Desktop\\git_test\\html-to-image')
import html_img 
test=html_img.CONVERT(MOD_SN, D_MOD_CRT, 'E:')
row = test.get_info()
test.convert_html(row)
</code>
</pre>

