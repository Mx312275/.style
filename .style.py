B
    [Kr]-  �               @   sr  d dl Z d dlZd dlZd dlZd dlT dZdZdZdZdZ	dZ
d	Zd
ZdZdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zd d!� Zd"d#� Zd$d%� Zd&d'� Zd(d)� Zed*�Zejd+d,d-d.d/d0� ejd1d2d3d.d4d0� ejd5d6d7d.d8d0� ejd9d:d;d.d<d0� ejd=d>d?d.d@d0� ejdAdBdCd.dDd0� e� � \Z!Z"G dEdF� dF�Z#e$dGk�rne#�  dS )H�    N)�*z[1;30mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[1;37mz[95mc       	      c   s�   d}x�|dk r�d|  |d  }d| d| d  }d� || |||�}|sR|d7 }|dkrbd| }t|dd� tj��  |V  |d7 }qW d S )	Nr   �(   z%s�   z [{3}] {1}{0}{2}�
�)�end)�format�print�sys�stdout�flush)	�A�B�C�D�E�nZdoneZtodo�s� r   �4/data/data/com.termux/files/home/STYLE_NANO/style.py�range_with_status   s    

r   c              C   s�   d} | }x�t d�D ]�}| }x>t d�D ]2}td|d  d|  dd� t�d	� |d
8 }q$W | }x>t d�D ]2}td|d  d|  dd� t�d� |d
8 }qhW qW d S )N�   �
   �   z[1] �0� � )r   g{�G�z�?r   g�������?)�ranger	   �time�sleep)ZNUMZnum�ir   r   r   �Animation_4    s    

r!   c              C   sx   d} t t|  dd� xVtd�D ]J}xDtdt| ��D ]2}t | d |� �� | | ��  dd� t�d� q2W qW t d� d S )	Nz [1] python for ever r   )r   �   r   r   g�������?r   )r	   �Wr   �len�lower�upperr   r   )�xr    r   r   r   �A12   s    $r(   c              C   s�   d} t td t|  dd� xftd�D ]Z}xTtdt| ��D ]B}t td t | d |� ��  t | | ��  dd� t�	d� q8W q$W t d	� d S )
Nz python for ever z[2]r   )r   r"   r   z [2]g�������?r   )
r	   r#   �Gr   r$   r%   r   r&   r   r   )r'   r    r   r   r   �A2=   s    4r*   c              C   s�   d} t td t|  dd� xftd�D ]Z}xTtdt| ��D ]B}t td t | d |� ��  t | | ��  dd� t�	d� q8W q$W t d	� d S )
Nz python for ever z[3]r   )r   r"   r   z [3]g�������?r   )
r	   r#   �Mr   r$   r%   �Rr&   r   r   )r'   r    r   r   r   �A3H   s    4r-   c              C   s�   d} t td t|  dd� xftd�D ]Z}xTtdt| ��D ]B}t td t | d |� ��  t | | ��  dd� t�	d� q8W q$W t d	� d S )
Nz python for ever z[4]r   )r   r"   r   z [4]g�������?r   )
r	   r#   r   r   r$   r%   �Yr&   r   r   )r'   r    r   r   r   �A4S   s    4r/   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nz\|/-r   r   z [B1] r   )r   g�������?r   )r   r$   r	   r#   r   r   )�yr    r   r   r   �B1`   s    r1   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ●○●◌r   r   z [B2] r   )r   g�������?r   )r   r$   r	   r#   r   r   )r0   r    r   r   r   �B2i   s    r2   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ▁▂▃▄▅▆▇█�   r   z [B3] r   )r   g�������?r   )r   r$   r	   r#   r   r   )r0   r    r   r   r   �B3r   s    r4   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ▘▖▗▝r   r   z [B4] r   )r   g�������?r   )r   r$   r	   r#   r   r   )r0   r    r   r   r   �B4{   s    r5   c              C   s\   d} xJt d�D ]>}x8t dt| ��D ]&}ttd | |  dd� t�d� q"W qW td� d S )	Nu   ┽╁┾╀r   r   z [B5] r   )r   g�������?r   )r   r$   r	   r#   r   r   )r0   r    r   r   r   �B5�   s    r6   c             C   s   t �d|  � d S )Nztoilet -f mono12  "%s")�os�system)r'   r   r   r   �String_toilet�   s    r9   c             C   s   t �d|  � d S )Nz	figlet %s)r7   r8   )r'   r   r   r   �string_figlet�   s    r:   c             C   s   t �d|  � d S )Nzjp2a %s)r7   r8   )r'   r   r   r   �image_style�   s    r;   c               C   st   t d� t d� t d� t d� t d� t d� t d� t d� t d	� t d
� t d� t d� t d� t d� d S )Nz[0;37;40m Normal text
z&[2;37;40m Underlined text[0;37;40m 
z$[1;37;40m Bright Colour[0;37;40m 
z&[3;37;40m Negative Colour[0;37;40m 
z%[5;37;40m Negative Colour[0;37;40m
z�[1;37;40m [2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground[0;37;40m
z�[1;30;40m Dark Gray      [0m 1;30;40m            [0;30;47m Black      [0m 0;30;47m               [0;37;41m Black      [0m 0;37;41mz�[1;31;40m Bright Red     [0m 1;31;40m            [0;31;47m Red        [0m 0;31;47m               [0;37;42m Black      [0m 0;37;42mz�[1;32;40m Bright Green   [0m 1;32;40m            [0;32;47m Green      [0m 0;32;47m               [0;37;43m Black      [0m 0;37;43mz�[1;33;40m Yellow         [0m 1;33;40m            [0;33;47m Brown      [0m 0;33;47m               [0;37;44m Black      [0m 0;37;44mz�[1;34;40m Bright Blue    [0m 1;34;40m            [0;34;47m Blue       [0m 0;34;47m               [0;37;45m Black      [0m 0;37;45mz�[1;35;40m Bright Magenta [0m 1;35;40m            [0;35;47m Magenta    [0m 0;35;47m               [0;37;46m Black      [0m 0;37;46mz�[1;36;40m Bright Cyan    [0m 1;36;40m            [0;36;47m Cyan       [0m 0;36;47m               [0;37;47m Black      [0m 0;37;47mz�[1;37;40m White          [0m 1;37;40m            [0;37;40m Light Grey [0m 0;37;40m               [0;37;48m Black      [0m 0;37;48m)r	   r   r   r   r   �COLORS�   s    r<   ap  
< script style 2.1v >
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
z-iz--image_str�imagez< eg. > style -i image.jpg >z-uz--update�updatez< e.g > style -u style >z-cz--Colors�Colorsz< e.g > style -c show_color >c            	   @   sL  e Zd Zejr ejZee� �n(ejr8ejZe	e� �nej
r�ej
Zedkr�ed� e�  e�  e�  e�  e�  e�  e�  e�  e�  ed� n2edkr�dZedd��Ze�e� W dQ R X e�  n�ejr�ejZee� njej�r"e� d� e� d	� e� d
� e� d� e� d� ed� n&ej!�r8e"�  e�  nee#j$� e�  dS )�stylez	-show_allr   �1a�  
import time

def Upper_string():

        x = '  python for ever ' # You can put any text here

        print (x,end='\r')

        for i in range(2): # Here is the number of repeating animated text


                for i in range (0,len(x)):
                        print (x[:i].lower()+x[i].upper(),end='\r')

                        time.sleep(0.1) # Here determines your time
        print('\n')

# < run > #
# ------- #

Upper_string()

# ------------- #

zSTYLE.py�wNzrm -rif ~/.style.pyz,git clone https://github.com/Mx312275/.stylezmv .style/.style.py ~/.style.pyzrm -rif .style�clearz[+] Done [+])%�__name__�
__module__�__qualname__�optionr=   �fr:   rA   �tr9   rB   r   r	   r(   r*   r-   r/   r1   r2   r4   r5   r6   Z	Style_txt�openZremove_code�write�exitrC   r    r;   rD   r7   r8   rE   r<   �parserZusager   r   r   r   rF   �   sP   








rF   �__main__)%r
   r   Z	threadingr7   ZoptparseZBlr,   r)   r.   r   �Pr   r#   r+   r   r!   r(   r*   r-   r/   r1   r2   r4   r5   r6   r9   r:   r;   r<   ZOptionParserrS   Z
add_optionZ
parse_argsrM   �argsrF   rJ   r   r   r   r   �<module>   sJ    					X
