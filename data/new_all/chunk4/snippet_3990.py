# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64391262/why-am-i-getting-the-error-attributeerror-mysqlcursor-object-has-no-attribu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(580286, _a_(580285, _n_(580284, "app", lambda: app), "route"), '/generate/file-manip',methods = ["GET","POST"]) # for saving the password(s)
def save_file():
  _l_(580469)

  pass_output_lst = [] #for passwords
  _l_(580287) #for passwords
  desc_output_lst = [] #for descriptions of the password
  _l_(580288) #for descriptions of the password
  encrypted_pass_output_lst = [] #storing passwords after encryption
  _l_(580289) #storing passwords after encryption
  encrypted_desc_output_lst = [] #storing descriptions of passwords after encryption
  _l_(580290) #storing descriptions of passwords after encryption
  UPLOAD_FOLDER = _c_(580293, _a_(580292, _n_(580291, "os", lambda: os), "getcwd"))
  _l_(580294)
  _a_(580296, _n_(580295, "app", lambda: app), "config")['UPLOAD_FOLDER'] = _n_(580297, "UPLOAD_FOLDER", lambda: UPLOAD_FOLDER)
  _l_(580298)
  if _a_(580300, _n_(580299, "request", lambda: request), "method") == "POST":
    _l_(580401)

    pass_file = _a_(580302, _n_(580301, "request", lambda: request), "files")['passfile'] #requesting the name of the password saving file
    _l_(580303) #requesting the name of the password saving file
    pass_file_Name = _c_(580307, _n_(580304, "secure_filename", lambda: secure_filename), _a_(580306, _n_(580305, "pass_file", lambda: pass_file), "filename")) #storing the name of the password saving file
    _l_(580308) #storing the name of the password saving file
    desc_file = _a_(580310, _n_(580309, "request", lambda: request), "files")['descfile'] #for the file storing descriptions of the file
    _l_(580311) #for the file storing descriptions of the file
    desc_file_Name =_c_(580315, _n_(580312, "secure_filename", lambda: secure_filename), _a_(580314, _n_(580313, "desc_file", lambda: desc_file), "filename"))
    _l_(580316)
    key = _c_(580319, _a_(580318, _n_(580317, "Fernet", lambda: Fernet), "generate_key")) # generating a key
    _l_(580320) # generating a key
    key_init = _c_(580323, _n_(580321, "Fernet", lambda: Fernet), _n_(580322, "key", lambda: key))  # storing the key for encrypting purpose
    _l_(580324)  # storing the key for encrypting purpose
    key_file = _a_(580326, _n_(580325, "request", lambda: request), "files")['keyfile']  # requesting the key saving file
    _l_(580327)  # requesting the key saving file
    key_file_name = _c_(580331, _n_(580328, "secure_filename", lambda: secure_filename), _a_(580330, _n_(580329, "key_file", lambda: key_file), "filename")) #storing the name of the key saving file
    _l_(580332) #storing the name of the key saving file
    file_lst = [_n_(580333, "pass_file_Name", lambda: pass_file_Name),_n_(580334, "desc_file_Name", lambda: desc_file_Name),_n_(580335, "key_file_name", lambda: key_file_name)]
    _l_(580336)

    for i in _a_(580338, _n_(580337, "GlobalData", lambda: GlobalData), "password"):
      _l_(580361)

      _c_(580348, _a_(580340, _n_(580339, "encrypted_pass_output_lst", lambda: encrypted_pass_output_lst), "append"), _c_(580347, _a_(580342, _n_(580341, "key_init", lambda: key_init), "encrypt"), _c_(580346, _n_(580343, "bytes", lambda: bytes), _a_(580345, _n_(580344, "i", lambda: i), "passwd"),encoding="utf-8")))
      _l_(580349)
      _c_(580359, _a_(580351, _n_(580350, "encrypted_desc_output_lst", lambda: encrypted_desc_output_lst), "append"), _c_(580358, _a_(580353, _n_(580352, "key_init", lambda: key_init), "encrypt"), _c_(580357, _n_(580354, "bytes", lambda: bytes), _a_(580356, _n_(580355, "i", lambda: i), "desc"),encoding="utf-8")))
      _l_(580360)
    with _c_(580364, _n_(580362, "open", lambda: open), _n_(580363, "pass_file_Name", lambda: pass_file_Name),"wb+") as k:
      _l_(580376)


      for i in _n_(580365, "encrypted_pass_output_lst", lambda: encrypted_pass_output_lst):
        _l_(580375)

        _c_(580369, _a_(580367, _n_(580366, "k", lambda: k), "write"), _n_(580368, "i", lambda: i))
        _l_(580370)
        _c_(580373, _a_(580372, _n_(580371, "k", lambda: k), "write"), b'\n')
        _l_(580374)

    with _c_(580379, _n_(580377, "open", lambda: open), _n_(580378, "desc_file_Name", lambda: desc_file_Name),"wb+") as k:
      _l_(580391)


      for i in _n_(580380, "encrypted_desc_output_lst", lambda: encrypted_desc_output_lst):
        _l_(580390)

        _c_(580384, _a_(580382, _n_(580381, "k", lambda: k), "write"), _n_(580383, "i", lambda: i))
        _l_(580385)
        _c_(580388, _a_(580387, _n_(580386, "k", lambda: k), "write"), b'\n')
        _l_(580389)
    with _c_(580394, _n_(580392, "open", lambda: open), _n_(580393, "key_file_name", lambda: key_file_name),"wb+") as k:
      _l_(580400)

      _c_(580398, _a_(580396, _n_(580395, "k", lambda: k), "write"), _n_(580397, "key", lambda: key))
      _l_(580399)


  if _a_(580403, _n_(580402, "GlobalData", lambda: GlobalData), "password") == []:
    _l_(580468)

    aux = _c_(580405, _n_(580404, "render_template", lambda: render_template), 'semantic-error.html',message = "Illegal method. Can't save the file when no password is generated")
    _l_(580406)
    return aux
  else: #[pass_file_Name,desc_file_Name,key_file_name]

        zip_obj = _c_(580409, _a_(580408, _n_(580407, "zipfile", lambda: zipfile), "ZipFile"), '/home/ZCDS4327/proj/cs_proj_pro_1/zipfile.zip','w')#creating a zip file and storing it inside an object
        _l_(580410)#creating a zip file and storing it inside an object

        #SQL Execution(an SQL table stores number of password generated by the user along with it's date and time)
        getDate = _c_(580414, _a_(580413, _a_(580412, _n_(580411, "datetime", lambda: datetime), "datetime"), "now")) #date and time of generating the passwords
        _l_(580415) #date and time of generating the passwords
        cursor = _c_(580418, _a_(580417, _n_(580416, "mydb", lambda: mydb), "cursor"))
        _l_(580419)
        n_passwd = _c_(580423, _n_(580420, "len", lambda: len), _a_(580422, _n_(580421, "GlobalData", lambda: GlobalData), "password")) #number of passwords generated
        _l_(580424) #number of passwords generated
        insert_query = "INSERT INTO password_table(n_passwd,c_date) VALUES(%s,%s)" %(_n_(580425, "n_passwd", lambda: n_passwd),_n_(580426, "getDate", lambda: getDate)) #inserting the passwords inside the table password_site
        _l_(580427) #inserting the passwords inside the table password_site
        _c_(580431, _a_(580429, _n_(580428, "cursor", lambda: cursor), "exceute"), _n_(580430, "insert_query", lambda: insert_query))
        _l_(580432)
        _c_(580435, _a_(580434, _n_(580433, "mydb", lambda: mydb), "commit"))
        _l_(580436)


        for i in _n_(580437, "file_lst", lambda: file_lst):
          _l_(580445)

          _c_(580443, _a_(580439, _n_(580438, "zip_obj", lambda: zip_obj), "write"), _n_(580440, "i", lambda: i),compress_type =_a_(580442, _n_(580441, "zipfile", lambda: zipfile), "ZIP_DEFLATED")) #inserting the required files inside the zip file
          _l_(580444) #inserting the required files inside the zip file
        _c_(580448, _a_(580447, _n_(580446, "zip_obj", lambda: zip_obj), "close"))
        _l_(580449)
        zip_obj_name = _a_(580451, _n_(580450, "zip_obj", lambda: zip_obj), "filename")
        _l_(580452)
        for i in _n_(580453, "file_lst", lambda: file_lst):
          _l_(580459)

          _c_(580457, _a_(580455, _n_(580454, "os", lambda: os), "remove"), _n_(580456, "i", lambda: i)) #removing the txt files
          _l_(580458) #removing the txt files
        del file_lst
        _l_(580460)
        aux = _c_(580463, _n_(580461, "send_file", lambda: send_file), _n_(580462, "zip_obj_name", lambda: zip_obj_name)),_c_(580466, _a_(580465, _n_(580464, "os", lambda: os), "remove"), '/home/ZCDS4327/proj/cs_proj_pro_1/zipfile.zip') #downloading the zipfile and deleting it from the working directory
        _l_(580467) #downloading the zipfile and deleting it from the working directory
        return aux #downloading the zipfile and deleting it from the working directory