import ftplib
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous","ftplib-example-1")
ftp.cwd('/pub/')
data = []
ftp.dir(data.append)
ftp.quit()
for i in data:
    print("-",i)
