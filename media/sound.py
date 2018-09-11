
import wave
import pymysql

# i am only storing the name of file in database with id
# infile is the path from where you are giving the sample file like downloads documents
# path is your storage folder on server machine where you keep your files

#Working-
#Enter the path of file to be checked
#It will look in database for the file name. if name already exists then it will append the new file at the end of previously stored file.
#If new file comes it will save the name to database and create new file at our storage location of those files that is path

#Database has two fields id int pk with auto increment and second is path(the database col name) to store names

def check_sound(incoming):
    match=False
    data=[]
    # storage on server
    path = '/home/raghav/Sounds/'
    infile = incoming
    out= infile.split('/')
    outfile= out[-1]
    print(outfile)
    file_format=outfile.split('.')
    if file_format[-1]!='wav':
        print('Wrong Format')
        return

    db=pymysql.connect(user='root',password='@dmin',port=3306,host='localhost',database='sound')
    cursor=db.cursor()
    sql='select path from sound'
    cursor.execute(sql)
    res= cursor.fetchall()
    for i in res:
        #print(i[0])
        if outfile.lower()==i[0].lower():
            match=True
            print('Duplicate. Appending to previous file - ')
            w = wave.open(path+outfile, 'rb')
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            
            w = wave.open(infile, 'rb')
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            w.close()

            output = wave.open(path+outfile, 'wb')
            output.setparams(data[0][0])
            output.writeframes(data[0][1])
            output.writeframes(data[1][1])
            output.close()
            print('File Appended')
    if match==False:
        print('New File')
        
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()

        output = wave.open(path+outfile, 'wb')
        output.setparams(data[0][0])
        output.writeframes(data[0][1])
        output.close()
        print('New File Created')
        sql='insert into sound(path) values(%s)'
        args = (outfile,)
        cursor.execute(sql,args)
        db.commit()
        print('Saved in database')
         
    db.close()

#temp storage of file to be processed
incoming = input('Enter filepath to be loaded-')
check_sound(incoming)
