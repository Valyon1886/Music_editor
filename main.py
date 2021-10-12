
from Song import Sound

def initiate_of_shift():
    print(f'The program converts two audio files (of the wav type into a single file)\n')
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
    '''
    type = 'wav'
    name1 = r"C:\Users\Valentin\Music\1"
    name2 = r'\Users\Valentin\Music\2'
    end_name = r'\Users\Valentin\Music\3'
    start_time1 = 1
    start_time2 = 2
    end_time1=4
    end_time2=5

    file1 = Sound(name1+'.'+type, start_time1, end_time1)
    file2 = Sound(name2+'.'+type, start_time2, end_time2)

    end_file = file1 + file2
    end_file.export(end_name+".wav", format='wav')
    print(f'The final file is located at: ' + end_name+".wav")

if __name__ == '__main__':
    initiate_of_shift()


