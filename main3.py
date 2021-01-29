import json

user=input("enter your name=")
print("WELCOME IN....LOGIN/SIGNING PROJECT..",user)

isUserExist=""
user_input= input("what you want login/sign up=")

def write_json(data, filename='userdetails.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

if user_input=="login":
    username= input("enter username")
    password= input("enter password")
    with open('userdetails.json') as f:
        var=json.load(f)
        var2=var['user']
        print("var2",var2)
        for j in var2:
            if j['username']== username and j['password']==password:
                print("thanks for login")
                print("this is "+j["username"]+", and my date of birth is "+j["profile"]["dob"]+"and your gender is "+j["profile"]["gender"])
                break
            else:
                print("this is invalid password/username")
                break
elif user_input=="sign up":
    username= input("enter username")
    password1= input("enter password")
    password2 = input("confirm password ")
    if password1 != password2 :
        print("both passwords are not same")
    else:
        with open('userdetails.json') as json_file: 
            data = json.load(json_file) 
            temperory = data['user']
            for i in temperory:
                print(i)
                if i["username"] == username:
                    isUserExist="yes"
            if isUserExist== "yes":
                print(username,"username is already exists")
            elif isUserExist=="":
                print("ooh great u are sign up succesfully")
                description=input("enter your discription=")
                data_of_birth=input("enter your date of birth=")
                hobbies=input("enter your hobbies=")
                gender_of_user=input("enter gender")
                dic={"username":username,"password":password1,"profile":{"description":description,"dob":data_of_birth,"hobbies":hobbies,"gender":gender_of_user}}
                temperory.append(dic)
                print("username:",username)
                print("gender:",gender_of_user)
                print("bio:i am  jyoti")
                print("hobbies:",hobbies)
                print("dob:",data_of_birth)
            
                # print("this is "+username+", and my date of birth is "+data_of_birth+"and your gender is "+gender_of_user)
                write_json(data)

    
    

            
            
    












        