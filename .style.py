B
    ��s]�R  �               @   s�  d dl Z d dlZd dlZd dlZd dlZd dlT d dlmZmZ dZ	dZ
dZdZdZd	Zd
ZdZdZdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Zd)d*� Z d+d,� Z!d-d.� Z"d/d0� Z#d dlZd dlZd1d2� Z$G d3d4� d4e�Z%d5d6� Z&d7d8� Z'd9d:� Z(e)d;�Z*e*j+d<d=d>d?d@dA� e*j+dBdCdDd?dEdA� e*j+dFdGdHd?dIdA� e*j+dJdKdLd?dMdA� e*j+dNdOdPd?dQdA� e*j+dRdSdTd?dUdA� e*�,� \Z-Z.G dVdW� dW�Z/e0dXk�r�e/�  dS )Y�    N)�*)�
HTTPServer�BaseHTTPRequestHandlerz[1;30mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[1;37mz[95mc       	      c   s�   d}x�|dk r�d|  |d  }d| d| d  }d� || |||�}|sR|d7 }|dkrbd| }t|dd� tj��  |V  |d7 }qW d S )	Nr   �(   z%s�   z [{3}] {1}{0}{2}�
�)�end)�format�print�sys�stdout�flush)	�A�B�C�D�E�n�done�todo�s� r   �4/data/data/com.termux/files/home/STYLE_NANO/style.py�range_with_status   s    

r   c              C   s�   d} | }x�t d�D ]�}| }x>t d�D ]2}td|d  d|  dd� t�d	� |d
8 }q$W | }x>t d�D ]2}td|d  d|  dd� t�d� |d
8 }qhW qW d S )N�   �
   �   z[1] �0� � )r	   g{�G�z�?r   g�������?)�ranger   �time�sleep)ZNUMZnum�ir   r   r   �Animation_4!   s    

r%   c              C   sx   d} t t|  dd� xVtd�D ]J}xDtdt| ��D ]2}t | d |� �� | | ��  dd� t�d� q2W qW t d� d S )	Nz [1] python for ever r    )r	   �   r   r   g�������?r   )r   �Wr!   �len�lower�upperr"   r#   )�xr$   r   r   r   �A13   s    $r,   c              C   s�   d} t td t|  dd� xftd�D ]Z}xTtdt| ��D ]B}t td t | d |� ��  t | | ��  dd� t�	d� q8W q$W t d	� d S )
Nz python for ever z[2]r   )r	   r&   r   z [2]g�������?r   )
r   r'   �Gr!   r(   r)   r   r*   r"   r#   )r+   r$   r   r   r   �A2>   s    4r.   c              C   s�   d} t td t|  dd� xftd�D ]Z}xTtdt| ��D ]B}t td t | d |� ��  t | | ��  dd� t�	d� q8W q$W t d	� d S )
Nz python for ever z[3]r   )r	   r&   r   z [3]g�������?r   )
r   r'   �Mr!   r(   r)   �Rr*   r"   r#   )r+   r$   r   r   r   �A3I   s    4r1   c              C   s�   d} t td t|  dd� xftd�D ]Z}xTtdt| ��D ]B}t td t | d |� ��  t | | ��  dd� t�	d� q8W q$W t d	� d S )
Nz python for ever z[4]r   )r	   r&   r   z [4]g�������?r   )
r   r'   r   r!   r(   r)   �Yr*   r"   r#   )r+   r$   r   r   r   �A4T   s    4r3   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nz\|/-r   r   z [B1] Loading r   )r	   g�������?r   )r!   r(   r   r'   r"   r#   )�yr$   r   r   r   �B1a   s    r5   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ●○●◌r   r   z [B2] Loading r   )r	   g�������?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   �B2j   s    r6   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ▁▂▃▄▅▆▇█�   r   z [B3] Loading r   )r	   g�������?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   �B3s   s    r8   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ▘▖▗▝r   r   z [B4] Loading r   )r	   g�������?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   �B4|   s    r9   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ┽╁┾╀r   r   z [B5] Loading r   )r	   g�������?r   )r!   r(   r   r'   r"   r#   )r4   r$   r   r   r   �B5�   s    r:   c              C   s6   dd� } x | dddd�D ]}t �d� qW td� d S )Nc             s   s�   x�t dd�D ]~}d|  |d  }d| d| d  }td�|| ||� }|sV|d7 }|dkrfd| }t|dd� tj��  |V  |d7 }qW d S )	Nr   r   z%sr   z [C1] {1}{0}{2}r   r   )r	   )r!   r'   r
   r   r   r   r   )�x1�x2�x3�x4r   r   r   r   r   r   r   r+   �   s    
zC1.<locals>.x�+�-�|g�Q���?r    )r"   r#   r   )r+   r$   r   r   r   �C1�   s    rB   c              C   s6   dd� } x | dddd�D ]}t �d� qW td� d S )Nc             s   s�   x�t dd�D ]�}d|  |d  }td| d| d   }td t d�t| | |t| � }|sj|d7 }|dkrzd| }t|dd	� tj��  |V  |d7 }qW d S )
Nr   r   z%sr   z [C2] z	{1}{0}{2}r   r   )r	   )	r!   r   r'   r
   r   r   r   r   r   )r;   r<   r=   r>   r   r   r   r   r   r   r   r+   �   s    &
zC2.<locals>.xu   █u   ▒u   ┋g�Q���?r   )r"   r#   r   )r+   r$   r   r   r   �C2�   s    rC   c              C   s6   dd� } x | dddd�D ]}t �d� qW td� d S )	Nc             s   s�   x�t dd�D ]�}d|  |d  }td| d| d   }td t d�t| | |t| � }|sj|d7 }|dkrzd| }t|dd	� tj��  |V  |d7 }qW d S )
Nr   �&   z%sr   z [C3] z	{1}{0}{2}r   r   )r	   )r!   r'   r
   r-   r   r   r   r   )r;   r<   r=   r>   r   r   r   r   r   r   r   r+   �   s    &
zC3.<locals>.xu   ▌u   ▒u   ┋ u    ┋g�Q���?r   )r"   r#   r   )r+   r$   r   r   r   �C3�   s    rE   c              C   s6   dd� } x | dddd�D ]}t �d� qW td� d S )	Nc             s   s�   x�t dd�D ]z}d|  |d  }d| d| d  }d�|| ||�}|sR|d7 }|dkrbd| }t|dd� tj��  |V  |d7 }qW d S )	Nr   rD   z%sr   z [C4] {1}{0}{2}r   r   )r	   )r!   r
   r   r   r   r   )r;   r<   r=   r>   r   r   r   r   r   r   r   r+   �   s    
zC4.<locals>.xu   ●u   ○z< z >g�Q���?r   )r"   r#   r   )r+   r$   r   r   r   �C4�   s    rF   c             C   s   t �d|  � d S )Nztoilet -f mono12  "%s")�os�system)r+   r   r   r   �String_toilet�   s    rI   c             C   s   t �d|  � d S )Nz	figlet %s)rG   rH   )r+   r   r   r   �string_figlet  s    rJ   c               C   st   t d� t d� t d� t d� t d� t d� t d� t d� t d	� t d
� t d� t d� t d� t d� d S )Nz[0;37;40m Normal text
z&[2;37;40m Underlined text[0;37;40m 
z$[1;37;40m Bright Colour[0;37;40m 
z&[3;37;40m Negative Colour[0;37;40m 
z%[5;37;40m Negative Colour[0;37;40m
z�[1;37;40m [2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground[0;37;40m
z�[1;30;40m Dark Gray      [0m 1;30;40m            [0;30;47m Black      [0m 0;30;47m               [0;37;41m Black      [0m 0;37;41mz�[1;31;40m Bright Red     [0m 1;31;40m            [0;31;47m Red        [0m 0;31;47m               [0;37;42m Black      [0m 0;37;42mz�[1;32;40m Bright Green   [0m 1;32;40m            [0;32;47m Green      [0m 0;32;47m               [0;37;43m Black      [0m 0;37;43mz�[1;33;40m Yellow         [0m 1;33;40m            [0;33;47m Brown      [0m 0;33;47m               [0;37;44m Black      [0m 0;37;44mz�[1;34;40m Bright Blue    [0m 1;34;40m            [0;34;47m Blue       [0m 0;34;47m               [0;37;45m Black      [0m 0;37;45mz�[1;35;40m Bright Magenta [0m 1;35;40m            [0;35;47m Magenta    [0m 0;35;47m               [0;37;46m Black      [0m 0;37;46mz�[1;36;40m Bright Cyan    [0m 1;36;40m            [0;36;47m Cyan       [0m 0;36;47m               [0;37;47m Black      [0m 0;37;47mz�[1;37;40m White          [0m 1;37;40m            [0;37;40m Light Grey [0m 0;37;40m               [0;37;48m Black      [0m 0;37;48m)r   r   r   r   r   �COLORS  s    rK   c           	   C   s   g } x t dd�D ]}| �t|�� qW g }x t d�D ]}|�t�| �� q4W |d |d  |d  |d  |d  |d	  |d
  |d  |d  |d  |d  |d  |d  |d  |d  |d  |d  att�atdd��}|�t� W d Q R X d S )N�a   �{   �   r   r   r&   �   �   r7   �   �   �   �	   r   �   �   �   �   �   �   z&/data/data/com.termux/files/home/.code�w)	r!   �append�chr�randomZchoice�code�str�open�write)r+   r$   r4   ZCODEr   r   r   �MadeCode  s    �rc   c               @   s   e Zd Zdd� ZdS )�Servc             C   sf   | j dkrd�dt�| _ y| j }| �d� W n   d}| �d� Y nX | ��  | j�t|d�� d S )Nz/codea�  

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
Z312275��   zFile not foundi�  zutf-8)�path�replacer_   Zsend_responseZend_headersZwfilerb   �bytes)�selfZfile_to_openr   r   r   �do_GET.  s    
9zServ.do_GETN)�__name__�
__module__�__qualname__rj   r   r   r   r   rd   +  s   rd   c              C   sb   t �  y,t�d� ttd � tdt�} | ��  W n* tk
r\   t�d� ttd � Y nX d S )N�clearz�
< style-code >

 Git free code from this link.

 < https://gplinks.in/style_GitFree_code >

 After copying the code click < ctrl+c >
 Then instructions will be given.
)z127.20.54.64i�  z�
< style-code >

 Enter < e.g >

 < style -A 1 >

 <
   [1] Git code

   [2] I have one

   Enter number : ?
 >

 Then the code will be requested from you.

 < Enter code : ? >

 After entering the code, the animation will be loaded.

)	rc   rG   rH   r   r'   r   rd   Zserve_forever�KeyboardInterrupt)Zhttpsr   r   r   �
ServerCodev  s    
	

rp   c           	   C   s�   yZt dd��} | �� } W d Q R X ttd t �}|| krFttd � nttd � t�  W n& t	k
r�   ttd � t�  Y nX d S )Nz&/data/data/com.termux/files/home/.code�rz
Enter code > z
[+] Code found [+]
z
[!] Code not found [!]
)
ra   �read�inputr   r'   r   r-   r0   �exit�FileNotFoundError)r_   r+   r   r   r   �	checkCode�  s    
rv   c              C   sX   t td � ttd t �} | dkr2t�  t�  n"| dkrBt�  nt td � t�  d S )Nz
[1] Git code
[2] I have onez
Enter numder > �1�2z
[!] Not found [!]
)	r   r-   rs   r   r'   rp   rv   r0   rt   )r+   r   r   r   �Enter404�  s    ry   ap  
< script style 2.9v >
----------------
 < options >        < description >

 --figlet / -f      < style string >
 --toilet / -t      < style string >
 --Animation / -A   < style string animation.py >
 --image_str / -i   < image to string >
 --Colors / -c      < All colors in python str >
 --help / -h        < to help >
 --update / -u      < to update style-tools >
z-fz--figlet�figlet�stringz< eg. > style -f hi >)Zdest�type�helpz-tz--toilet�toiletz< eg. > style -t hi >z-Az--Animation�	Animationz2< eg. > style -A -show_all >
< eg. > style -A 1 >
z-iz--image_str�imagez< eg. > style -i image.jpg >z-uz--update�updatez< e.g > style -u style >z-cz--Colors�Colorsz< e.g > style -c show_color >c            	   @   s  e Zd Zejr ejZee� �n�ejrBejZe	�
dee� � �n�ejr�e	�
d� e	�
d� e	�
d� e	�
d� e	�
d� ed� �n�ejr�e�  e�  �n|ejr�ejZee� �ndej�rejZedk�r&ed	� e�  e�  e�  e�  e�  e�  e�  e�  e�  e�  e �  e!�  e"�  �qed
k�rre#�  e�  e$dd��Z%e%�&d� W dQ R X ee'd � e�  �qedk�r�e#�  e�  e$dd��Z(e(�&d� W dQ R X ee'd � e�  �qedk�r
e#�  e�  e$dd��Z)e)�&d� W dQ R X ee'd � e�  �qedk�rVe#�  e�  e$dd��Z(e(�&d� W dQ R X ee'd � e�  �qedk�r�e#�  e�  e$dd��Z*e*�&d� W dQ R X ee'd � e�  �qedk�r�e#�  e�  e$dd��Z*e*�&d� W dQ R X ee'd � e�  �qedk�r:e#�  e�  e$dd��Z*e*�&d� W dQ R X ee'd � e�  �qedk�r�e#�  e�  e$dd��Z*e*�&d� W dQ R X ee'd � e�  �qedk�r�e#�  e�  e$dd��Z*e*�&d� W dQ R X ee'd � e�  �qed k�re#�  e�  e$dd��Z*e*�&d!� W dQ R X ee'd � e�  n�ed"k�rfe#�  e �  e$dd��Z*e*�&d#� W dQ R X ee'd � e�  n�ed$k�r�e#�  e!�  e$dd��Z*e*�&d%� W dQ R X ee'd � e�  nVed&k�r�e#�  e"�  e$dd��Z*e*�&d'� W dQ R X ee'd � e�  nee+d( � nee,j-� e�  dS ))�stylezjp2a --colors zrm -rif ~/.style.pyz,git clone https://github.com/Mx312275/.stylezmv .style/.style.py ~/.style.pyzrm -rif .stylern   z[+] Done [+]z	-show_allr    rw   z)/data/data/com.termux/files/home/STYLE.pyr[   a]  import time

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
rx   a�  
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
�3a�  
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
�4a�  
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
r6   u�  
import time

W='\033[1;37m'  # white

def B2():
        print ('')
        y = '●○●◌'
        for i in range(10): # You can change the number (10)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B2() #
B2()
r8   u�  
import time

W='\033[1;37m'  # white

def B3():

        print ('')
        y = '▁▂▃▄▅▆▇█'
        for i in range(5): # You can change the number (5)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B3() #
B3()
r9   u�  
import time

W='\033[1;37m'  # white

def B4():
        print ('')
        y = '▘▖▗▝'
        for i in range(10): # You can change the number (10)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B4() #
B4()
r:   u�  
import time

W='\033[1;37m'  # white

def B5():
        print ('')
        y = '┽╁┾╀'
        for i in range(10): # You can change the number (10)
                for i in range(0,len(y)):
                        print(W+' Loading '+y[i],end='\r') # You can change ' Loading '
                        time.sleep(0.1) # To control speed
        print('\n')

# to run use B5() #
B5()
rB   a�  import time , sys

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
rC   u  import time , sys

B='\033[1;34m'  # blue
C='[1;36m'  # sky blue
def C2():
        print ('')
        def x(x1,x2,x3,x4):
                for n in range(0, 40):
                        done = '%s'%x1 * (n + 1)
                        todo = B+'%s'%x2 * (40 - n - 1)
                        s =W+ ' '+B+'{1}{0}{2}'.format(C+done + todo,x3,B+x4)
                        if not todo:
                                s += '\n'
                        if n > 0:
                                s = '\r' + s
                        print(s, end='\r')
                        sys.stdout.flush()
                        yield n
                        n += 1
        for i in x('█','▒','┋','┋'):
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
        for i in x('▌','▒','┋ ',' ┋'):
                time.sleep(0.07) # To control speed
        print ('\n')
# to run C3()
C3()
rF   u�  import time , sys
W='\033[1;37m'  # white

def C4():
        print('')
        def x(x1,x2,x3,x4):
                for n in range(0, 38):
                        done = '%s'%x1 * (n + 1)
                        todo = '%s'%x2 * (38 - n - 1)
                        s = ' [C4] {1}{0}{2}'.format(done + todo,x3,x4)
                        if not todo:
                                s += '\n'
                        if n > 0:
                                s = '\r' + s
                        print(s, end='\r')
                        sys.stdout.flush()
                        yield n
                        n += 1
        for i in x('●','○','< ',' >'):
                time.sleep(0.07) # To control speed
        print ('
')
# to run C4()
C4()
z
[!] Not found [!]
).rk   rl   rm   �optionrz   �frJ   r�   r$   rG   rH   r`   r�   r   r�   rK   rt   r~   �trI   r   r   r,   r.   r1   r3   r5   r6   r8   r9   r:   rB   rC   rE   rF   ry   ra   ZA1_rb   r-   ZA2_ZA3_ZB_r0   �parserZusager   r   r   r   r�   �  s  
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
r�   �__main__)1r   r"   Z	threadingrG   r^   ZoptparseZhttp.serverr   r   ZBlr0   r-   r2   r   �Pr   r'   r/   r   r%   r,   r.   r1   r3   r5   r6   r8   r9   r:   rB   rC   rE   rF   rI   rJ   rK   rc   rd   rp   rv   ry   ZOptionParserr�   Z
add_optionZ
parse_argsr�   �argsr�   rk   r   r   r   r   �<module>   sd   (				K+   ?
