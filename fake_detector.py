import facebook
from datetime import date

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter
import numpy as np
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter as Tk

from PIL import ImageTk, Image

#Checking user`s friends
class Friends:
    def __init__(self, counter, user_id):
        self.counter = counter
        self.user_id = user_id

    def friends(self, counter, user_id):
        count = counter
        user_id = user_id
        fr = graph.get_object(id=user_id, fields='friends')
        fr = fr.get('friends', None)
        fr = fr.get('summary', None)
        fr = fr.get('total_count', None)
        if fr == 0:
            count += 3
        elif fr < 20 and fr > 0:
            count += 2
        elif fr >= 300 and fr <= 1000:
            count += 1
        elif fr > 1000:
            count += 2
        else:
            count += 0
        return count

#Checking user`s photos and cover
class Photos:
    def __init__(self, counter, user_id):
        self.counter = counter
        self.user_id = user_id

    def checkPhoto(self, counter, user_id):
        count = counter
        user_id = user_id
        photoAvatar = graph.get_object(id=user_id, fields='picture')
        photoAvatar = photoAvatar.get('picture')
        photoAvatar = photoAvatar.get('data')
        photoAvatar = photoAvatar.get('is_silhouette')
        if photoAvatar == True:
            count += 3
        else:
            count += 0
        return count

    def numberOfPhotosImChecked(self, counter, user_id):
        count = counter
        numberOfPhotoes = graph.get_object(id=user_id, fields='photos')
        numberOfPhotoes = numberOfPhotoes.get('photos', None)
        if numberOfPhotoes == None:
            count += 3
            return count
        else:
            numberOfPhotoes = len(numberOfPhotoes)
            if numberOfPhotoes == 0:
                count += 3
            elif numberOfPhotoes > 0 and numberOfPhotoes <= 10:
                count += 1
            elif numberOfPhotoes > 100:
                count += 2
            else:
                count += 0
        return count

    def photoCover(self, counter, user_id):
        counter = counter
        user_id = user_id
        photo_cover = graph.get_object(id=user_id, fields='cover')
        photo_cover = photo_cover.get('cover')
        if photo_cover == None:
            counter += 3
        else:
            counter += 0
        return counter

#Checking user`s posts
class Posts:
    def __init__(self, counter, user_id):
        self.counter = counter
        self.user_id = user_id

    def numberOfPosts(self, counter, user_id):
        user_id = user_id
        count = counter
        posts = graph.get_object(id=user_id, fields='posts')
        posts = posts.get('posts', None)
        if posts == None:
            count += 3
            return count
        else:
            posts = posts.get('data', None)
            posts = len(posts)
            if posts >= 3 and posts <= 9:
                count += 2
                return count
            elif posts >= 10 and posts <= 50:
                count += 0
                return count
            elif posts > 100:
                count += 2
                return count
            elif posts <= 2:
                count += 3
                return count
            else:
                count += 1
                return count

#Checking user`s personal information and name
class PersonalInfo:
    def __init__(self, counter, user_id):
        self.counter = counter
        self.user_id = user_id

    def birthday(self, counter, user_id):
        user_id = user_id
        ob = graph.get_object(id=user_id, fields='birthday')
        count = counter
        birth = ob.get('birthday', None)
        if birth == None:
            count += 2
            return count
        else:
            birth = str(birth)
            birth = birth[6:10]
            birth = int(birth)

            if birth > 2009:
                count += 1
            elif birth < 1932:
                count += 1
            else:
                count += 0
        return count

    def isUserInformationExist(self, counter, user_id):
        count = counter
        info_educ = graph.get_object(id=user_id, fields='education')
        info_city = graph.get_object(id=user_id, fields='hometown')
        info_work = graph.get_object(id=user_id, fields='work')
        info_email = graph.get_object(id=user_id, fields='email')
        info_relat = graph.get_object(id=user_id, fields='relationship_status')

        info_educ = info_educ.get('education', None)
        info_city = info_city.get('hometown', None)
        info_work = info_work.get('work', None)

        if info_educ == None:
            count += 1
        else:
            count += 0

        if info_city == None:
            count += 2
        else:
            count += 0

        if info_work == None:
            count += 1
        else:
            count += 0

        info_email = len(info_email)
        if info_email > 1:
            count += 1
        else:
            count += 0

        info_relat = len(info_relat)
        if info_relat > 3:
            count += 0
        else:
            count += 1

        count = int(count/2)
        return count

    def timeComparing(self, counter, user_id):
        user_id = user_id
        count = counter
        update = graph.get_object(id=user_id, fields='updated_time')
        update = update.get('updated_time')
        today = date.today()

        today = str(today)
        update = str(update)
        update = update[:10]

        updateYear = update[0:4]
        updateMonth = update[5:7]
        updateDay = update[8:10]

        todayYear = today[0:4]
        todayMonth = today[5:7]
        todayDay = today[8:10]

        resultYear = int(todayYear) - int(updateYear)
        resultMonth = int(todayMonth) - int(updateMonth)
        resultDay = int(todayDay) - int(updateDay)

        if resultYear >= 1:
            count += 3
        else:
            if resultMonth >= 1:
                count += 2
            else:
                if resultDay >= 14:
                    count += 1
                else:
                    count += 0
        return count

    def getCountry(self, user_id):
        location = graph.get_object(id=user_id, fields='location')
        location = location.get('location')
        if location == None:
            country = 3
        else:
            location = location.get('id')
            country = graph.get_object(id=location, fields='location')
            country = country.get('location')
            country = country.get('country')
        return country

    def getName(self, user_id):
        name = graph.get_object(id=user_id, fields='name')
        name = name.get('name')
        name = name.split(' ')
        name = name[0]
        return name

    def getGender(self, user_id):
        gender = graph.get_object(id=user_id, fields='gender')
        gender = gender.get('gender')
        return gender

    def compareNameAndCountry(self, counter, user_id):
        user_id = user_id
        count = counter
        country = self.getCountry(user_id)
        if country == 3:
            count += 3
            return count
        else:
            name = self.getName(user_id)
            gender = self.getGender(user_id)
            if country == 'Ukraine' or country == 'Russia':
                if gender == 'male':
                    file_names = open("D:/GitProjects/Class_test/List_of_names/Slavonic/slavonic_male_names.txt", 'r')
                    lines = file_names.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == name:
                            count += 0
                            return count
                    file_names_trlrtd = open(
                        "D:/GitProjects/Class_test/List_of_names/Slavonic/slavonic_male_names_transliterated.txt", 'r')
                    lines = file_names_trlrtd.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == name:
                            count += 0
                            return count
                else:
                    file_names = open("D:/GitProjects/Class_test/List_of_names/Slavonic/slavonic_female_names.txt", 'r')
                    lines = file_names.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == name:
                            count += 0
                            return count
                    file_names_trlrtd = open(
                        "D:/GitProjects/Class_test/List_of_names/Slavonic/slavonic_female_names_transliterated.txt",
                        'r')
                    lines = file_names_trlrtd.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == name:
                            count += 0
                            return count
            elif country == 'United Kingdom' or country == 'United States':
                if gender == 'male':
                    file_names = open("D:/GitProjects/Class_test/List_of_names/English/eng_names_male_ext.txt", 'r')
                    lines = file_names.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == name:
                            count += 0
                            return count
                else:
                    file_names = open("D:/GitProjects/Class_test/List_of_names/English/eng_names_female_ext.txt", 'r')
                    lines = file_names.readlines()
                    for line in lines:
                        line = line.strip()
                        if line == name:
                            count += 0
                            return count
            else:
                count += 2
                return count

#Checking user`s number of likes
class Likes:
    def __init__(self, counter, user_id):
        self.counter = counter
        self.user_id = user_id

    def likesUserHavePut(self, counter, user_id):
        user_id = user_id
        count = counter
        likes = graph.get_object(id=user_id, fields='likes')
        likes = likes.get('likes', None)
        if likes == None:
            count += 3
            return count
        else:
            likes = likes.get('data', None)
            likes = len(likes)
            if likes == 0:
                count += 3
            elif likes > 0 and likes < 10:
                count += 2
            elif likes > 100 and likes < 1000:
                count += 0
            elif likes >= 10 and likes <=100:
                count += 1
            else:
                count += 1
        return count

    def postsLikes(self, counter, user_id):
        user_id = user_id
        count = counter
        posts = graph.get_object(id=user_id, fields='posts')
        posts = posts.get('posts', None)
        posts = posts.get('data', None)
        number_of_posts = len(posts)

        posts = str(posts)
        i = 0
        number_of_likes = 0
        while i < len(posts):
            index = posts.find("'id':", i, )
            link = posts[index + 7:index + 38:1]
            obj = graph.get_object(id=link, fields='likes')
            obj = obj.get('likes', None)

            if obj == None:
                number_of_likes += 0
            else:
                obj = obj.get('data', None)
                number_of_likes += len(obj)
            i = index + 45

        number_of_likes = number_of_likes / number_of_posts
        if number_of_likes <= 1:
            count += 3
        elif number_of_likes > number_of_posts:
            count += 2
        else:
            count += 0
        return count

class Result:
    def __init__(self, counter, user_id):
        self.counter = counter
        self.user_id = user_id

    def result(self, counter, user_id):
        counter = counter
        user_id = user_id

        friends = Friends(counter=counter, user_id=user_id)
        friendsF = friends.friends(counter, user_id)

        photos = Photos(counter=counter, user_id=user_id)
        photosCP = photos.checkPhoto(counter, user_id)
        photosNOPIC = photos.numberOfPhotosImChecked(counter, user_id)
        photoC = photos.photoCover(counter, user_id)

        posts = Posts(counter=counter, user_id=user_id)
        postsP = posts.numberOfPosts(counter, user_id)

        info = PersonalInfo(counter=counter, user_id=user_id)
        infoB = info.birthday(counter, user_id)
        infoIUIE = info.isUserInformationExist(counter, user_id)
        infoTC = info.timeComparing(counter, user_id)
        infoN = info.compareNameAndCountry(counter, user_id)

        likes = Likes(counter=counter, user_id=user_id)
        likesUHP = likes.likesUserHavePut(counter, user_id)
        likesPL = likes.postsLikes(counter, user_id)

        file = open("total.txt", 'w')
        file.write(str(friendsF) + str(photosCP) + str(photosNOPIC) + str(photoC) + str(postsP) + str(infoB) + str(infoIUIE) + str(infoTC) + str(infoN) + str(likesUHP) + str(likesPL))
        file.close()
        file = open("total.txt", 'r')
        mas = file.read()
        file.close()
        mas = list(mas)
        print(mas)

        #Histogram
        figure = Figure(figsize=(6, 3), dpi=100)
        ax = figure.add_subplot(111)

        objects = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')
        y_pos = np.arange(len(objects))  # the x locations for the groups

        barchart = ax.bar(y_pos, mas, align='center', alpha=0.5)
        barchart[0].set_color('orange')
        barchart[1].set_color('red')
        barchart[2].set_color('red')
        barchart[3].set_color('red')
        barchart[4].set_color('green')
        barchart[5].set_color('yellow')
        barchart[6].set_color('yellow')
        barchart[7].set_color('yellow')
        barchart[8].set_color('yellow')
        barchart[9].set_color('blue')
        barchart[10].set_color('blue')

        ax.set_xticks(np.arange(len(objects)))
        ax.set_xticklabels(objects, fontdict=None, minor=False)

        ax.yaxis.grid()


        canvas = FigureCanvasTkAgg(figure, master=frame_graph)

        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        result = 3*friendsF + 3*photosCP + 2*photosNOPIC + 1*photoC + 2*postsP + 1*infoB + 2*infoIUIE + 1*infoTC + 1*infoN + 2*likesUHP + 2*likesPL
        print(result)
        result = (result/65)*100
        result = round(result, 2)

        result = str(result)

        return result

    def __str__(self, result):
        result = self.result
        return result

def Check():
    result = Result(counter=counter, user_id=user_id)
    result = result.result(counter, user_id)
    pb["value"] = float(result)

    if float(result) < 40.0:
        status_entry.insert(1.0, "The page is clear")
        status_entry.tag_add("here", "1.0", "1.64")
        status_entry.tag_config("here", foreground="green")
    elif float(result) > 60.0:
        status_entry.insert(1.0, "The page is fake")
        status_entry.tag_add("here", "1.0", "1.64")
        status_entry.tag_config("here", foreground="red")
    else:
        status_entry.insert(1.0, "No information")
        status_entry.tag_add("here", "1.0", "1.64")
        status_entry.tag_config("here", foreground="yellow")

    label_result = Label(frame_progressbar, font='TimesNewRoman 14')
    label_result['text'] = 'Chance the page is fake is ' + result + '%'
    label_result.pack()

    print('Chance the page is fake is ' + result + '%')

root = tk.Tk()

root.resizable(width=True, height=True)
root.title("Fakes in Facebook")

frame_info = Frame(root)
frame_progressbar = Frame(root, bd=5)
frame_status = Frame(root, bd=5)
frame_graph = Frame(root, bd=5)

counter = 0
user_id = 'me'
file_token = open('access_token.txt', 'r')
access_token = file_token.read()
file_token.close()
graph = facebook.GraphAPI(access_token=access_token, version=2.8)
permissions = graph.get_permissions(user_id=user_id)

id = graph.get_object(id=user_id, fields='id')
id = id.get('id', None)
label_id = Label(frame_info, font='TimesNewRoman 14')
label_id['text'] = "User id: " + id
label_id.pack()

check_button = Button(frame_info, width=15, height=5, fg="black", font='TimesNewRoman 14', command=Check)
check_button["text"] = "Check page"
check_button.bind("Check page")
check_button.pack()

style_pb = ttk.Style()
style_pb.theme_use('classic')
style_pb.configure("red.Horizontal.TProgressbar", troughcolor='green', background='red')

pb = ttk.Progressbar(frame_progressbar, style="red.Horizontal.TProgressbar", length=300, mode="determinate")
pb.pack()

label_status = Label(frame_status, font='TimesNewRoman 14')
label_status['text'] = "Status: "
label_status.pack()

status_entry = Text(frame_status, height=1, width=17, font='Consolas 12')
status_entry.pack()

#LEGEND
im = Image.open('Legend.jpg')
tkimage = ImageTk.PhotoImage(im)
label_image = tkinter.Label(frame_graph, image=tkimage)
label_image.config(height=294, width=200)
label_image.pack(side=RIGHT)

frame_info.pack()
frame_progressbar.pack()
frame_status.pack()
frame_graph.pack()

root.mainloop()