from Song import Sound
import warnings
from pydub.playback import play
from playsound import playsound
warnings.filterwarnings("ignore")


def initiate_of_shift():
    print(f'The program converts two audio files (of the wav type into a single file)\n')
    '''

    #For tests
    type = 'wav'
    name1 = "C:\\Users\\Valentin\\Music\\1"
    name2 = 'C:\\Users\\Valentin\\Music\\2'
    end_name = 'C:\\Users\\Valentin\\Music\\prop'
    start_time1 = 0
    start_time2 = 0
    end_time1=3
    end_time2=3
    '''

    print(f'Enter the path (without type) to the first audio file:')
    name1 = input()
    print(f'Enter the start time of the first file:')
    start_time1 = input()
    print(f'Enter the end time of the first file:')
    end_time1 = input()

    print(f'Enter the path (without type) to the second audio file:')
    name2 = input()
    print(f'Enter the start time of the second file:')
    start_time2 = input()
    print(f'Enter the end time of the second file:')
    end_time2 = input()

    print(f'Enter the name(endpath/name) (without type) of the finished file:')
    end_name = input()

    type = 'wav'

    file1 = Sound(name1+'.'+type, start_time1, end_time1)
    file2 = Sound(name2+'.'+type, start_time2, end_time2)

    end_file = file1 + file2
    end_file.export(end_name+".wav", format='wav')
    print(f'The final file is located at: ' + end_name+".wav")

    print('Do you wanna play it? (Yes/No)')
    a = input()
    if(a=="Yes"):
        """
        print("Enter your file path: ")
        b = input()
        """
        print(" ♫•*¨*•.¸¸♪ (^_^♪) ")
        playsound(end_name+".wav")
    if(a == "No"):
        print("ЪуЪ  ((╬◣﹏◢╬))  ЪуЪ")
if __name__ == '__main__':
    initiate_of_shift()


