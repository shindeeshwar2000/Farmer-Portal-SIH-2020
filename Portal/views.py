import pyrebase
import twilio
import random
import firebase_admin
import firebase
from firebase_admin import credentials
from django.contrib import auth
from django.shortcuts import render ,redirect
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from firebase_admin import auth as admin
from firebase_admin import db
from .models import *
import threading
import time
from threading import Thread
from bs4 import BeautifulSoup
import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
requests.packages.urllib3.disable_warnings()

import random 



# config = {
#     'apiKey': "AIzaSyA7JMfUB2XdR3OnmuM5gN0Ma1L-6yS2RsA",
#     'authDomain': "cpanel-52867.firebaseapp.com",
#     'databaseURL': "https://cpanel-52867.firebaseio.com",
#     'projectId': "cpanel-52867",
#     'storageBucket': "cpanel-52867.appspot.com",
#     'messagingSenderId': "940927878646",
#     'appId': "1:940927878646:web:7bfb616abda15cab9373d7",
#     'measurementId': "G-R72FN0C1LJ"
# }

config = {
    'apiKey': "AIzaSyA7A4K8zW30Kqcn9o-ftpnvfTdKQzvMtag",
    'authDomain': "loginregister-5c8a7.firebaseapp.com",
    'databaseURL': "https://loginregister-5c8a7.firebaseio.com",
    'projectId': "loginregister-5c8a7",
    'storageBucket': "loginregister-5c8a7.appspot.com",
    'messagingSenderId': "786367269805",
    'appId': "1:786367269805:web:ca5179e64750332d012f24",
    'measurementId': "G-3Z941MD1D7"
}


co = 1
ip = IPv4Address("192.168.43.1") 
session = AirmoreSession(ip)
session = AirmoreSession(ip, 2333)  # assuming it is 2334
service = MessagingService(session)
was_accepted = session.request_authorization()

# # print(was_accepted)
# message = None
# message = service.fetch_message_history()[0]

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()

database = firebase.database()

cred = credentials.Certificate("/home/prathamesh/Downloads/loginregister-5c8a7-firebase-adminsdk-w7e9m-2335f41a50.json")

firebase_admin.initialize_app(cred)


# ref = database.reference('boxes')
# print(ref.get())











# data = {
#     'work':"progress",
#     'ok':"ok"
# }
# database.child("users").push(data)

# firebase = firebase.FirebaseApplication("https://cpanel-52867.firebaseio.com/" , None)

# print(firebase.get('/users',None))

# firebase.post('/users' , { Name:'123', phone:'456', loction:'890', produce:{ Name_f:'Apple',  Oty:'20',  Prize:'300', Delivery_option:'1' } })

# { Name:'123', phone:'456', loction:'', produce:{ Name:'Apple',  Oty:'20',  Prize:'300', Delivery_option:'1' } }

    
        
    
    
# data:{
    
#     'Name':'pratham',
#     'phone':'ok',
#     'email':'1@gmail.com'
# }

# result = firebase.post('/cpanel-52867/customer',data)
# print(result)










def signIn(request):

    return render(request, "signIn.html")


def postsign(request):
    
    email = request.POST.get('email')
    # user = authe.create_user(  uid='1234', email='user@example.com', phone_number='+15555550100' ,)
    # print('Sucessfully created new user: {0}'.format(user.uid))
    password = request.POST.get('password')
    # import firebase_admin
    # from firebase_admin import credentials

    # cred = credentials.Certificate("/home/prathamesh/Downloads/cpanel-52867-firebase-adminsdk-3g80u-7933dcb931.json")
    # firebase_admin.initialize_app(cred)
    
    # user = auth.create_user( 
        
    #     email='user@example.com',
    #     email_verified=False, 
    #     phone_number='+15555550100',
    #     password='secretPassword',
    #     display_name='John Doe',
    #     photo_url='http://www.example.com/12345678/photo.png',
    #     disabled=False
    # )
    # print('Sucessfully created new user: {0}'.format(user.uid))
    
    try:
        user = authe.sign_in_with_email_and_password(email, password)
    
    except:
        messsage = "invalid credentials"
        return render(request, "signIn.html", {'messsage': messsage})

    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html", {'e': email})


def logout(request):
    auth.logout(request)
    return render(request, "signIn.html")


def signup(request):

    return render(request, "signup.html")


def post_sign_up(request):
    name = request.POST.get('username')
    password = request.POST.get('password')

    user = authe.create_user_with_email_and_password(name, password)
    uid = user['localId']
    data = {"name": name, "status": "1"}

    database.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")


def create(request):

    return render(request, "create.html")


def post_create(request):
    work = request.POST.get('work')
    progress = request.POST.get('progress')
    
    
    data = {
        'Qty':"1Kg",
        'Price':"400",
        'Delivery-Option':'0'
    }

    sold = {
        'Qty':"3Kg",
        'Price':"200",
        'Delivery-Option':'1',
        'Buyer':'++919371546987'
    }

    Order_List = {
        'Produce-Name':'Bhel',
        'Qty':"50L",
        'Price':"10K",
        'Delivery-Option':'With Home Delivery',
        'Farmer':'+91888746311'
    }
    idtoken = request.session['uid']
    user_phone = request.session['user_phone']
    print(user_phone)
    # a = authe.get_account_info(idtoken)
    # a = a['users']
    # a = a[0]
    # a = a['localId']
    # database.child('users').child("Farmers").child(user_phone).child("Produce").child("Onion").set(data)
    database.child('users').child("Buyers").child(user_phone).child("Order-List").child("Order-No-2").set(Order_List)
    # database.child('users').child("Buyers").child(user_phone).child("Order-List").child("Order-No-2").set(Order_List)
   

    # database.child('users').child("Buyers").child(user_phone).set(profile)

    return render(request, 'welcome.html')

# sold = {
#         'Qty':"3Kg",
#         'Price':"200",
#         'Delivery-Option':'1',
#     }

# database.child('users').child("Farmers").child("+919595666570").child("Produce-sold")
# database.child('users').child("Buyers").child(user_phone).child("Order-List").child("Order-No-2").set(Order_List)
# profile = {
#     'Name':"Prathamesh",
#     'Address':"Nasik",
# }



def add_to_cart(request , add_to_cart=None ):
    print("*88888888888888888888888888888888")
    print(add_to_cart)
    print("*888888855555555558888888888888888888888888")
    
    print(request.POST.get('bnt'))
    print("*888881111111111111888888888888888888888888888")

    phn = request.POST.get('bnt')
    test = request.POST.get('bnt')
    print(request.POST[test])
    price = database.child('users').child("Farmers").child(phn).child("Produce").child(add_to_cart).child("Price").shallow().get().val()  ## Value to be updated
    Qty = database.child('users').child("Farmers").child(phn).child("Produce").child(add_to_cart).child("Qty").shallow().get().val()  ## Value to be updated
    DO = database.child('users').child("Farmers").child(phn).child("Produce").child(add_to_cart).child("Delivery-Option").get().val()  ## Value to be updated
    
    
    print(price , Qty , DO )
    print("*8888899999999888888888888888888888888888")
    # database.ch89ild('users').child("Farmers").child(phn).child("Produce").child(add_to_cart).child("Qty").set(str(int(Qty)-int(test)))
    
    cart={
        'Price':price,
        'Qty' : Qty,
        'Delivery-Options':DO,
        'Farmer':test,
    }
    cart_farmer={
        'Price':price,
        'Qty' : Qty,
        'Delivery-Options':DO,
        'Buyer':test,
    }
    print(request.session['user_phone'])    
    data = database.child('users').child("Buyers").child(request.session['user_phone']).child("Cart").child(add_to_cart).set(cart)
    data = database.child('users').child("Farmers").child(test).child("Produce-Request").child(add_to_cart).set(cart_farmer)
    
    cart = database.child('users').child("Buyers").child(request.session['user_phone']).child("Cart").get().val()
    print(cart)
    li = []
    for i in cart:
        li.append(i)
    
    
    
    # items = list(cart.items())
    # print(items)
    # data_sold = database.child('users').child("Buyers").child(test).set(profile)
   
    return render(request , "index.html" , {'cart' : li})

def checkout(request):
    print(request.session['user_phone']) 
    data = database.child('users').child("Buyers").child(request.session['user_phone']).child("Cart").get().val()
    print(data)
    li =  []
    for key, value in data.items():
        temp = [ key ,value['Farmer'] ,value['Price'] , value['Qty'] , database.child('users').child("Farmers").child(value['Farmer']).child("Name").get().val() ]
        li.append(temp)
        temp=[]
        # print(key, value['Farmer'] , database.child('users').child("Buyers").child(value['Farmer']).child("Name").get().val())
    print(li)
    return render(request ,"cart.html" , {'cart' : li} )

# data = database.child('users').child("Buyers").child("+919922716485").child("Cart").get().val()
# print(data)

def display(request):

    Fruits = [ "Apple" , "Tomato" ,"Onion"]        
    li=[]
    args = {}
    all_users = database.child("users").child("Farmers").get()
    for user in all_users.each():
        for key, value in (user.val()['Produce']).items():
            if key in Fruits:
                list_inside= [user.key(),user.val()['Name'] ,key , (user.val()['Address']) , value['Price'] ,value['Qty'] ]
                li.append(list_inside)
                list_inside=[]
    args['list_of_farmers'] = li
    
    return render(request, 'product-list.html',args)


def background():
    
    # session 
    # was_accepted = session.request_authorization()
    print(was_accepted)
    print("IN")
    message = None
    message = service.fetch_message_history()
    # print(message.content, message.phone)
    #tomato 2kg 200
    last_id = 0
    while True:
        message = service.fetch_message_history()

        # user = admin.get_user_by_phone_number(message[0].phone)
        print(message[0].was_read)
        print("============")
        print(last_id)
        print("====--------========")
        print(message[0].id)
        print("====--------========")
        # message = messages[0]
        # m = messages[0]
        # print(messages[0].id)
        # chat = service.fetch_chat_history(m)
        # print(chat[0].id)

        if not message[0].was_read == True and last_id != message[0].id:
            last_id = message[0].id
            print(message[0].content, message[0].phone)
            l = message[0].content.split()
            
            
            if len(l) == 1:
               
                if int(l[0]) == 2:
                    m = message[0]
                    # print(m[0].id)
                    chat=service.fetch_chat_history(m)
                    print(chat[1].id)
                    s = chat[2].content.split()
                    data = {
                        'Qty':s[1],
                        'Price':s[2],
                        'Delivery-Option':s[3]
                    }
                    
                    pande={
                        'Product_Name':s[0],
                        'Quantity':s[1],
                        'Price':s[2],
                        'Mobile':message[0].phone
                    }
                 
                    service.send_message(message[0].phone, ''' Thanks for using Our Farmer Portal !\nYour product is live for sale on our Portal now ''')
                    database.child('users').child("Farmers").child(message[0].phone).child("Produce").child(s[0]).set(data)
                    database.child('products').child(random.randint(9, 9999)).set(pande)
                
                if int(l[0]) == 1:
                    m = message[0]
                # print(m[0].id)
                chat=service.fetch_chat_history(m)
                print(chat[1].id)
                
                s = chat[2].content.split()
                ss1 = chat[1].content.split()
                print(ss1)
                data = {
                    'Qty':s[1],
                    'Price':ss1[11],
                    'Delivery-Option':s[3]
                }
                
                pande={
                    'Product_Name':s[0],
                    'Quantity':s[1],
                    'Price':ss1[11],
                    'Mobile':message[0].phone
                }
                service.send_message(message[0].phone, ''' Thanks for using Our Farmer Portal !\nYour product is live for sale on our Portal now ''')
                database.child('users').child("Farmers").child(message[0].phone).child("Produce").child(s[0]).set(data)
                database.child('products').child(random.randint(9, 9999)).set(pande)

            # elif len(l) != 5:
                # service.send_message(message[0].phone, message[0].content + '''Sorry : You have entered wrong information  Plesase Enter in  
                    # <Produce-Name>  <Quantity>  <Qualitiy>  <Expected-Price>  <Delivery-option>''' )
       
            else:
               
                words = []
                path="/home/prathamesh/SIH/cpanel/cpanel/prod-list.csv"
                with open(path) as csvDataFile:
                    csvReader = csv.reader(csvDataFile)
                    for row in csvReader:
                        for word in row:
                            words.append(word)

                # print all words from file
                for word in words:
                    print(word)
                print()

                test = message[0].content
                query0 = test.split()
                query = query0[0]

                print("Query : ", query)
                string1, accuracy = process.extractOne(query, words)
                if accuracy >= 50:
                    l[0] = words
                    s1 , s2 = process.extractOne(query, words)
                    print("Best fit : ", process.extractOne(query, words))
                    
                else:
                    print("Word NOT Found..!")
               
                # service.send_message(message[0].phone, '''Thanks for using SIH  ''' + message[0].content  + '''  Your Produce is now Live on SIH.com''')  
                session = requests.Session()
                session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
                print("ok-1")

                url = 'http://agmarknet.gov.in/'
                content = session.get(url, verify=False).content
                soup = BeautifulSoup(content, "html.parser")
                print("ok-2")

                vals = soup.find_all('div', {'class': 'commodity'})
                print(len(vals))

                district = ""
                state = ""
                commodity = 0
                market = 0
                flag = 0
                print("ok-13")
                
                for i in vals:
                    option = i.find_all('option')

                    for j in option:
                        if j.text == l[0]: #####
                            commodity = j.get("value")

                url1 = 'http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=' + str(commodity) + '&Tx_State=MH&Tx_District=14&Tx_Market=0&DateFrom=02-Jan-2020&DateTo=10-Jan-2020&Fr_Date=02-Jan-2020&To_Date=10-Jan-2020&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Maharashtra&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--'
                content1 = session.get(url1, verify=False).content
                soup = BeautifulSoup(content1, "html.parser")

                vals = soup.find_all('div', {'id': 'cphBody_paneltabular'})
                price = 0
                nos = 0
                quality = "A" ####

                print("ok-15")
                if quality == "A":
                    for m in vals:
                        for i in range(0, 50):

                            id_1 = 'cphBody_GridPriceData_Labmaxpric_' + str(i)
                            f_p = m.find_all('span', {'id': id_1})
                            for k in f_p:
                                price += int(k.text)
                                nos += 1

                elif quality == "B":
                    for m in vals:
                        for i in range(0, 50):

                            id_1 = 'cphBody_GridPriceData_LabModalpric_' + str(i)
                            f_p = m.find_all('span', {'id': id_1})
                            for k in f_p:
                                print(k.text)
                                price += int(k.text)
                                nos += 1
                elif quality == "C":
                    for m in vals:
                        for i in range(0, 50):

                            id_1 = 'cphBody_GridPriceData_LabMinPrice_' + str(i)
                            f_p = m.find_all('span', {'id': id_1})
                            for k in f_p:
                                print(k.text)
                                price += int(k.text)
                                nos += 1
                print("ok-17")

                print('suggested price:- ' + str(price/nos)) ####

                # if int(price/nos) < int(l[2]):
                Address_buyer = database.child('users').child("Farmers").child(message[0].phone).child("Address").get().val()
                service.send_message(message[0].phone , '''Current Suggested Price for your product '''+ s1 +''' from ''' + Address_buyer + ''' \nMarket is ''' + str(price/nos) +'''.\n\nDo you want to continue with suggested Price?\nPress 1 - continue with suggested price \nPress 2 - continue with your price \nPress 3 - Cancel ''')
                    # service.send_message(message[0].phone, "Suggested price" + str(price/nos))
                    
                # database.child('users').child("Farmers").child(message[0].phone).child("Produce").child(l[0]).set(data)
                print("ok---")
            # except:
                print(message[0].phone)
                print("Not Ok")
                # service.send_message(message[0].phone, "your order has been successfully placed")
               


def post_form(request):
    
    if request.POST:
        pname = request.POST.get('prodname')
        qnty = request.POST.get('qnty')
        Price = request.POST.get('price')
        customer_group_id = request.POST.get('customer_group_id')
    
        print("55555555511111111111111")
        print(pname,qnty,Price,customer_group_id)
       
        data={
            'Delivery-Option':customer_group_id,
            'Price':Price,
            'Qty':qnty,
        }
        database.child('users').child("Farmers").child(request.session['user_phone']).child("Produce").child(pname).set(data)
        data = database.child('users').child("Farmers").child(request.session['user_phone']).child("Produce-Request").get().val()
        li =  []
        for key, value in data.items():
            temp = [ key ,value['Buyer'] ,database.child('users').child("Buyers").child(value['Buyer']).child("Name").get().val()   ]
            li.append(temp)
            temp=[]
            print(key, value['Buyer'] , database.child('users').child("Buyers").child(value['Buyer']).child("Name").get().val())
        print("555555555555555555")
        # print(temp)
        return render(request, "farmer_dashboard.html" ,{'name':database.child('users').child("Farmers").child(request.session['user_phone']).child("Name").get().val() ,  'Buyer_List' : li })



def upload_form(request):
    return render(request,"farmer_sell.html")


def check(request):

    return render(request, "check.html")


def home(request):
    
    was_accepted = session.request_authorization()
    print(was_accepted)
    
    t = Thread(target=background)
    t.start()

    return render(request, "index.html")
    
    
def Fruits(request):
    return render(request,"category.html")    



def category(request):
    
    return render(request,"category.html")


def Register(request):
    print("reg")
    return render(request,"register.html")


def Post_Register(request):
    if request.POST:
        name = request.POST.get("name")
        mobile = request.POST.get("telephone")
        address = request.POST.get("address_1")
        city = request.POST.get("city")
        password = request.POST.get("password")   
        check = request.POST.get("customer_group_id")   

    
        # li = [ name,mobAddress_buyer = database.child('users').child("Farmers").child("+919595666570").child("Address").get().val()


# print(Address_buyer).................................................................................................................................................................................................ile,address,city,password ,check ]
        
        # cred = credentials.Certificate("/home/prathamesh/Downloads/cpanel-52867-firebase-adminsdk-3g80u-7933dcb931.json")
        # firebase_admin.initialize_app(cred)

        user = admin.create_user( 
            
            email= str(random.randint(999, 9999))+'@example.com',
            phone_number=mobile,
            password=password,
            display_name=name,
            photo_url='http://www.example.com/12345678/photo.png',
            disabled=False
        )
                
        profile = {
            'Name':name,
            'Address':address,
            'city':city
        }   
        if check == 2:
            database.child('users').child("Farmers").child(mobile).set(profile)
        else:
            database.child('users').child("Buyers").child(mobile).set(profile)
        OTP = random.randint(999, 9999)
        service.send_message(mobile, "Your verification code is " + str(OTP))
        print(OTP)


    return render(request,"login-OTP.html" , {'phone':mobile , 'OTP' : OTP}) 
        
def post_otp(request , OTP=1):
    
    print(request.POST.get('otp'))
    print(OTP)    
    if not request.POST.get('otp') == OTP:
        messsage = "invalid credentials"
        return render(request, "register.html", {'messsage': messsage})
    
    return render(request, "login.html")

def login(request):
    
  return render(request,"login.html")

def link_myprod(request):
    return render(request , "farmer_myprod.html")


def login_by_phone(request):
    
    if request.POST:
        phone = request.POST.get('mob')
        password = request.POST.get('password')

        print("****************************************")
        user_phone = admin.get_user_by_phone_number(phone)
        
       
        name = (user_phone.display_name)
   
        try:
            user = authe.sign_in_with_email_and_password(user_phone.email, password)

        except:
            messsage = "invalid credentials"
            return render(request, "signIn.html", {'messsage': messsage})

        user_phone = authe.get_account_info(user['idToken'])
        print(user_phone)
        user_phone = user_phone['users'][0]['phoneNumber']
        # print(user_phone['users'][0]['displayName'])
            
        if user_phone == phone:            
            session_id = user['idToken']
            request.session['uid'] = str(session_id)
            request.session['user_phone'] = str(user_phone)
    # try :
        if user_phone == "+919922716485":
            return render(request, "index.html" ,{'name':name})
        else:
            # return render(request, "farmer_dashboard.html" ,{'name':name})
    # except:
            data = database.child('users').child("Farmers").child(user_phone).child("Produce-Request").get().val()
            li =  []
            for key, value in data.items():
                temp = [ key ,value['Buyer'] ,database.child('users').child("Buyers").child(value['Buyer']).child("Name").get().val()   ]
                li.append(temp)
                temp=[]
                print(key, value['Buyer'] , database.child('users').child("Buyers").child(value['Buyer']).child("Name").get().val())
            print("555555555555555555")
            # print(temp)
            return render(request, "farmer_dashboard.html" ,{'name':name ,  'Buyer_List' : li })
            


def buyer_details(request , buyer_number=1):

    print(request.session['user_phone'] )
    Name_buyer = database.child('users').child("Buyers").child(buyer_number).child("Name").get().val()
    Address_buyer = database.child('users').child("Buyers").child(buyer_number).child("Address").get().val()
    data_farmer = database.child('users').child("Farmers").child(request.session['user_phone']).child("Produce-Request").get().val()
    
    li = []
    print(data_farmer)
    # print(data)
  
    
    print(Name_buyer , Address_buyer)
    
    # print(li)
    li.append(Name_buyer)    
    li.append(Address_buyer)    
    for key, value in data_farmer.items():
        temp = []
        print(key,value)
        if value['Buyer'] == buyer_number:
            li.append(key)
            li.append(value['Price'])
            li.append(value['Qty'])
           

  
    li.append(buyer_number)
    print(li)
    
    # li.append(li[2]['Farmer'])
    # li.append(li[2]['Price'])
    # li.append(li[2]['Qty'])
    # li.append(li[2]['Produce-Name'])
    # li.append(li[2]['Delivery-Options'])
    
    

      
        
    # print(data.items()['Address'])

  
    return render(request , "farmer_req.html" , {'li' : li})


# Order_List = {
#     'Buyer':'+919096014847s',
#     'Price':'100',
#     'Qty':'10kg'
# }   

# database.child('users').child("Farmers").child("+919595666570").child("Produce-Request").child("Banana").set(Order_List)
# Order_List={
# 'Buyer':'+919922716485',
# 'Price':'20000',
# 'Qty':'10kg'
# }   
# database.child('users').child("Farmers").child("+919595666570").child("Produce-Request").child("Banana").set(Order_List)


# Order_List = {
#     'Delivery-Options':"0",
#     'Farmer':'+919595666570',
#     'Price':'20000',
#     'Produce-Name':'Banana',
#     'Qty':'50kg'
# }   
# database.child('users').child("Buyers").child("+919881247910").child("Order-List").set(Order_List)
# data = database.child('users').child("Buyers").child("+919881247910").get().val()
# # print(data)
# i = 1;
# li = []
# for key, value in data.items():
#     i = i + 1 
#     if i == 3:
#         li.append(value)                      
#     else:
#         li.append(value)
# li.append(li[2]['Farmer'])
# li.append(li[2]['Price'])
# li.append(li[2]['Qty'])
# li.append(li[2]['Produce-Name'])
# li.append(li[2]['Delivery-Options'])

# for i in li:
#     print(i)



# print(data)
# for key, value in data.items():
#     print(key, value['Buyer'])
# res = [[i.values() for i in data[x]] for x in data.keys()] 
# print(res)

# Address_buyer = database.child('users').child("Farmers").child("+919595666570").child("Address").get().val()


# print(Address_buyer)

# li =  []
# for key, value in data.items():
#     # print(new_phone)
#     # print(new_phone)
#     name =database.child('users').child("Buyers").child("+919371515211").child("Name").get().val()
#     print(name)
#     temp = [ key ,value['Buyer'] ,name   ]
#     print(temp)
#     li.append(temp)
#     temp = []
# print(li)

def login_by_OTP(request):
    if request.POST:
        phone = request.POST.get('mob')
        password = request.POST.get('password')
    
        if not password:
            print("ok")
            
    
    
def signin(request):
    
    return render(request,"signIn.html")





def product_list(request,Name):
    
    print(Name)
    Fruits = [ "Apple" , "Tomato"  ,"Mango" , "Banana" , "Greps"]        
    li=[]
    args = {}
    all_users = database.child("users").child("Farmers").get()
    print(all_users)
    for user in all_users.each():
        # print(user.val())
        for key, value in (user.val()['Produce']).items():
            print("///////////////////////")
            print(key)
            print("**************************************")
            print(key)
            print("==========================")
            if key in Name:
                list_inside= [user.key(),user.val()['Name'] ,key , (user.val()['Address']) , value['Price'] ,value['Qty']  ]
                li.append(list_inside)
                list_inside=[]
    args['list_of_farmers'] = li
    args['Frutis_Name'] = Name
    
    return render(request, 'product-list.html',args)


# profile = {
#     'Name':"Omkar",
#     'Address':'Karnataka'
# }   
# database.child('users').child("Farmers").child("+917774047389").set(profile)
# messages = service.fetch_message_history()
# message = messages[0]
# print(messages[0].id)
# chat = service.fetch_chat_history(message)
# print(chat[1].id)

def accpet_order(request,buyer_number=1):
    print(buyer_number)
    service.send_message(buyer_number, '''Your Order Accpted by farmer''')
    return render(request , "index.html")

def reject_order(request,buyer_number=1):
    print(buyer_number)
    service.send_message(buyer_number, '''Your Order Rejected by farmer''')
    return render(request , "index.html")

print("==========*************========")
# chat = service.fetch_chat_history(message)
  # a list of Message objects again

# chats = service.fetch_chat_history()
# print(messages[0].type) 