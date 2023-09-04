  Mail_List  =  ("ajeetha.r2020@gmail.com","akash.s2020@gmail.com",
                         "akasthiyan.r2020@gmail.com”,"anishkumar.a2020@gmail.com",
                         "aruna.s2020@gmail.com","balaji.v2020@gmail.com",
                        "daniel.at2020@gmail.com","danush.s2020@gmail.com",
                        "ganesh.p2020@gmail.com","deeksha.d2020@gmail.com",
                         "gayathri.p2020@gmail.com","gayathi.s2020@gmail.com",
                         "govarthini.p2020@gmail.com","hamsavarthini.k2020@gmail.com",
                         "harikrishnan.t2020@gmail.com","harishankar.b2020@gmail.com",
                         "harithamonshe.e2020@gmail.com","kanishka.p2020@gmail.com",
                         "kanithra.s2020@gmail.com","kathirvelan.a2020@gmail.com",
                         "keerthana.r2020@gmail.com","lokeshkumar.l2020@gmail.com",
                         "madhusuriya.s2020@gmail.com","manikandan.r2020@gmail.com",
                         "meghasri.r2020@gmail.com","miruthubashini.a2020@gmail.com",
                         "muraliprasanth.s2020@gmail.com","narmadha.d2020@gmail.com",
                         "naveen.r2020@gmail.com","navin.m2020@gmail.com",
                         "niranjana.k2020@gmail.com","nowsathbegum.m2020@gmail.com",
                         "pavithran.r2020@gmail.com","ponezhil.r2020@gmail.com",
                         "pratap.r2020@gmail.com","priyadharshini.g2020@gmail.com",
                         "rashikaroshini.r2020@gmail.com","rithika.m2020@gmail.com",
                         "sadhanaa.r2020@gmail.com","sandeep.r2020@gmail.com",
                         "sangamithraa.v2020@gmail.com","sanjana.r2020@gmail.com",
                         "santhiya.k2020@gmail.com","shalini.s2020@gmail.com",
                         "shrihari.b2020@gmail.com","sridharan.s2020@gmail.com",
                         "subasini.j2020@gmail.com","suruthi.d2020@gmail.com",
                        "swedha.m2020@gmail.com","swethapalpandiyan.s2020@gmail.com",
                        "Thejaskumar.b2020@gmail.com","uditpranav.s2020@gmail.com",
                        "yuvasri.s2020@gmail.com")
  Mail_of_Student = (input("Enter the Mail of a Student:"))
def Find_a_Mail(Student_Mail):                     
   for aStudent_id in Mail_List:
        if Student_Mail == aStudent_id:
             return True
        else:
            return False
Student_Status = Find_a_Mail(Mail_of_Student)
 if Student_Status is True:
        print("Student_Mail is in the List")
else:
 print("Student_Mail is not in the List")

OUTPUT:
Enter the Mail of a Student:Thejaskumar.b2020@gmail.com
Student_Mail is in the List
