# Restaurant Management System

from tkinter import *
import random
import time
from tkinter import filedialog , messagebox
import requests

# Functions
def reset() :
    textReceipt.delete(1.0 , END)
    e_manchowsoup.set('0')
    e_manchurian.set('0')
    e_paneerchilli.set('0')
    e_paneerhandi.set('0')
    e_sahipaneer.set('0')
    e_roti.set('0')
    e_rice.set('0')
    e_daal.set('0')
    e_fries.set('0')

    e_buttermilk.set('0')
    e_lassi.set('0')
    e_roselassi.set('0')
    e_pops.set('0')
    e_mocktails.set('0')
    e_cocktails.set('0')
    e_coco.set('0')
    e_jaljeera.set('0')
    e_falooda.set('0')

    e_paan.set('0')
    e_brownies.set('0')
    e_muffins.set('0')
    e_gulabjamun.set('0')
    e_rasmalai.set('0')
    e_blackforest.set('0')
    e_icecream.set('0')
    e_candy.set('0')
    e_waffles.set('0')

    textmanchowsoup.config(state=DISABLED)
    textmanchurian.config(state=DISABLED)
    textpaneerchilli.config(state=DISABLED)
    textpaneerhandi.config(state=DISABLED)
    textsahipaneer.config(state=DISABLED)
    textroti.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfries.config(state=DISABLED)

    textbuttermilk.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textroselassi.config(state=DISABLED)
    textpops.config(state=DISABLED)
    textmocktails.config(state=DISABLED)
    textcocktails.config(state=DISABLED)
    textcoco.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textfalooda.config(state=DISABLED)

    textpaan.config(state=DISABLED)
    textbrownies.config(state=DISABLED)
    textmuffins.config(state=DISABLED)
    textgulabjamun.config(state=DISABLED)
    textrasmalai.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    texticecream.config(state=DISABLED)
    textcandy.config(state=DISABLED)
    textwaffles.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofdessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def send() :
    if textReceipt.get(1.0  , END) == "\n" :
        pass

    else :
        def sendmsg() :
            message = textarea.get(1.0 , END)
            number = numberfield.get()
            auth = "MoJcEXbtN4AxkaWHD1YVyl7eTnI3RvuhOPSqjUZwLiC0rG98Qmj5wKs7zHMOgixZSBucn09rmehFNJRE"
            url = "https://www.fast2sms.com/dev/bulk"

            para = {'authorization' : auth , 
                    'message' : message ,
                    'numbers' : number ,
                    'sender-id' : 'FSTSMS' ,
                    'route' : 'p' ,
                    'language' : 'English'}
            response = requests.get(url,params=para)
            dic = response.json()
            result = dic.get('return')

            if result == True :
                messagebox.showinfo("Sent Successfully" , "Message Sent Successfully !")

            else :
                messagebox.showerror("Error" , "Something went wrong !")

        root2 = Toplevel()
        root2.title('Send Bill')
        root2.config(bg="Light green")
        root2.geometry('485x620+50+50')

        logoImage = PhotoImage(file='sender.png')
        label = Label(root2 , image = logoImage , bg="Light green")
        label.pack()

        numberLabel = Label(root2 , text="Mobile Number" , font=('Times New Roman' , 18 , 'underline' , 'bold') , bg = "light green" , fg = "black")
        numberLabel.pack(pady=5)

        numberfield = Entry(root2, font=('Helvetica' , 22 , 'bold'), bd =3 , width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2 , text="Bill Details" , font=('Times New Roman' , 18 , 'underline' , 'bold') , bg = "light green" , fg = "black")
        billLabel.pack(pady=5)

        textarea = Text(root2 , font=("Times New Roman" , 12 , "bold") , bd=3 , width=42 , height=14)
        textarea.pack(pady=5)
        textarea.insert(END , 'Receipt Ref:\t\t' + billnumber + "\t\t" + date + "\n\n")
        if costoffoodvar.get()!= '0 Rs' :
            textarea.insert(END , f'Cost of Food\t\t\t {priceofFood} Rs\n')

        if costofdrinksvar.get()!= '0 Rs' :
            textarea.insert(END , f'Cost of Drinks\t\t\t {priceofDrinks} Rs\n')

        if costofdessertvar.get()!= '0 Rs' :
            textarea.insert(END , f'Cost of Desserts\t\t\t {priceofDesserts} Rs\n')

        textarea.insert(END , f'Sub Total\t\t\t {subtotalofitems} Rs\n')
        textarea.insert(END , f'Service Tax\t\t\t {100} Rs\n')
        textarea.insert(END , f'Total Cost\t\t\t {subtotalofitems + 100} Rs\n')


        sendButton = Button(root2 , text="Send" , font=("Times New Roman", 19, "bold") , bg = "white" , fg = "black" , bd = 7 , relief=GROOVE , command = sendmsg)
        sendButton.pack(pady = 5)

        root2.mainloop()

def save():
    if textReceipt.get(1.0 , END) == "\n" :
        pass

    else :
        url = filedialog.asksaveasfile(mode='w' , defaultextension='.txt')
        if url == None :
            pass

        else :
            bill_data = textReceipt.get(1.0 , END)
            url.write(bill_data)
            url.close()

            messagebox.showinfo('Information' , 'Your Bill is Successfully Saved !!')

def receipt():
    global billnumber , date

    if costoffoodvar.get()!='' or costofdrinksvar.get()!='' or costofdessertvar.get()!='' :
        textReceipt.delete(1.0 , END)
        x = random.randint(100 , 10000)
        billnumber = "BILL" + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END , 'Receipt REF :\t\t ' + billnumber + '\t\t' + date + "\n")
        textReceipt.insert(END , '********************************************\n')
        textReceipt.insert(END , "Items:\t\t Cost Of Items(Rs)\n")
        textReceipt.insert(END , '********************************************\n')
        if (e_manchowsoup.get() != '0') :
            textReceipt.insert(END , f'Manchow Soup\t\t\t{int(e_manchowsoup.get())*90}\n\n')

        if (e_manchurian.get() != '0') :
            textReceipt.insert(END , f'Manchurian\t\t\t{int(e_manchurian.get())*100}\n\n')

        if (e_paneerchilli.get() != '0') :
            textReceipt.insert(END , f'Paneer Chilli\t\t\t{int(e_paneerchilli.get())*120}\n\n')    

        if (e_paneerhandi.get() != '0') :
            textReceipt.insert(END , f'Paneer Handi\t\t\t{int(e_paneerhandi.get())*130}\n\n')

        if (e_sahipaneer.get() != '0') :
            textReceipt.insert(END , f'Sahi Paneer\t\t\t{int(e_sahipaneer.get())*125}\n\n')

        if (e_roti.get() != '0') :
            textReceipt.insert(END , f'Roti\t\t\t{int(e_roti.get())*17}\n\n')

        if (e_rice.get() != '0') :
            textReceipt.insert(END , f'Rice\t\t\t{int(e_rice.get())*95}\n\n')

        if (e_daal.get() != '0') :
            textReceipt.insert(END , f'Daal\t\t\t{int(e_daal.get())*100}\n\n')

        if (e_fries.get() != '0') :
            textReceipt.insert(END , f'Fries\t\t\t{int(e_fries.get())*85}\n\n')

        if (e_buttermilk.get() != '0') :
            textReceipt.insert(END , f'Butter Milk\t\t\t{int(e_buttermilk.get())*35}\n\n')

        if (e_lassi.get() != '0') :
            textReceipt.insert(END , f'Lassi\t\t\t{int(e_lassi.get())*50}\n\n')

        if (e_roselassi.get() != '0') :
            textReceipt.insert(END , f'Rose Lassi\t\t\t{int(e_roselassi.get())*40}\n\n')

        if (e_pops.get() != '0') :
            textReceipt.insert(END , f'Pops\t\t\t{int(e_pops.get())*20}\n\n')

        if (e_mocktails.get() != '0') :
            textReceipt.insert(END , f'Mock-Tails\t\t\t{int(e_mocktails.get())*125}\n\n')

        if (e_cocktails.get() != '0') :
            textReceipt.insert(END , f'Cock-Tails\t\t\t{int(e_cocktails.get())*199}\n\n')

        if (e_coco.get() != '0') :
            textReceipt.insert(END , f'Coco\t\t\t{int(e_coco.get())*30}\n\n')

        if (e_jaljeera.get() != '0') :
            textReceipt.insert(END , f'Jal-Jeera\t\t\t{int(e_jaljeera.get())*15}\n\n')

        if (e_falooda.get() != '0') :
            textReceipt.insert(END , f'Falooda\t\t\t{int(e_falooda.get())*50}\n\n')

        if (e_paan.get() != '0') :
            textReceipt.insert(END , f'Paan\t\t\t{int(e_paan.get())*25}\n\n')

        if (e_brownies.get() != '0') :
            textReceipt.insert(END , f'Brownies\t\t\t{int(e_brownies.get())*99}\n\n')

        if (e_muffins.get() != '0') :
            textReceipt.insert(END , f'Muffins\t\t\t{int(e_muffins.get())*10}\n\n')

        if (e_gulabjamun.get() != '0') :
            textReceipt.insert(END , f'Gulab-Jamun\t\t\t{int(e_gulabjamun.get())*35}\n\n')

        if (e_rasmalai.get() != '0') :
            textReceipt.insert(END , f'Rasmalai\t\t\t{int(e_rasmalai.get())*45}\n\n')

        if (e_blackforest.get() != '0') :
            textReceipt.insert(END , f'Black-Forest\t\t\t{int(e_blackforest.get())*35}\n\n')

        if (e_icecream.get() != '0') :
            textReceipt.insert(END , f'Ice-Cream\t\t\t{int(e_icecream.get())*20}\n\n')

        if (e_candy.get() != '0') :
            textReceipt.insert(END , f'Candy\t\t\t{int(e_candy.get())*20}\n\n')

        if (e_waffles.get() != '0') :
            textReceipt.insert(END , f'Waffles\t\t\t{int(e_waffles.get())*149}\n\n')

        textReceipt.insert(END , '********************************************\n')

        if costoffoodvar.get()!= '0 Rs' :
            textReceipt.insert(END , f'Cost of Food\t\t\t {priceofFood} Rs\n\n')

        if costofdrinksvar.get()!= '0 Rs' :
            textReceipt.insert(END , f'Cost of Drinks\t\t\t {priceofDrinks} Rs\n\n')

        if costofdessertvar.get()!= '0 Rs' :
            textReceipt.insert(END , f'Cost of Desserts\t\t\t {priceofDesserts} Rs\n\n')

        textReceipt.insert(END , f'Sub Total\t\t\t {subtotalofitems} Rs\n\n')
        textReceipt.insert(END , f'Service Tax\t\t\t {100} Rs\n\n')
        textReceipt.insert(END , f'Total Cost\t\t\t {subtotalofitems + 100} Rs\n\n')
        textReceipt.insert(END , '********************************************\n')

    else :
        messagebox.showerror("Error" , "No item is selected")

def totalcost() :
    global priceofFood , priceofDrinks , priceofDesserts , subtotalofitems

    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or var26.get()!=0 or var27.get()!=0 :

        item1 = int(e_manchowsoup.get())
        item2 = int(e_manchurian.get())
        item3 = int(e_paneerchilli.get())
        item4 = int(e_paneerhandi.get())
        item5 = int(e_sahipaneer.get())
        item6 = int(e_roti.get())
        item7 = int(e_rice.get())
        item8 = int(e_daal.get())
        item9 = int(e_fries.get())

        item10 = int(e_buttermilk.get())
        item11 = int(e_lassi.get())
        item12 = int(e_roselassi.get())
        item13 = int(e_pops.get())
        item14 = int(e_mocktails.get())
        item15 = int(e_cocktails.get())
        item16 = int(e_coco.get())
        item17 = int(e_jaljeera.get())
        item18 = int(e_falooda.get())

        item19 = int(e_paan.get())
        item20 = int(e_brownies.get())
        item21 = int(e_muffins.get())
        item22 = int(e_gulabjamun.get())
        item23 = int(e_rasmalai.get())
        item24 = int(e_blackforest.get())
        item25 = int(e_icecream.get())
        item26 = int(e_candy.get())
        item27 = int(e_waffles.get())

        priceofFood = (item1*90) + (item2*100) + (item3*120) + (item4*130) + (item5*125) + (item6*17) + (item7*95) + (item8*100) + (item9*85)
        priceofDrinks = (item10*35) + (item11*50) + (item12*40) + (item13*20) + (item14*125) + (item15*199) + (item16*30) + (item17*15) + (item18*50)
        priceofDesserts = (item19*25) + (item20*99) + (item21*10) + (item22*35) + (item23*45) + (item24*35) + (item25*20) + (item26*20) + (item27*149)

        costoffoodvar.set(str(priceofFood) + ' Rs')
        costofdrinksvar.set(str(priceofDrinks) + ' Rs')
        costofdessertvar.set(str(priceofDesserts) + ' Rs')

        subtotalofitems = priceofFood + priceofDrinks + priceofDesserts
        subtotalvar.set(str(subtotalofitems) + ' Rs')

        servicetaxvar.set('100 Rs')

        totalcost = subtotalofitems + 100
        totalcostvar.set(str(totalcost) + ' Rs')

    else :
        messagebox.showerror("Error" , "No item is selected")

def manchowsoup() :
    if var1.get() == 1 :
        textmanchowsoup.config(state=NORMAL)
        textmanchowsoup.delete(0 , END)
        textmanchowsoup.focus()

    elif var1.get() == 0 :
        textmanchowsoup.config(state=DISABLED)
        e_manchowsoup.set('0')

def manchurian() :
    if var2.get() == 1 :
        textmanchurian.config(state=NORMAL)
        textmanchurian.delete(0 , END)
        textmanchurian.focus()

    elif var2.get() == 0:
        textmanchurian.config(state=DISABLED)
        e_manchurian.set('0')

def paneerchilli() :
    if var3.get() == 1 :
        textpaneerchilli.config(state=NORMAL)
        textpaneerchilli.delete(0 , END)
        textpaneerchilli.focus()

    elif var3.get() == 0 :
        textpaneerchilli.config(state=DISABLED)
        e_paneerchilli.set('0')

def paneerhandi() :
    if var4.get() == 1 :
        textpaneerhandi.config(state=NORMAL)
        textpaneerhandi.delete(0 , END)
        textpaneerhandi.focus()

    elif var4.get() == 0 :
        textpaneerhandi.config(state=DISABLED)
        e_paneerhandi.set('0')

def sahipaneer() :
    if var5.get() == 1 :
        textsahipaneer.config(state=NORMAL)
        textsahipaneer.delete(0 , END)
        textsahipaneer.focus()

    elif var5.get() == 0 :
        textsahipaneer.config(state=DISABLED)
        e_sahipaneer.set('0')

def roti() :
    if var6.get() == 1 :
        textroti.config(state=NORMAL)
        textroti.delete(0 , END)
        textroti.focus()

    elif var6.get() == 0 :
        textroti.config(state=DISABLED)
        e_roti.set('0')

def rice() :
    if var7.get() == 1 :
        textrice.config(state=NORMAL)
        textrice.delete(0 , END)
        textrice.focus()

    elif var7.get() == 0 :
        textrice.config(state=DISABLED)
        e_rice.set('0')

def daal() :
    if var8.get() == 1 :
        textdaal.config(state=NORMAL)
        textdaal.delete(0 , END)
        textdaal.focus()

    elif var8.get() == 0 :
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def fries() :
    if var9.get() == 1 :
        textfries.config(state=NORMAL)
        textfries.delete(0 , END)
        textfries.focus()

    elif var9.get() == 0 :
        textfries.config(state=DISABLED)
        e_fries.set('0')

def buttermilk() :
    if var10.get() == 1 :
        textbuttermilk.config(state=NORMAL)
        textbuttermilk.delete(0 , END)
        textbuttermilk.focus()

    elif var10.get() == 0 :
        textbuttermilk.config(state=DISABLED)
        e_buttermilk.set('0')

def lassi() :
    if var11.get() == 1 :
        textlassi.config(state=NORMAL)
        textlassi.delete(0 , END)
        textlassi.focus()

    elif var11.get() == 0 :
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def roselassi() :
    if var12.get() == 1 :
        textroselassi.config(state=NORMAL)
        textroselassi.delete(0 , END)
        textroselassi.focus()

    elif var12.get() == 0 :
        textroselassi.config(state=DISABLED)
        e_roselassi.set('0')

def pops() :
    if var13.get() == 1 :
        textpops.config(state=NORMAL)
        textpops.delete(0 , END)
        textpops.focus()

    elif var13.get() == 0 :
        textpops.config(state=DISABLED)
        e_pops.set('0')

def mocktails() :
    if var14.get() == 1 :
        textmocktails.config(state=NORMAL)
        textmocktails.delete(0 , END)
        textmocktails.focus()

    elif var14.get() == 0 :
        textmocktails.config(state=DISABLED)
        e_mocktails.set('0')

def cocktails() :
    if var15.get() == 1 :
        textcocktails.config(state=NORMAL)
        textcocktails.delete(0 , END)
        textcocktails.focus()

    elif var15.get() == 0 :
        textcocktails.config(state=DISABLED)
        e_cocktails.set('0')

def coco() :
    if var16.get() == 1 :
        textcoco.config(state=NORMAL)
        textcoco.delete(0 , END)
        textcoco.focus()

    elif var16.get() == 0 :
        textcoco.config(state=DISABLED)
        e_coco.set('0')

def jaljeera() :
    if var17.get() == 1 :
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0 , END)
        textjaljeera.focus()

    elif var17.get() == 0 :
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')

def falooda() :
    if var18.get() == 1 :
        textfalooda.config(state=NORMAL)
        textfalooda.delete(0 , END)
        textfalooda.focus()

    elif var18.get() == 0 :
        textfalooda.config(state=DISABLED)
        e_falooda.set('0')

def paan() :
    if var19.get() == 1 :
        textpaan.config(state=NORMAL)
        textpaan.delete(0 , END)
        textpaan.focus()

    elif var19.get() == 0 :
        textpaan.config(state=DISABLED)
        e_paan.set('0')

def brownies() :
    if var20.get() == 1 :
        textbrownies.config(state=NORMAL)
        textbrownies.delete(0 , END)
        textbrownies.focus()

    elif var20.get() == 0 :
        textbrownies.config(state=DISABLED)
        e_brownies.set('0')

def muffins() :
    if var21.get() == 1 :
        textmuffins.config(state=NORMAL)
        textmuffins.delete(0 , END)
        textmuffins.focus()

    elif var21.get() == 0 :
        textmuffins.config(state=DISABLED)
        e_muffins.set('0')

def gulabjamun() :
    if var22.get() == 1 :
        textgulabjamun.config(state=NORMAL)
        textgulabjamun.delete(0 , END)
        textgulabjamun.focus()

    elif var22.get() == 0 :
        textgulabjamun.config(state=DISABLED)
        e_gulabjamun.set('0')

def rasmalai() :
    if var23.get() == 1 :
        textrasmalai.config(state=NORMAL)
        textrasmalai.delete(0 , END)
        textrasmalai.focus()

    elif var23.get() == 0 :
        textrasmalai.config(state=DISABLED)
        e_rasmalai.set('0')

def blackforest() :
    if var24.get() == 1 :
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0 , END)
        textblackforest.focus()

    elif var24.get() == 0 :
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

def icecream() :
    if var25.get() == 1 :
        texticecream.config(state=NORMAL)
        texticecream.delete(0 , END)
        texticecream.focus()

    elif var25.get() == 0 :
        texticecream.config(state=DISABLED)
        e_icecream.set('0')

def candy() :
    if var26.get() == 1 :
        textcandy.config(state=NORMAL)
        textcandy.delete(0 , END)
        textcandy.focus()

    elif var26.get() == 0 :
        textcandy.config(state=DISABLED)
        e_candy.set('0')

def waffles() :
    if var27.get() == 1 :
        textwaffles.config(state=NORMAL)
        textwaffles.delete(0 , END)
        textwaffles.focus()

    elif var27.get() == 0 :
        textwaffles.config(state=DISABLED)
        e_waffles.set('0')

root = Tk()

root.geometry("1270x690+0+0")
root.resizable(0,0)
root.title("Restaurant Management System")
root.config(bg="cyan")

topFrame = Frame(root , bd = 15 , relief=RIDGE , bg="blue")
topFrame.pack(side=TOP)

labelTitle = Label(topFrame , text = "Restaurant Management System" , font=('Times New Roman' , 35 , 'bold') , fg="DarkBlue" , bg="lightgreen" , width=44)
labelTitle.grid(row=0 , column=0)

#frames

menuFrame = Frame(root , bd = 10 , relief=RIDGE , bg = "blue")
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame , bd = 8 , relief=RIDGE , bg = "lightgreen" , pady = 10 , padx=17)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame , text = "Food" , font = ('Times New Roman' , 19 , 'bold'), fg="Black" , bg="lightgreen", bd = 10 , relief=RIDGE)
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame , text = "Drinks" , font = ('Times New Roman' , 19 , 'bold') ,fg="Black" , bg="lightgreen" , bd = 10 , relief=RIDGE)
drinksFrame.pack(side=LEFT)

dessertFrame = LabelFrame(menuFrame , text = "Desserts" , font = ('Times New Roman' , 19 , 'bold') ,fg="Black" , bg="lightgreen", bd = 10 , relief=RIDGE)
dessertFrame.pack(side=LEFT)

rightFrame = Frame(root , bd = 15 , relief=RIDGE ,  bg="blue")
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame , bd=1 , relief=RIDGE , bg="blue")
calculatorFrame.pack()

recieptFrame = Frame(rightFrame , bd=4 , relief=RIDGE , bg="blue")
recieptFrame.pack()

buttonFrame = Frame(rightFrame , bd=3 , relief=RIDGE  , bg="blue")
buttonFrame.pack()

#Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_manchowsoup = StringVar()
e_manchurian = StringVar()
e_paneerchilli = StringVar()
e_paneerhandi = StringVar()
e_sahipaneer = StringVar()
e_roti = StringVar()
e_rice = StringVar()
e_daal = StringVar()
e_fries = StringVar()

e_manchowsoup.set('0')
e_manchurian.set('0')
e_paneerchilli.set('0')
e_paneerhandi.set('0')
e_sahipaneer.set('0')
e_roti.set('0')
e_rice.set('0')
e_daal.set('0')
e_fries.set('0')

e_buttermilk = StringVar()
e_lassi = StringVar()
e_roselassi = StringVar()
e_pops = StringVar()
e_mocktails = StringVar()
e_cocktails = StringVar()
e_coco = StringVar()
e_jaljeera = StringVar()
e_falooda = StringVar()

e_buttermilk.set('0')
e_lassi.set('0')
e_roselassi.set('0')
e_pops.set('0')
e_mocktails.set('0')
e_cocktails.set('0')
e_coco.set('0')
e_jaljeera.set('0')
e_falooda.set('0')

e_paan = StringVar()
e_brownies = StringVar()
e_muffins = StringVar()
e_gulabjamun = StringVar()
e_rasmalai = StringVar()
e_blackforest = StringVar()
e_icecream = StringVar()
e_candy = StringVar()
e_waffles = StringVar()

e_paan.set('0')
e_brownies.set('0')
e_muffins.set('0')
e_gulabjamun.set('0')
e_rasmalai.set('0')
e_blackforest.set('0')
e_icecream.set('0')
e_candy.set('0')
e_waffles.set('0')

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofdessertvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

# Food
manchowsoup = Checkbutton(foodFrame , text = 'Manchow Soup' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var1 , command=manchowsoup)
manchowsoup.grid(row=0 , column=0 , sticky=W)

manchurian = Checkbutton(foodFrame , text = 'Manchurian' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var2 , command=manchurian)
manchurian.grid(row=1 , column=0 , sticky=W)

paneerchilli = Checkbutton(foodFrame , text = 'Paneer Chilli' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var3 , command=paneerchilli)
paneerchilli.grid(row=2 , column=0 , sticky=W)

paneerhandi = Checkbutton(foodFrame , text = 'Paneer Handi' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var4 , command=paneerhandi)
paneerhandi.grid(row=3 , column=0 , sticky=W)

sahipaneer = Checkbutton(foodFrame , text = 'Sahi Paneer' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var5 , command=sahipaneer)
sahipaneer.grid(row=4 , column=0 , sticky=W)

roti = Checkbutton(foodFrame , text = 'Roti' , font=('Times New Roman' , 18 , 'bold'),fg="Black" , bg="lightgreen" , onvalue=1 , offvalue=0 , variable=var6 , command=roti)
roti.grid(row=5 , column=0 ,sticky=W)

rice = Checkbutton(foodFrame , text = 'Rice' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var7 , command = rice)
rice.grid(row=6 , column=0 , sticky=W)

daal = Checkbutton(foodFrame , text = 'Daal' , font=('Times New Roman' , 18 , 'bold') , fg="Black" ,bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var8 , command=daal)
daal.grid(row=7 , column=0 , sticky=W)

fries = Checkbutton(foodFrame , text = 'Fries' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var9 , command=fries)
fries.grid(row=8 , column=0 , sticky=W)

# Entry fields for Food Items

textmanchowsoup = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_manchowsoup)
textmanchowsoup.grid(row=0 , column=1)

textmanchurian = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_manchurian)
textmanchurian.grid(row=1 , column=1)

textpaneerchilli = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_paneerchilli)
textpaneerchilli.grid(row=2 , column=1)

textpaneerhandi = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_paneerhandi)
textpaneerhandi.grid(row=3 , column=1)

textsahipaneer = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_sahipaneer)
textsahipaneer.grid(row=4 , column=1)

textroti = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_roti)
textroti.grid(row=5 , column=1)

textrice = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_rice)
textrice.grid(row=6 , column=1)

textdaal = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_daal)
textdaal.grid(row=7 , column=1)

textfries = Entry(foodFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_fries)
textfries.grid(row=8 , column=1)

# Drinks

buttermilk = Checkbutton(drinksFrame , text = 'Butter Milk' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var10 , command=buttermilk)
buttermilk.grid(row=0 , column=0 , sticky=W)

lassi = Checkbutton(drinksFrame , text = 'Lassi' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var11 , command=lassi)
lassi.grid(row=1 , column=0 , sticky=W)

roselassi = Checkbutton(drinksFrame , text = 'Rose Lassi' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var12 ,command = roselassi)
roselassi.grid(row=2 , column=0 , sticky=W)

pops = Checkbutton(drinksFrame , text = 'Pops' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var13 , command=pops)
pops.grid(row=3 , column=0 , sticky=W)

mocktails = Checkbutton(drinksFrame , text = 'Mock-Tails' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var14 , command=mocktails)
mocktails.grid(row=4 , column=0 , sticky=W)

cocktails = Checkbutton(drinksFrame , text = 'Cock-Tails' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var15 , command=cocktails)
cocktails.grid(row=5 , column=0 , sticky=W)

coco = Checkbutton(drinksFrame , text = 'Coco' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var16 , command=coco)
coco.grid(row=6 , column=0 , sticky=W)

jaljeera = Checkbutton(drinksFrame , text = 'Jal-Jeera' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var17 , command=jaljeera)
jaljeera.grid(row=7 , column=0 , sticky=W)

falooda = Checkbutton(drinksFrame , text = 'Falooda' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var18 , command=falooda)
falooda.grid(row=8 , column=0 , sticky=W)

# Entry fields for drink items

textbuttermilk = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_buttermilk)
textbuttermilk.grid(row=0 , column=1)

textlassi = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_lassi)
textlassi.grid(row=1 , column=1)

textroselassi = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_roselassi)
textroselassi.grid(row=2 , column=1)

textpops = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_pops)
textpops.grid(row=3 , column=1)

textmocktails = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_mocktails)
textmocktails.grid(row=4 , column=1)

textcocktails = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_cocktails)
textcocktails.grid(row=5 , column=1)

textcoco = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_coco)
textcoco.grid(row=6 , column=1)

textjaljeera = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_jaljeera)
textjaljeera.grid(row=7 , column=1)

textfalooda = Entry(drinksFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_falooda)
textfalooda.grid(row=8 , column=1)

#Dessert

paan = Checkbutton(dessertFrame , text = 'Paan' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var19 , command = paan)
paan.grid(row=0 , column=0 , sticky=W)

brownies = Checkbutton(dessertFrame , text = 'Brownies' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var20 , command = brownies)
brownies.grid(row=1 , column=0 , sticky=W)

muffins = Checkbutton(dessertFrame , text = 'Muffins' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var21 , command = muffins)
muffins.grid(row=2 , column=0 , sticky=W)

gulabjamun = Checkbutton(dessertFrame , text = 'Gulab Jamun' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var22 , command = gulabjamun)
gulabjamun.grid(row=3 , column=0 , sticky=W)

rasmalai = Checkbutton(dessertFrame , text = 'Rasmalai' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var23 , command = rasmalai)
rasmalai.grid(row=4 , column=0 , sticky=W)

blackforest = Checkbutton(dessertFrame , text = 'Black-Forest' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var24 , command = blackforest)
blackforest.grid(row=5 , column=0 , sticky=W)

icecream = Checkbutton(dessertFrame , text = 'Ice-Cream' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var25 , command = icecream)
icecream.grid(row=6 , column=0 , sticky=W)

candy = Checkbutton(dessertFrame , text = 'Candy' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var26 , command = candy)
candy.grid(row=7 , column=0 , sticky=W)

waffles = Checkbutton(dessertFrame , text = 'Waffles' , font=('Times New Roman' , 18 , 'bold') ,fg="Black" , bg="lightgreen" ,onvalue=1 , offvalue=0 , variable=var27 , command=waffles)
waffles.grid(row=8 , column=0 , sticky=W)

#Entry fields for Drinks items

textpaan = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_paan)
textpaan.grid(row=0 , column=1)

textbrownies = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_brownies)
textbrownies.grid(row=1 , column=1)

textmuffins = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_muffins)
textmuffins.grid(row=2 , column=1)

textgulabjamun = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_gulabjamun)
textgulabjamun.grid(row=3 , column=1)

textrasmalai = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_rasmalai)
textrasmalai.grid(row=4 , column=1)

textblackforest = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_blackforest)
textblackforest.grid(row=5 , column=1)

texticecream = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_icecream)
texticecream.grid(row=6 , column=1)

textcandy = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_candy)
textcandy.grid(row=7 , column=1)

textwaffles = Entry(dessertFrame , font = ('Times New Roman' , 18 , 'bold') , bd=7 , width=6 , state=DISABLED , textvariable=e_waffles)
textwaffles.grid(row=8 , column=1)

#Cost Labels and Entry Fields

labelCostofFood = Label(costFrame , text='Cost of Food' , font = ('Times New Roman' , 18 , 'bold') , bg="lightgreen" , fg="black")
labelCostofFood.grid(row=0 , column=0)

textCostofFood = Entry(costFrame , font = ("Times New Roman" , 18 , "bold") , bd = 6 , width=14 , state = 'readonly' , textvariable=costoffoodvar)
textCostofFood.grid(row=0 , column=1 , padx = 41)

labelCostofDrinks = Label(costFrame , text='Cost of Drinks' , font = ('Times New Roman' , 18 , 'bold') , bg="lightgreen" , fg="black")
labelCostofDrinks.grid(row=1 , column=0)

textCostofDrinks = Entry(costFrame , font = ("Times New Roman" , 18 , "bold") , bd = 6 , width=14 , state = 'readonly' , textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1 , column=1 , padx = 41)

labelCostofDessert = Label(costFrame , text='Cost of Dessert' , font = ('Times New Roman' , 16 , 'bold') , bg="lightgreen" , fg="black")
labelCostofDessert.grid(row=2 , column=0)

textCostofDessert = Entry(costFrame , font = ("Times New Roman" , 18 , "bold") , bd = 6 , width=14 , state = 'readonly' , textvariable=costofdessertvar)
textCostofDessert.grid(row=2 , column=1 , padx = 41)

labelSubTotal = Label(costFrame , text='Sub-Total' , font = ('Times New Roman' , 18 , 'bold') , bg="lightgreen" , fg="black")
labelSubTotal.grid(row=0 , column=2)

textSubTotal = Entry(costFrame , font = ("Times New Roman" , 18 , "bold") , bd = 6 , width=14 , state = 'readonly' , textvariable=subtotalvar)
textSubTotal.grid(row=0 , column=3 , padx = 41)

labelServiceTax = Label(costFrame , text='Service-Tax' , font = ('Times New Roman' , 16 , 'bold') , bg="lightgreen" , fg="black")
labelServiceTax.grid(row=1 , column=2)

textServiceTax = Entry(costFrame , font = ("Times New Roman" , 18 , "bold") , bd = 6 , width=14 , state = 'readonly' , textvariable=servicetaxvar)
textServiceTax.grid(row=1 , column=3 , padx = 41)

labelTotalCost = Label(costFrame , text='Total-Cost' , font = ('Times New Roman' , 18 , 'bold') , bg="lightgreen" , fg="black")
labelTotalCost.grid(row=2 , column=2)

textTotalCost = Entry(costFrame , font = ("Times New Roman" , 18 , "bold") , bd = 6 , width=14 , state = 'readonly' , textvariable=totalcostvar)
textTotalCost.grid(row=2 , column=3 , padx = 41)

# Buttons 
buttonTotal = Button(buttonFrame , text = "Total" , font=("Times New Roman" , 14 , "bold") , fg = "black" , bg = "lightgreen" , bd = 3 , padx = 5 , command = totalcost)
buttonTotal.grid(row = 0 , column=0)

buttonReceipt = Button(buttonFrame , text = "Receipt" , font=("Times New Roman" , 14 , "bold") , fg = "black" , bg = "lightgreen" , bd = 3 , padx = 5 , command = receipt)
buttonReceipt.grid(row = 0 , column=1)

buttonSave = Button(buttonFrame , text = "Save" , font=("Times New Roman" , 14 , "bold") , fg = "black" , bg = "lightgreen" , bd = 3 , padx = 5 , command = save)
buttonSave.grid(row = 0 , column=2)

buttonSend = Button(buttonFrame , text = "Send" , font=("Times New Roman" , 14 , "bold") , fg = "black" , bg = "lightgreen" , bd = 3 , padx = 5 , command = send)
buttonSend.grid(row = 0 , column=3)

buttonReset = Button(buttonFrame , text = "Reset" , font=("Times New Roman" , 14 , "bold") , fg = "black" , bg = "lightgreen" , bd = 3 , padx = 5 , command = reset)
buttonReset.grid(row = 0 , column=4)

# Text area for Receipt

textReceipt = Text(recieptFrame , font=("Times New Roman" , 12 , "bold") , bd = 3 , width=44 , height=14)
textReceipt.grid(row=0 , column=0)

# Calculator 
operator = ''
def buttonClick(numbers) :
    global operator
    operator = operator + numbers
    calculatorField.delete(0 , END)
    calculatorField.insert(END , operator)

def clear() :
    global operator
    operator = ''
    calculatorField.delete(0 ,END)

def answer() :
    global operator
    result = str(eval(operator))
    calculatorField.delete(0 ,END)
    calculatorField.insert(0 , result)
    operator = ''

calculatorField = Entry(calculatorFrame , font=("Time New Roman" , 16 , "bold") , width=30 , bd=4)
calculatorField.grid(row=0 , column=0 , columnspan=4)

button7 = Button(calculatorFrame , text = "7" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" , bd=6 , width=6 , command = lambda:buttonClick('7'))
button7.grid(row=1 , column=0)

button8 = Button(calculatorFrame , text = "8" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" , bd=6 , width=6 , command = lambda:buttonClick('8'))
button8.grid(row=1 , column=1)

button9 = Button(calculatorFrame , text = "9" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" , bd=6 , width=6 ,  command = lambda:buttonClick('9'))
button9.grid(row=1 , column=2)

buttonPlus = Button(calculatorFrame , text = "+" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" , bd=6 , width=6 , command = lambda:buttonClick('+'))
buttonPlus.grid(row=1 , column=3)

button4 = Button(calculatorFrame , text = "4" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('4'))
button4.grid(row=2 , column=0)

button5 = Button(calculatorFrame , text = "5" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('5'))
button5.grid(row=2 , column=1)

button6 = Button(calculatorFrame , text = "6" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('6'))
button6.grid(row=2 , column=2)

buttonminus = Button(calculatorFrame , text = "-" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('-'))
buttonminus.grid(row=2 , column=3)

button1 = Button(calculatorFrame , text = "1" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('1'))
button1.grid(row=3 , column=0)

button2 = Button(calculatorFrame , text = "2" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('2'))
button2.grid(row=3 , column=1)

button3 = Button(calculatorFrame , text = "3" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('3'))
button3.grid(row=3 , column=2)

buttonmult = Button(calculatorFrame , text = "*" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('*'))
buttonmult.grid(row=3 , column=3)

buttonAns = Button(calculatorFrame , text = "Ans" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = answer)
buttonAns.grid(row=4 , column=0)

buttonClear = Button(calculatorFrame , text = "Clear" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = clear)
buttonClear.grid(row=4 , column=1)

button0 = Button(calculatorFrame , text = "0" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('0'))
button0.grid(row=4 , column=2)

buttondiv = Button(calculatorFrame , text = "/" , font = ("Times New Roman" , 16 , "bold") , fg = "black" , bg="lightgreen" ,width=6 , bd=6 , command = lambda:buttonClick('/'))
buttondiv.grid(row=4 , column=3)

root.mainloop()