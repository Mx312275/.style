B
    Ú+u]£W  ã               @   s  d dl Z d dlZd dlZd dlZd dlZd dlT d dlmZmZ dZ	dZ
dZdZdZd	Zd
ZdZdZdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd  Zd!d" Zd#d$ Zd%d& Zd'd( Zd)d* Z d+d, Z!d-d. Z"d/d0 Z#d dlZd dlZd1d2 Z$G d3d4 d4eZ%d5d6 Z&d7d8 Z'd9d: Z(e)d; *d<e¡ *d=e
¡ *d$e¡ *d>e¡Z+e+j,d?d@dAdBdCdD e+j,dEdFdGdBdHdD e+j,dIdJdKdBdLdD e+j,dMdNdOdBdPdD e+j,dQdRdSdBdTdD e+j,dUdVdWdBdXdD e+ -¡ \Z.Z/G dYdZ dZZ0e1d[krþe0  dS )\é    N)Ú*)Ú
HTTPServerÚBaseHTTPRequestHandlerz[1;30mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[1;37mz[95mc       	      c   s   d}x|dk rd|  |d  }d| d| d  }d  || |||¡}|sR|d7 }|dkrbd| }t|dd tj ¡  |V  |d7 }qW d S )	Nr   é(   z%sé   z [{3}] {1}{0}{2}Ú
ú)Úend)ÚformatÚprintÚsysÚstdoutÚflush)	ÚAÚBÚCÚDÚEÚnÚdoneÚtodoÚs© r   ú4/data/data/com.termux/files/home/STYLE_NANO/style.pyÚrange_with_status   s    

r   c              C   s¦   d} | }xt dD ]}| }x>t dD ]2}td|d  d|  dd t d	¡ |d
8 }q$W | }x>t dD ]2}td|d  d|  dd t d¡ |d
8 }qhW qW d S )Né   é
   é   z[1] Ú0ú Ú )r	   g{®Gáz?r   g©?)Úranger   ÚtimeÚsleep)ZNUMZnumÚir   r   r   ÚAnimation_4!   s    

r%   c              C   sx   d} t t|  dd xVtdD ]J}xDtdt| D ]2}t | d |  ¡ | |  ¡  dd t d¡ q2W qW t d d S )	Nz [1] python for ever r    )r	   é   r   r   gÉ?r   )r   ÚWr!   ÚlenÚlowerÚupperr"   r#   )Úxr$   r   r   r   ÚA13   s    $r,   c              C   s   d} t td t|  dd xftdD ]Z}xTtdt| D ]B}t td t | d |  ¡  t | |  ¡  dd t 	d¡ q8W q$W t d	 d S )
Nz python for ever z[2]r   )r	   r&   r   z [2]gÉ?r   )
r   r'   ÚGr!   r(   r)   r   r*   r"   r#   )r+   r$   r   r   r   ÚA2>   s    4r.   c              C   s   d} t td t|  dd xftdD ]Z}xTtdt| D ]B}t td t | d |  ¡  t | |  ¡  dd t 	d¡ q8W q$W t d	 d S )
Nz python for ever z[3]r   )r	   r&   r   z [3]gÉ?r   )
r   r'   ÚMr!   r(   r)   ÚRr*   r"   r#   )r+   r$   r   r   r   ÚA3I   s    4r1   c              C   s   d} t td t|  dd xftdD ]Z}xTtdt| D ]B}t td t | d |  ¡  t | |  ¡  dd t 	d¡ q8W q$W t d	 d S )
Nz python for ever z[4]r   )r	   r&   r   z [4]gÉ?r   )
r   r'   r   r!   r(   r)   ÚYr*   r"   r#   )r+   r$   r   r   r   ÚA4T   s    4r3   c              C   s\   d} xJt dD ]>}x8t dt| D ]&}ttd | |  dd t d¡ q"W qW td d S )	Nz\|/-r   r   z [B1] Loading r   )r	   g¹?r   )r!   r(   r   r'   r"   r#   )Úyr$   r   r   r   ÚB1a   s    r5   c              C   s\   d} xJt dD ]>}x8t dt| D ]&}ttd | |  dd t d¡ q"W qW td d S )	Nu   ââââr   r   z [B2] Loading r   )r	   g¹?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   ÚB2j   s    r6   c              C   s\   d} xJt dD ]>}x8t dt| D ]&}ttd | |  dd t d¡ q"W qW td d S )	Nu   ââââââââé   r   z [B3] Loading r   )r	   g¹?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   ÚB3s   s    r8   c              C   s\   d} xJt dD ]>}x8t dt| D ]&}ttd | |  dd t d¡ q"W qW td d S )	Nu   ââââr   r   z [B4] Loading r   )r	   g¹?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   ÚB4|   s    r9   c              C   s\   d} xJt dD ]>}x8t dt| D ]&}ttd | |  dd t d¡ q"W qW td d S )	Nu   â½ââ¾âr   r   z [B5] Loading r   )r	   g¹?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   ÚB5   s    r:   c              C   s6   dd } x | ddddD ]}t  d¡ qW td d S )Nc             s   s   xt ddD ]~}d|  |d  }d| d| d  }td || ||¡ }|sV|d7 }|dkrfd| }t|dd tj ¡  |V  |d7 }qW d S )	Nr   r   z%sr   z [C1] {1}{0}{2}r   r   )r	   )r!   r'   r
   r   r   r   r   )Úx1Úx2Úx3Úx4r   r   r   r   r   r   r   r+      s    
zC1.<locals>.xú+ú-ú|gìQ¸ë±?r    )r"   r#   r   )r+   r$   r   r   r   ÚC1   s    rB   c              C   s6   dd } x | ddddD ]}t  d¡ qW td d S )Nc             s   s¦   x t ddD ]}d|  |d  }td| d| d   }td t d t| | |t| ¡ }|sj|d7 }|dkrzd| }t|dd	 tj ¡  |V  |d7 }qW d S )
Nr   r   z%sr   z [C2] z	{1}{0}{2}r   r   )r	   )	r!   r   r'   r
   r   r   r   r   r   )r;   r<   r=   r>   r   r   r   r   r   r   r   r+   ³   s    &
zC2.<locals>.xu   âu   âu   âgìQ¸ë±?r   )r"   r#   r   )r+   r$   r   r   r   ÚC2²   s    rC   c              C   s6   dd } x | ddddD ]}t  d¡ qW td d S )	Nc             s   s¦   x t ddD ]}d|  |d  }td| d| d   }td t d t| | |t| ¡ }|sj|d7 }|dkrzd| }t|dd	 tj ¡  |V  |d7 }qW d S )
Nr   é&   z%sr   z [C3] z	{1}{0}{2}r   r   )r	   )r!   r'   r
   r-   r   r   r   r   )r;   r<   r=   r>   r   r   r   r   r   r   r   r+   Î   s    &
zC3.<locals>.xu   âu   âu   â u    âgìQ¸ë±?r   )r"   r#   r   )r+   r$   r   r   r   ÚC3Í   s    rE   c              C   s6   dd } x | ddddD ]}t  d¡ qW td d S )	Nc             s   s   xt ddD ]~}d|  |d  }d| d| d  }td || ||¡ }|sV|d7 }|dkrfd| }t|dd tj ¡  |V  |d7 }qW d S )	Nr   rD   z%sr   z [C4] {1}{0}{2}r   r   )r	   )r!   r'   r
   r   r   r   r   )r;   r<   r=   r>   r   r   r   r   r   r   r   r+   é   s    
zC4.<locals>.xu   âu   âz< z >gìQ¸ë±?r    )r"   r#   r   )r+   r$   r   r   r   ÚC4è   s    rF   c             C   s   t  d|  ¡ d S )Nztoilet -f mono12  "%s")ÚosÚsystem)r+   r   r   r   ÚString_toiletþ   s    rI   c             C   s   t  d|  ¡ d S )Nz	figlet %s)rG   rH   )r+   r   r   r   Ústring_figlet  s    rJ   c               C   st   t d t d t d t d t d t d t d t d t d	 t d
 t d t d t d t d d S )Nz[0;37;40m Normal text
z&[2;37;40m Underlined text[0;37;40m 
z$[1;37;40m Bright Colour[0;37;40m 
z&[3;37;40m Negative Colour[0;37;40m 
z%[5;37;40m Negative Colour[0;37;40m
z[1;37;40m [2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground[0;37;40m
z[1;30;40m Dark Gray      [0m 1;30;40m            [0;30;47m Black      [0m 0;30;47m               [0;37;41m Black      [0m 0;37;41mz[1;31;40m Bright Red     [0m 1;31;40m            [0;31;47m Red        [0m 0;31;47m               [0;37;42m Black      [0m 0;37;42mz[1;32;40m Bright Green   [0m 1;32;40m            [0;32;47m Green      [0m 0;32;47m               [0;37;43m Black      [0m 0;37;43mz[1;33;40m Yellow         [0m 1;33;40m            [0;33;47m Brown      [0m 0;33;47m               [0;37;44m Black      [0m 0;37;44mz[1;34;40m Bright Blue    [0m 1;34;40m            [0;34;47m Blue       [0m 0;34;47m               [0;37;45m Black      [0m 0;37;45mz[1;35;40m Bright Magenta [0m 1;35;40m            [0;35;47m Magenta    [0m 0;35;47m               [0;37;46m Black      [0m 0;37;46mz[1;36;40m Bright Cyan    [0m 1;36;40m            [0;36;47m Cyan       [0m 0;36;47m               [0;37;47m Black      [0m 0;37;47mz[1;37;40m White          [0m 1;37;40m            [0;37;40m Light Grey [0m 0;37;40m               [0;37;48m Black      [0m 0;37;48m)r   r   r   r   r   ÚCOLORS  s    rK   c           	   C   s   g } x t ddD ]}|  t|¡ qW g }x t dD ]}| t | ¡¡ q4W |d |d  |d  |d  |d  |d	  |d
  |d  |d  |d  |d  |d  |d  |d  |d  |d  |d  attatdd}| t¡ W d Q R X d S )Néa   é{   é   r   r   r&   é   é   r7   é   é   é   é	   r   é   é   é   é   é   é   z&/data/data/com.termux/files/home/.codeÚw)	r!   ÚappendÚchrÚrandomZchoiceÚcodeÚstrÚopenÚwrite)r+   r$   r4   ZCODEr   r   r   ÚMadeCode  s    rc   c               @   s   e Zd Zdd ZdS )ÚServc             C   sf   | j dkrd dt¡| _ y| j }|  d¡ W n   d}|  d¡ Y nX |  ¡  | j t|d¡ d S )Nz/codea  

<!DOCTYPE html>
<html>
<head>
	<title>style-code</title>
</head>
<body>


<center>
	<h1 id="text" cols="50" rows="1"> 312275  </h1><br>
	<button onclick="copy()">Copy</button><br>
</center>
<script type="text/javascript">
	function copy(){
		var text = document.getElementById('text');
		var range = document.createRange();

		range.selectNode(text);
		window.getSelection().addRange(range);
		document.execCommand('copy');

	}
</script>
<style type="text/css">

body{
  min-height: 100vh;
  background-image: linear-gradient(120deg,#3498db,#8e44ad);
}

button{
  display: black;
  width: 100%;
  height: 50px;
  border: none;
  background: linear-gradient(120deg,#3498db,#8e44ad,#3498db);
  background-size: 200%;
  color: #fff;
  outline: none;
  cursor: pointer;
  transition: .5s;

}

center{

  position: absolute;
  left: 50%;top: 50%;
  transform: translate(-50%,-50%);
}

</style>
</body>
</html>
Z312275éÈ   zFile not foundi  zutf-8)ÚpathÚreplacer_   Zsend_responseZend_headersZwfilerb   Úbytes)ÚselfZfile_to_openr   r   r   Údo_GET.  s    
9zServ.do_GETN)Ú__name__Ú
__module__Ú__qualname__rj   r   r   r   r   rd   +  s   rd   c           	   C   s   t   yLt d¡ ttd dt¡ dt¡ dt¡ dt¡  t	dt
} |  ¡  W nB tk
r   t d¡ ttd dt¡ dt¡ dt¡  Y nX d S )	NÚclearu  
 W1< R1style-codeW1 >
                               ââââ
             ââ                ââââ
 ââââââââ  âââââââ   âââ  âââ    ââ       ââââââ
 ââââââ â    ââ       âââ ââ     ââ      ââââââââ
  âââââââ    ââ        âââââ     ââ      ââââââââ
 ââââââââ    âââââ      âââ      âââââ   ââââââââ
  ââââââ      ââââ      ââ        ââââ     âââââ
                      âââ

      | G1Git free code from this link W1|

 [ C1C1https://gplinks.in/style_GitFree_code W1]R1

 After copying the code click W1< C1ctrl+c W1>

ÚG1ÚR1rB   ÚW1)z127.20.54.64i´  u»  
W1< R1style-check code W1>
                               ââââ
             ââ                ââââ
 ââââââââ  âââââââ   âââ  âââ    ââ       ââââââ
 ââââââ â    ââ       âââ ââ     ââ      ââââââââ
  âââââââ    ââ        âââââ     ââ      ââââââââ
 ââââââââ    âââââ      âââ      âââââ   ââââââââ
  ââââââ      ââââ      ââ        ââââ     âââââ
                      âââ

 R1< C1Please place the code you copied R1>
)rc   rG   rH   r   r'   rg   r-   r0   r   r   rd   Zserve_foreverÚKeyboardInterrupt)Zhttpsr   r   r   Ú
ServerCodev  s    
(

rs   c           	   C   s   ylt dd} |  ¡ } W d Q R X ttd t }| dd¡| krXttd  t 	d¡ ntt
d  t  W n& tk
r   tt
d  t  Y nX d S )	Nz&/data/data/com.termux/files/home/.codeÚrzEnter code > r   r    z
[+] Code found [+]
zrm -rif ~/.codez
[!] Code not found [!]
)ra   ÚreadÚinputr   r'   rg   r   r-   rG   rH   r0   Ú	checkCodeÚFileNotFoundErrorÚexit)r_   r+   r   r   r   rw      s    

rw   c               C   s   t   t  d S )N)rs   rw   r   r   r   r   ÚFreeCode_Server³  s    rz   a¨  
W1< R1script style G13.5v W1>
W1  -----------------

 < G1optionsW1 >        W1<G1 descriptionW1 >

 --figlet / C1-fW1      < style string >
 --toilet / C1-tW1      < style string >
 --Animation / C1-AW1   < style string animation.py >
 --image_str / C1-iW1   < image to string >
 --Colors / C1-cW1      < All colors in python str >
 --help / C1-hW1        < to help >
 --update / C1-u W1     < G1to update style-tools W1>
ro   rp   rq   z-fz--figletÚfigletÚstringz< eg. > style -f hi >)ZdestÚtypeÚhelpz-tz--toiletÚtoiletz< eg. > style -t hi >z-Az--AnimationÚ	Animationz2< eg. > style -A -show_all >
< eg. > style -A 1 >
z-iz--image_strÚimagez< eg. > style -i image.jpg >z-uz--updateÚupdatez< e.g > style -u style >z-cz--ColorsÚColorsz< e.g > style -c show_color >c            	   @   s  e Zd Zejr ejZee nøejrBejZe	 
dee ¡ nÖejre	 
d¡ e	 
d¡ e	 
d¡ e	 
d¡ e	 
d¡ ed nejre  e  n|ejr´ejZee ndejrejZedkr&ed	 e  e  e  e  e  e  e  e  e  e  e   e!  e"  qed
krre#  e  e$ddZ%e% &d¡ W dQ R X ee'd  e  qedkr¾e#  e  e$ddZ(e( &d¡ W dQ R X ee'd  e  qedkr
e#  e  e$ddZ)e) &d¡ W dQ R X ee'd  e  qedkrVe#  e  e$ddZ(e( &d¡ W dQ R X ee'd  e  qedkr¢e#  e  e$ddZ*e* &d¡ W dQ R X ee'd  e  qedkrîe#  e  e$ddZ*e* &d¡ W dQ R X ee'd  e  qedkr:e#  e  e$ddZ*e* &d¡ W dQ R X ee'd  e  qedkre#  e  e$ddZ*e* &d¡ W dQ R X ee'd  e  qedkrÒe#  e  e$ddZ*e* &d¡ W dQ R X ee'd  e  qed kre#  e  e$ddZ*e* &d!¡ W dQ R X ee'd  e  nêed"krfe#  e   e$ddZ*e* &d#¡ W dQ R X ee'd  e  n ed$kr°e#  e!  e$ddZ*e* &d%¡ W dQ R X ee'd  e  nVed&krúe#  e"  e$ddZ*e* &d'¡ W dQ R X ee'd  e  nee+d(  nee,j- e  dS ))Ústylezjp2a --colors zrm -rif ~/.style.pyz,git clone https://github.com/Mx312275/.stylezmv .style/.style.py ~/.style.pyzrm -rif .stylern   z[+] Done [+]z	-show_allr    Ú1z)/data/data/com.termux/files/home/STYLE.pyr[   a]  import time

W='\033[1;37m'  # white

def A1():
  print('')
  x =' python for ever ' # You can enter any text
  print (W+x,end='')

  for i in range(2): # You can change the number (2)
    for i in range (0,len(x)):

      print (x[:i].lower()+x[i].upper(),end='\r')
      time.sleep(0.2) # To control speed

  print('\n')

# to run use A1() #

A1()Nz$
 File save in [ home as STYLE.py ]
Ú2aÇ  
import time

G='\033[1;32m'  # green
B='\033[1;34m'  # blue

def A2():
        print ('')
        x =' python for ever ' # You can enter any text
        print (G+x,end='\r')
        for i in range(2): # You can change the number (2)
                for i in range (0,len(x)):
                        print (G+x[:i].lower()+B+x[i].upper(),end='\r')
                        time.sleep(0.2) # To control speed
        print('\n')

# to run use A2() #
A2()
Ú3a·  
import time

M = '[95m'
R='[1;31m'  # red

def A3():
        print ('')
        x =' python for ever ' # You can enter any text
        print (M+x,end='\r')
        for i in range(2): # You can change the number (2)
                for i in range (0,len(x)):
                        print (M+x[:i].lower()+R+x[i].upper(),end='\r')
                        time.sleep(0.2) # To control speed
        print('\n')

# to run use A3() #
A3()
Ú4aÎ  
import time

C='\033[1;36m'  # light blue
Y='\033[1;33m'  # yallow

def A4():
        print ('')
        x =' python for ever ' # You can enter any text
        print (C+x,end='\r')
        for i in range(2): # You can change the number (2)
                for i in range (0,len(x)):
                        print (C+x[:i].lower()+Y+x[i].upper(),end='\r')
                        time.sleep(0.2) # To control speed
        print('\n')

# to run use A4() #
A4()
r5   a  
import time

W='\033[1;37m'  # white

def B1():
        print ('')
        y = '\|/-'
        for i in range(10): # You can change the number (10)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B1() #
B1()
r6   u  
import time

W='\033[1;37m'  # white

def B2():
        print ('')
        y = 'ââââ'
        for i in range(10): # You can change the number (10)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B2() #
B2()
r8   u  
import time

W='\033[1;37m'  # white

def B3():

        print ('')
        y = 'ââââââââ'
        for i in range(5): # You can change the number (5)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B3() #
B3()
r9   u  
import time

W='\033[1;37m'  # white

def B4():
        print ('')
        y = 'ââââ'
        for i in range(10): # You can change the number (10)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B4() #
B4()
r:   u  
import time

W='\033[1;37m'  # white

def B5():
        print ('')
        y = 'â½ââ¾â'
        for i in range(10): # You can change the number (10)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B5() #
B5()
rB   aê  import time , sys

W='\033[1;37m'  # white

def C1():
        print('')
        def x(x1,x2,x3,x4):
                for n in range(0, 40):
                        done = '%s'%x1 * (n + 1)
                        todo = '%s'%x2 * (40 - n - 1)
                        s = W+' {1}{0}{2}'.format(done + todo,x3,x4)
                        if not todo:
                                s += '\n'
                        if n > 0:
                                s = '\r' + s
                        print(s, end='\r')
                        sys.stdout.flush()
                        yield n
                        n += 1
        for i in x('+','-','|','|'):
                time.sleep(0.07) # To control speed
        print ('')

# to run C1()
C1()
rC   u  import time , sys

B='\033[1;34m'  # blue
C='[1;36m'  # sky blue
def C2():
        print ('')
        def x(x1,x2,x3,x4):
                for n in range(0, 40):
                        done = '%s'%x1 * (n + 1)
                        todo = B+'%s'%x2 * (40 - n - 1)
                        s = B+' {1}{0}{2}'.format(C+done + todo,x3,B+x4)
                        if not todo:
                                s += '\n'
                        if n > 0:
                                s = '\r' + s
                        print(s, end='\r')
                        sys.stdout.flush()
                        yield n
                        n += 1
        for i in x('â','â','â','â'):
                time.sleep(0.07) # To control speed
        print ('\n')
# to run C2()
C2()
rE   u  import time , sys
W='\033[1;37m'  # white
G='\033[1;32m'  # green
def C3():
        print('')
        def x(x1,x2,x3,x4):
                for n in range(0, 38):
                        done = '%s'%x1 * (n + 1)
                        todo = W+'%s'%x2 * (38 - n - 1)
                        s = W+' '+W+'{1}{0}{2}'.format(G+done + todo,x3,W+x4)
                        if not todo:
                                s += '\n'
                        if n > 0:
                                s = '\r' + s
                        print(s, end='\r')
                        sys.stdout.flush()
                        yield n
                        n += 1
        for i in x('â','â','â ',' â'):
                time.sleep(0.07) # To control speed
        print ('\n')
# to run C3()
C3()
rF   uî  import time , sys
W='\033[1;37m'  # white

def C4():
        print('')
        def x(x1,x2,x3,x4):
                for n in range(0, 38):
                        done = '%s'%x1 * (n + 1)
                        todo = '%s'%x2 * (38 - n - 1)
                        s = W+' {1}{0}{2}'.format(done + todo,x3,x4)
                        if not todo:
                                s += '\n'
                        if n > 0:
                                s = '\r' + s
                        print(s, end='\r')
                        sys.stdout.flush()
                        yield n
                        n += 1
        for i in x('â','â','< ',' >'):
                time.sleep(0.07) # To control speed
        print ('')
# to run C4()
C4()
z
[!] Not found [!]
).rk   rl   rm   Úoptionr{   ÚfrJ   r   r$   rG   rH   r`   r   r   r   rK   ry   r   ÚtrI   r   r   r,   r.   r1   r3   r5   r6   r8   r9   r:   rB   rC   rE   rF   rz   ra   ZA1_rb   r-   ZA2_ZA3_ZB_r0   ÚparserZusager   r   r   r   r   Ö  s  






























r   Ú__main__)2r   r"   Z	threadingrG   r^   ZoptparseZhttp.serverr   r   ZBlr0   r-   r2   r   ÚPr   r'   r/   r   r%   r,   r.   r1   r3   r5   r6   r8   r9   r:   rB   rC   rE   rF   rI   rJ   rK   rc   rd   rs   rw   rz   ZOptionParserrg   r   Z
add_optionZ
parse_argsr   Úargsr   rk   r   r   r   r   Ú<module>   sd   (				K*&   ?
