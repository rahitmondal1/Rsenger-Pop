
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Ellipse, Line, RoundedRectangle, Triangle
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.text import LabelBase
from kivy.utils import platform
import math, threading

TOTAL = 600.0

SCENES = [
("01 • HERO ENTRY","ভোরের গ্রাম • 00:00–01:00",0,60,[
(0,"NARRATOR","সূর্য উঠেছে। গ্রাম জেগেছে। কিন্তু আজ একটা বড় ঝামেলা অপেক্ষা করছে।"),
(10,"ভোলা","রুদ্র! রুদ্র! সর্বনাশ হয়ে গেছে!"),(19,"রুদ্র","সর্বনাশ হলে মানুষ দৌড়ায় কেন?"),
(27,"ভোলা","ভয় পেয়েছি!"),(34,"রুদ্র","আমি ভয় পেলে... অন্যরা দৌড়ায়।"),
(44,"ভোলা","এই dialogueটা আগে থেকে মুখস্থ ছিল?"),(50,"রুদ্র","না। মাথায় এল।"),
(56,"NARRATOR","আর সেই মুহূর্তেই শুরু হলো গোঁফের জোরে রাজার গল্প।")]),
("02 • TEA STALL BOSS","মিঠুর দোকান • 01:00–02:00",60,120,[
(60,"মিঠু","চা, বিস্কুট আর খবর—তিনটাই গরম।"),(70,"কালু দা","এই গ্রামে আমার অনুমতি ছাড়া একটা পাতাও নড়বে না!"),
(80,"NARRATOR","ঠিক তখনই একটা পাতা উড়ে এসে কালুর মুখে পড়ল।"),(86,"মিঠু","পাতাটা মনে হয় permission নেয়নি."),
(94,"কালু দা","চুপ!"),(100,"রুদ্র","একটা চা দে।"),(107,"কালু দা","আমার সামনে দাঁড়িয়ে কথা বলছিস?"),
(113,"রুদ্র","চা দোকানটা আপনার সামনে, না আপনার পিছনে?")]),
("03 • মাঠের ঝামেলা","গ্রামের মাঠ • 02:00–03:00",120,180,[
(120,"কালু দা","কাল থেকে এই মাঠ আমার!"),(130,"সরলা মাসি","তোর বাপের?"),(136,"কালু দা","না।"),
(140,"সরলা মাসি","তাহলে তোর কী?"),(146,"পটলা","Boss, জমির কাগজ আছে?"),(152,"কালু দা","তুই আমার লোক, না ওদের লোক?"),
(158,"রুদ্র","মাঠটা গ্রামের।"),(165,"কালু দা","তুই আমাকে আটকাবি?"),(171,"রুদ্র","আমি একা না।"),(176,"ভোলা","আমি আছি।"),(179,"রুদ্র","তুই পিছনে থাক।")]),
("04 • MASS TRAINING","রুদ্রের উঠোন • 03:00–04:00",180,240,[
(180,"ভোলা","আমাকেও তোমার মতো mass বানাও!"),(188,"রুদ্র","প্রথমে হাঁটা শিখ।"),
(198,"NARRATOR","রুদ্র ধীরে হাঁটে। ভোলা সেটা দেখে আরও ধীরে হাঁটে।"),(205,"ভোলা","এইভাবে?"),
(210,"রুদ্র","না। তুই হাঁটছিস না, Wi-Fi খুঁজছিস।"),(220,"ভোলা","তাহলে গোঁফে হাত দেব?"),
(227,"ভোলা","আহ! নাক টেনে ফেললাম!"),(233,"রুদ্র","তোর গোঁফেরও confidence নেই।")]),
("05 • VILLAIN PLAN","গোপন ঘর • 04:00–05:00",240,300,[
(240,"কালু দা","রুদ্রকে সরাতে হবে।"),(248,"পটলা","কোথায় সরাব?"),(254,"কালু দা","গ্রাম থেকে!"),
(260,"পটলা","বাসে?"),(266,"কালু দা","আমি মানুষটার কথা বলছি!"),(275,"NARRATOR","কালুর plan—মিথ্যা অভিযোগ, আর রুদ্রকে ফাঁসানো।"),
(286,"পটলা","আর যদি আমি আগে পালাই?"),(294,"কালু দা","তাহলে তোকে আগে আটকাব।")]),
("06 • THE TRAP","গ্রামের চত্বর • 05:00–06:00",300,360,[
(300,"NARRATOR","পরদিন সকালে রুদ্রকে গ্রামের মাঝখানে আটকানো হলো।"),(310,"কালু দা","এবার তুই শেষ!"),
(317,"রুদ্র","শেষ?"),(322,"কালু দা","হ্যাঁ।"),(326,"রুদ্র","আমার সিনেমা এখনও এক ঘণ্টা বাকি।"),
(334,"ভোলা","কিন্তু সিনেমা তো দশ মিনিটের!"),(340,"রুদ্র","তুই mood নষ্ট করিস না।"),
(348,"সরলা মাসি","এক মিনিট। কাগজটা পড়েছিস?"),(355,"পটলা","Boss... আমাদের plan-এর plan-ই ছিল না।")]),
("07 • আসল হিসাব","মিঠুর দোকান • 06:00–07:00",360,420,[
(360,"মিঠু","আমি সব জানি।"),(368,"ভোলা","তাহলে এতদিন বলিসনি কেন?"),(374,"মিঠু","চা খেতে খেতে ভুলে গেছিলাম।"),
(380,"সরলা মাসি","কালু বহুদিন ধরে গ্রামের মানুষকে ঠকাচ্ছে।"),(390,"রুদ্র","এবার হিসাব হবে।"),(400,"ভোলা","হিসাব মানে?"),
(405,"রুদ্র","যেটা নিয়েছিস সেটা ফেরত।"),(412,"ভোলা","আর চায়ের টাকা?"),(417,"রুদ্র","সেটাও।")]),
("08 • CHAOS","মাঠ • 07:00–08:10",420,490,[
(420,"NARRATOR","কালু তার লোকজন নিয়ে এল। সামনে রুদ্র। পাশে ভোলা।"),(428,"ভোলা","রুদ্র... লোক অনেক।"),
(434,"রুদ্র","দেখেছি।"),(440,"ভোলা","আমরা দুইজন।"),(446,"রুদ্র","সেটাও দেখেছি।"),
(451,"ভোলা","তাহলে?"),(456,"রুদ্র","কমেডি সিনেমায় হিসাব মানুষ দিয়ে হয় না। Timing দিয়ে হয়।"),
(466,"কালু দা","ধর ওকে!"),(475,"NARRATOR","Chaos শুরু। একজন এদিকে, আরেকজন ওদিকে।"),
(482,"ভোলা","এই যে দাঁড়াও! আমি তোমাকে ধরতে আসছি!"),(487,"পটলা","আমাকেই কেন?")]),
("09 • FINAL SHOWDOWN","সূর্যাস্ত • 08:10–09:20",490,560,[
(490,"NARRATOR","সূর্য ডুবছে। মাঠে মুখোমুখি রুদ্র আর কালু।"),(500,"কালু দা","তুই ভাবছিস তুই জিতে গেছিস?"),
(508,"রুদ্র","ভাবছি না।"),(514,"কালু দা","তাহলে?"),(519,"রুদ্র","দেখছি।"),
(526,"কালু দা","তোর সবচেয়ে বড় শক্তি কী?"),(533,"রুদ্র","আমার গোঁফ না।"),
(540,"রুদ্র","আমার পাশে যারা দাঁড়ায়... তারা।"),(548,"NARRATOR","পিছনে পুরো গ্রাম এসে দাঁড়াল।"),
(556,"সরলা মাসি","হিসাব করতে লোক লাগে।")]),
("10 • THE END","গ্রামের উৎসব • 09:20–10:00",560,600,[
(560,"NARRATOR","কালুর দাপট শেষ। মাঠ গ্রামের। সবাই খুশি।"),(568,"ভোলা","আজ থেকে আমিও hero!"),
(575,"রুদ্র","কেন?"),(580,"ভোলা","আমি কালুর সঙ্গে লড়েছি。"),(584,"রুদ্র","কখন?"),
(588,"ভোলা","ও পড়ে গেলে আমি ওকে উঠতে দিইনি।"),(593,"মিঠু","চা খাবি?"),(596,"রুদ্র","দে。"),
(598,"মিঠু","টাকা?"),(599,"ভোলা","আমি side character!")])
]

CHAR_COLORS = {
"রুদ্র":(0.22,0.25,0.29,1),"ভোলা":(0.88,0.57,0.12,1),
"কালু দা":(0.32,0.15,0.18,1),"মিঠু":(0.30,0.41,0.26,1),
"সরলা মাসি":(0.48,0.30,0.45,1),"পটলা":(0.32,0.39,0.52,1)
}

def font_for_bengali():
    # If bundled NotoSansBengali-Regular.ttf is placed beside main.py, Kivy will use it.
    import os
    p=os.path.join(os.path.dirname(__file__),"NotoSansBengali-Regular.ttf")
    if os.path.exists(p):
        LabelBase.register(name="BN", fn_regular=p)
        return "BN"
    return "Roboto"

FONT = font_for_bengali()

class MovieCanvas(Widget):
    def __init__(self, app, **kw):
        super().__init__(**kw); self.app=app; self.t=0; self.scene=-1
        Clock.schedule_interval(self.draw,1/30)

    def draw(self, dt):
        self.t=self.app.elapsed
        self.canvas.clear()
        with self.canvas:
            # Cinematic sky
            phase=(self.t/TOTAL)
            Color(0.08+0.18*phase,0.13+0.12*phase,0.22+0.08*phase)
            Rectangle(pos=self.pos,size=self.size)
            Color(0.25+0.30*(1-phase),0.43+0.12*(1-phase),0.58+0.08*(1-phase))
            Rectangle(pos=(0,self.height*.38),size=(self.width,self.height*.42))
            # sun
            sx=self.width*.80 - self.width*.18*phase
            sy=self.height*.80 - self.height*.38*phase
            Color(1.0,.72,.32,.95)
            Ellipse(pos=(sx-45,sy-45),size=(90,90))
            # mountains
            Color(.25,.38,.46,.75)
            for x in range(-100,int(self.width)+300,260):
                Triangle(points=[x,self.height*.38,x+130,self.height*.65,x+260,self.height*.38])
            # ground
            Color(.22,.39,.18,1); Rectangle(pos=(0,0),size=(self.width,self.height*.38))
            # road
            Color(.55,.42,.30,1)
            Triangle(points=[self.width*.18,0,self.width*.82,0,self.width*.62,self.height*.38,self.width*.38,self.height*.38])
            Color(1,.88,.65,.35)
            Line(points=[self.width*.48,0,self.width*.49,self.height*.36],width=2)
            # houses
            for x,sc in [(self.width*.12,1),(self.width*.43,.75),(self.width*.72,1.1)]:
                self.house(x,self.height*.38,sc)
            # trees
            self.tree(self.width*.05,self.height*.38,1)
            self.tree(self.width*.91,self.height*.38,1.2)
            # actors
            speakers=[s for _,s,_ in self.current_lines()]
            positions={"মিঠু":.08,"রুদ্র":.25,"ভোলা":.43,"পটলা":.62,"কালু দা":.77,"সরলা মাসি":.88}
            for name,xp in positions.items():
                if name in speakers or name in ("রুদ্র","ভোলা","কালু দা"):
                    self.actor(name,self.width*xp,self.height*.37,1.0,name==self.app.speaker)

            # vignette
            Color(0,0,0,.22)
            Rectangle(pos=self.pos,size=(self.width,self.height*.09))
            Rectangle(pos=(0,0),size=(self.width,self.height*.09))

    def house(self,x,y,s):
        w=100*s; h=65*s
        Color(.75,.58,.40,1); Rectangle(pos=(x,y),size=(w,h))
        Color(.38,.20,.16,1)
        Triangle(points=[x-12*s,y+h,x+w/2,y+h+45*s,x+w+12*s,y+h])
        Color(.18,.12,.10,1); Rectangle(pos=(x+w*.38,y),size=(w*.22,h*.5))

    def tree(self,x,y,s):
        Color(.38,.25,.16,1); Rectangle(pos=(x,y),size=(12*s,70*s))
        Color(.14,.35,.17,1); Ellipse(pos=(x-32*s,y+48*s),size=(75*s,75*s))
        Ellipse(pos=(x+8*s,y+65*s),size=(65*s,65*s))

    def actor(self,name,x,y,s,talking):
        c=CHAR_COLORS.get(name,(.4,.4,.4,1))
        bob=math.sin(self.t*7)*3 if talking else math.sin(self.t*3)*1.5
        x+=bob
        Color(*c); Rectangle(pos=(x-28*s,y),size=(56*s,72*s))
        Color(.63,.38,.23,1); Ellipse(pos=(x-25*s,y+68*s),size=(50*s,50*s))
        Color(.08,.06,.04,1); Ellipse(pos=(x-28*s,y+103*s),size=(56*s,25*s))
        # eyes
        Color(.02,.02,.02,1); Ellipse(pos=(x-12*s,y+91*s),size=(5*s,5*s)); Ellipse(pos=(x+8*s,y+91*s),size=(5*s,5*s))
        # legs
        Color(.12,.12,.13,1); Rectangle(pos=(x-19*s,y-38*s),size=(15*s,40*s)); Rectangle(pos=(x+4*s,y-38*s),size=(15*s,40*s))
        # moustache for Rudra
        if name=="রুদ্র":
            Color(.04,.025,.018,1)
            Rectangle(pos=(x-15*s,y+79*s),size=(30*s,6*s))

    def current_lines(self):
        for _,_,start,end,lines in SCENES:
            if start <= self.t < end:
                return lines
        return SCENES[-1][4]

class MovieScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.elapsed=0; self.playing=False; self.speed=1.0
        self.speaker="NARRATOR"; self.line_index=-1; self.scene_index=-1
        root=BoxLayout(orientation="vertical",padding=8,spacing=6)
        self.movie=MovieCanvas(self)
        root.add_widget(self.movie)

        self.scene_label=Label(text="গোঁফের জোরে রাজা",font_name=FONT,font_size="20sp",size_hint_y=None,height=38,bold=True)
        root.add_widget(self.scene_label)

        self.dialogue=Label(text="একটা ছোট্ট গ্রাম।",font_name=FONT,font_size="17sp",halign="left",valign="middle",size_hint_y=None,height=105)
        self.dialogue.bind(size=lambda *_: setattr(self.dialogue,'text_size',(self.dialogue.width-20,None)))
        root.add_widget(self.dialogue)

        self.slider=Slider(min=0,max=TOTAL,value=0,size_hint_y=None,height=40)
        self.slider.bind(on_touch_up=self.seek)
        root.add_widget(self.slider)

        controls=BoxLayout(size_hint_y=None,height=48,spacing=5)
        for txt,fn in [("▶ Play",self.play),("Ⅱ Pause",self.pause),("↻ Restart",self.restart),("−5s",lambda *_:self.jump(-5)),("+5s",lambda *_:self.jump(5))]:
            b=Button(text=txt,font_name=FONT); b.bind(on_release=fn); controls.add_widget(b)
        root.add_widget(controls)

        bottom=BoxLayout(size_hint_y=None,height=44,spacing=5)
        self.speed_btn=Button(text="Speed 1×",font_name=FONT); self.speed_btn.bind(on_release=self.change_speed)
        scene_btn=Button(text="Scenes",font_name=FONT); scene_btn.bind(on_release=self.show_scenes)
        full_btn=Button(text="Fullscreen",font_name=FONT); full_btn.bind(on_release=lambda *_:App.get_running_app().toggle_fullscreen())
        bottom.add_widget(self.speed_btn); bottom.add_widget(scene_btn); bottom.add_widget(full_btn)
        root.add_widget(bottom)
        self.add_widget(root)

    def play(self,*_):
        if self.elapsed>=TOTAL:self.elapsed=0
        self.playing=True

    def pause(self,*_): self.playing=False

    def restart(self,*_):
        self.playing=False; self.elapsed=0; self.line_index=-1; self.scene_index=-1
        self.update_ui()

    def jump(self,sec): self.elapsed=max(0,min(TOTAL,self.elapsed+sec)); self.update_ui(force=True)

    def seek(self,slider,touch):
        if touch and slider.collide_point(*touch.pos):
            self.elapsed=slider.value; self.update_ui(force=True)

    def change_speed(self,*_):
        vals=[.5,1,1.5,2]; self.speed=vals[(vals.index(self.speed)+1)%len(vals)]
        self.speed_btn.text=f"Speed {self.speed:g}×"

    def show_scenes(self,*_):
        box=BoxLayout(orientation="vertical",padding=8,spacing=5)
        for i,(title,sub,start,end,lines) in enumerate(SCENES):
            b=Button(text=title+"\n"+sub,font_name=FONT,size_hint_y=None,height=58)
            b.bind(on_release=lambda btn,i=i:self.goto_scene(i))
            box.add_widget(b)
        p=Popup(title="Scene Navigator",content=box,size_hint=(.92,.85))
        p.open(); self.scene_popup=p

    def goto_scene(self,i):
        self.elapsed=SCENES[i][2]; self.update_ui(force=True)
        if hasattr(self,'scene_popup'): self.scene_popup.dismiss()

    def update_ui(self,force=False):
        self.slider.value=self.elapsed
        mm=int(self.elapsed//60); ss=int(self.elapsed%60)
        self.scene_label.text=f"গোঁফের জোরে রাজা   •   {mm:02d}:{ss:02d} / 10:00"
        for i,(_,sub,start,end,lines) in enumerate(SCENES):
            if start<=self.elapsed<end:
                if i!=self.scene_index or force:
                    self.scene_index=i
                li=0
                for j,(t,speaker,text) in enumerate(lines):
                    if self.elapsed>=t: li=j
                if li!=self.line_index or force:
                    self.line_index=li; self.speaker=speaker
                    self.dialogue.text=f"[b]{speaker}[/b]\n{text}"
                break

    def tick(self,dt):
        if self.playing:
            self.elapsed=min(TOTAL,self.elapsed+dt*self.speed)
            if self.elapsed>=TOTAL:self.playing=False
            self.update_ui()

class MainApp(App):
    title="গোঁফের জোরে রাজা"
    def build(self):
        self.sm=ScreenManager()
        self.sm.add_widget(MovieScreen(name="movie"))
        return self.sm
    def on_start(self):
        Clock.schedule_interval(self.sm.get_screen("movie").tick,1/30)
    def toggle_fullscreen(self):
        from kivy.core.window import Window
        Window.fullscreen = not Window.fullscreen

if __name__=="__main__":
    MainApp().run()
