import cx_Oracle
import imgkit as img


class CONVERT(object):

    def __init__(self, sn, crt, path):
        self.sn = sn
        self.crt = crt
        self.path = path

    def get_info(self):
        "# DB_RC_TEAM 접속"
        dsn = cx_Oracle.makedsn("tdb1_vip", 1521, service_name="TPDB")
        con_NEWS = cx_Oracle.connect("news_user", "news_user1", dsn)
        cursor_NEWS = con_NEWS.cursor()

        mod = """select  mod_sn, d_mod_crt, mod_cnts, img_row_size, img_col_size 
                       from news_user. rtbl_mod_cnts_atype 
                       where mod_sn=:mod_sn and d_mod_crt =: d_mod_crt"""


        cursor_NEWS.execute(mod, MOD_SN=self.sn, D_MOD_CRT=self.crt)
        row = cursor_NEWS.fetchone()

        return row

    def convert_html(self, row):
        html = row[2].read()
        sn=row[0]
        # print(sn)
        crt=row[1]
        print(crt)
        width=row[3]
        # print(width)
        height=row[4]
        # print(height)
        # with open('{}-{}.html'.format(sn,crt), 'w', encoding='utf-16') as h:
        #     h.write(html)

        path = self.path + '/mod_stk_{}_{}.jpeg'.format(crt, sn)
        if width ==None:
            if height==None:
                option={'quiet':'',
                        'disable-javascript': '',
                        'width': 900,
                        'height': 900,
                        }

            else:
                option = {'quiet': '',
                          'width': 900,
                          'height': 900,
                          'disable-javascript': ''
                          }



        else:
            option = {'quiet': '',
                      'width': width,
                      'height': height,
                      'disable-javascript':'',
                      }

        config = img.config(wkhtmltoimage="E:/Test03/html-to-image/wkhtmltopdf/bin/wkhtmltoimage.exe")
        img.from_string(html, '{}'.format(path), config=config, options=option)


if __name__ == "__main__":
    dsn = cx_Oracle.makedsn("tdb1_vip", 1521, service_name="TPDB")
    con_NEWS = cx_Oracle.connect("news_user", "news_user1", dsn)
    cursor_NEWS = con_NEWS.cursor()

    mod ="""select * from RTBL_MOD_CNTS_ATYPE where d_mod_crt =: d_mod_crt"""
    crt=input('날짜 입력 :')
    cursor_NEWS.execute(mod, d_mod_crt=crt)
    row = cursor_NEWS.fetchall()
    print(row)
    for info in row:
        print(info)
        sn=info[0]
        crt=info[1]

        test=CONVERT(sn, crt, 'E:\mod_cnts')
        row=test.get_info()
        test.convert_html(row)