B
    �Nq]  �               @   s  d dl Z d dlZd dlZd dlZd dlT dZdZdZdZdZ	dZ
d	Zd
Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zed�Zejdddddd� ejd d!d"dd#d� ejd$d%ddd&d� ejd'd(d)dd*d� ejd+d,d-dd.d� e�� \ZZG d/d0� d0�Zed1k�re�  dS )2�    N)�*z[1;30mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[1;37mc              C   st   d} t | dd� xVtd�D ]J}xDtdt| ��D ]2}t | d |� �� | | ��  dd� t�d� q.W qW t d� d S )Nz [1]  python for ever �)�end�   r   g�������?�
)�print�range�len�lower�upper�time�sleep)�x�i� r   �4/data/data/com.termux/files/home/STYLE_NANO/style.py�Upper_string   s    $r   c              C   sX   d} xFt d�D ]:}x4t dt| ��D ]"}td| |  dd� t�d� q"W qW td� d S )	Nz\|/-�
   r   z [2]   r   )r   g�������?r   )r   r	   r   r   r   )�yr   r   r   r   �	Animation   s    r   c       	      c   s�   d}x�|dk r�d|  |d  }d| d| d  }d� || |||�}|sR|d7 }|dkrbd| }t|dd� tj��  |V  |d7 }qW d S )	Nr   �(   z%s�   z [{3}] {1}{0}{2}r   r   )r   )�formatr   �sys�stdout�flush)	�A�B�C�D�E�nZdoneZtodo�sr   r   r   �range_with_status"   s    

r#   c              C   s�   d} | }x�t d�D ]�}| }x>t d�D ]2}td|d  d|  dd� t�d	� |d
8 }q$W | }x>t d�D ]2}td|d  d|  dd� t�d� |d
8 }qhW qW d S )N�   r   �   z[1] �0� � )r   g{�G�z�?r   g�������?)r   r   r   r   )ZNUMZnumr   r   r   r   �Animation_42   s    

r)   c             C   s   t �d|  � d S )Nztoilet -f mono12  "%s")�os�system)r   r   r   r   �String_toiletB   s    r,   c             C   s   t �d|  � d S )Nz	figlet %s)r*   r+   )r   r   r   r   �string_figletF   s    r-   c             C   s   t �d|  � d S )Nzjp2a %s)r*   r+   )r   r   r   r   �image_styleJ   s    r.   a:  
< script style >
----------------
 < options >        < description >

 --figlet / -f      < style string >
 --toilet / -t      < style string >
 --Animation / -A   < style string animation.py >
 --image_str / -i   < image to string >
 --help / -h        < to help >
 --update / -u      < to update style-tools >
z-fz--figlet�figlet�stringz< eg. > style -f hi >)Zdest�type�helpz-tz--toilet�toiletz< eg. > style -t hi >z-Az--Animationz< eg. > style -show_all>z-iz--image_str�imagez< eg. > style -i image.jpg >z-uz--update�updatez< e.g > style -u style >c            	   @   s�  e Zd Zejr ejZee� �njejr8ejZe	e� �nRej
�rej
Zedkr�ed� e�  e
�  x"eddddd�D ]Ze�d� qtW ed� x"edd	d
d
d�D ]Ze�d� q�W ed� x"eddddd�D ]Ze�d� q�W ed� n4edk�r�dZedd��Ze�e� W dQ R X e�  nlej�r6ejZee� nTej�rze�d� e�d� e�d� e�d� e�d� ed� neej� e�  dS )�stylez	-show_allr(   �#�-�|�3g�������?u   ▐u   ▒u   ┋�4u   ●u   ◌u   ᎒�5�1a�  
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

zSTYLE.py�wNzrm -rif ~/.style.pyz,git clone https://github.com/Mx312275/.stylezmv .style/.style.py ~/.style.pyzrm -rif .style�clearz[+] Done [+])�__name__�
__module__�__qualname__�optionr/   �fr-   r3   �tr,   r   r   r   r   r#   r   r   r   Z	Style_txt�openZremove_code�write�exitr4   r.   r5   r*   r+   �parserZusager   r   r   r   r6   h   sL   









r6   �__main__)r   r   Z	threadingr*   ZoptparseZBl�R�G�Yr   �Pr   �Wr   r   r#   r)   r,   r-   r.   ZOptionParserrI   Z
add_optionZ
parse_argsrC   �argsr6   r@   r   r   r   r   �<module>   s6    
	V
