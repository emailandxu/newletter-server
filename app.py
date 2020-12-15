

_links = [
"http://newsletter.kust.edu.cn/info/1107/1021.htm",
"http://newsletter.kust.edu.cn/info/1107/1068.htm",
"http://newsletter.kust.edu.cn/info/1107/1069.htm",
"http://newsletter.kust.edu.cn/info/1107/1060.htm",
"http://newsletter.kust.edu.cn/info/1107/1048.htm",
"http://newsletter.kust.edu.cn/info/1107/1023.htm",
"http://newsletter.kust.edu.cn/info/1107/1061.htm",
"http://newsletter.kust.edu.cn/info/1107/1062.htm",
"http://newsletter.kust.edu.cn/info/1107/1063.htm",
"http://newsletter.kust.edu.cn/info/1107/1022.htm"
]

_imgs = [
"http://newsletter.kust.edu.cn/__local/F/92/E3/C005C403F6D0CE45252F9D0B4A4_C36012BC_21DFE.png",
"http://newsletter.kust.edu.cn/__local/4/46/3B/1B80F2222AA59F236A0783D568F_C752881B_A2F71.png",
"http://newsletter.kust.edu.cn/__local/2/21/D3/57482B26FE17EDDA15F8B96DFDA_2C8C0BCE_2294B.png",
"http://newsletter.kust.edu.cn/__local/A/B3/25/1C82EBF849F4CBD53FA7F62CFF7_AE5E4AF5_13405.png",
"http://newsletter.kust.edu.cn/__local/A/F7/2D/B46EA5740680F58F6BAAB3618F4_95D60585_C4DFA.png?e=.png",
"http://newsletter.kust.edu.cn/__local/B/BF/B7/A5CD9A4F15A70CC2056BF38924D_BD2D9D75_9E756.png?e=.png",
"http://newsletter.kust.edu.cn/__local/E/74/36/C00D8C7F21647E3C37971C16EF2_A19B3405_1216B.jpg",
"http://newsletter.kust.edu.cn/__local/7/35/10/E1930CA03DE6BF2DCF94CD0944D_218995C2_164CF.png",
"http://newsletter.kust.edu.cn/__local/F/88/54/CC751757E412552E8B6C283FAD1_09128402_A2F71.png",
"http://newsletter.kust.edu.cn/__local/D/F7/1D/42E0B878A57F50EB01542C5145B_41CFE686_145AA4.png?e=.png"
]

_titles = [
"President XI Jinping Wrote Back to KUST Elite Alumni WANG Xiji",
"Emergency Response Drill Held for COVID-19 Prevention and Control for 2020 Spring Semester Opening",
"Students Are About to Return | New Smart Classrooms Are Waiting!",
"KUST Sends Letters of Concern to International Partners over COVID-19 Outbreak",
"KUST MOOC Launched on the International Platform FUN-MOOC of France",
"KUST Won 97.98 Million yuan for Key Special Project of National Key Research & Development Plan",
"Undergraduate Chinese Major Approved by Lao Ministry of Education and Sports",
"KUST Selected as Top 59 in China for Construction of Inte'l Online-teaching Platform Courses",
"Prof. Na Jing Participates in the Yunnan Talent Portrait Program and Recorded a Promo Video of Young Top Talents in Yunnan",
"Drought Resistance & Water Supply for Poverty Alleviation——KUST's Working Team Is Working Hard"
]

_sumaries = [
"The Space Day of China, which falls on April 24, is more special this year, as it marks the 50th anniversary of the successful launch of Dongfanghong-1, the country’s first …",
"On April 30, KUST carried out an emergency response drill on Chenggong Campus for the prevention and control of the COVID-19 for the opening of 2020 spring semester to improv…",
" KUST has prepared students and teachers new smart classrooms. More than 252 multimedia and smart classrooms in Chenggong Campus have completely been upgraded. With equipment…",
"When China was at the most difficult period of fighting against Covid-19, many international partners including President Joachim Schachtner of TU Clausthal in Germany and Pr…",
"Since the outbreak of COVID-19 epidemic, countries around the world have been advancing massive online education and teaching. China with the largest number of MOOCs and stud…",
"Recently, the Ministry of Science and Technology has released a draft version of the key special projects of “Resource Utilization of Solid Waste” of the national key res…",
"On May 8, according to a notice from the Ministry of Education and Sports in Laos，the Chinese major of undergraduate applied by Confucius Institute at Souphanouvong Universi…",
"On April 10, the national video conference on the construction of international online-teaching platform courses of Chinese universities was held in Beijing. It is reported b…",
'Prof. Na Jing has many honors such as the winner of "China Youth May Fourth Medal" "National Excellent Teacher" and so on. Born in 1982, he is energetic and active in thinkin…',
"Watersupply is a major issue related to poverty alleviation and people’s livelihood. Since March this year, water shortage has swept Xuanwei city as a result of the dry weat…"
]

import requests as rr
from pyquery import PyQuery as pq
import flask
r = rr.get("http://newsletter.kust.edu.cn/")
d = pq(r.content.decode("utf-8"))
d.make_links_absolute(base_url="http://newsletter.kust.edu.cn/")


titles = [ i.text for i in d("h3")]
sumaries = [ i.text.replace("….Read More ","").replace("\u200b","") for i in d(".imgnews1 p")]
imgs = [i.attr["src"] for i in d(".imgnews1 img").items()]
links = [i.attr["href"] for i in d(".imgnews1 a").items()]


newsletter = ""
with open("./KUST-Newsletter-1.html",'r',encoding="utf-8") as f:
    newsletter = f.read()

for _title,title in zip(_titles,titles):
    newsletter = newsletter.replace(_title,title)

for _link,link in zip(_links,links):
    newsletter = newsletter.replace(_link,link)

for _img,img in zip(_imgs,imgs):
    newsletter = newsletter.replace(_img,img)

for _sumary,sumary in zip(_sumaries,sumaries):
    newsletter = newsletter.replace(_sumary,sumary)


app = flask.Flask(__name__)

@app.route("/")
def index():
    return newsletter

app.run()