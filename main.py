
from Song import Sound

def initiate_of_shift():
    print(f'The program converts two audio files (of the same type into a single file)\n')
    print(f'Enter the file type:')
    type = input()
    print(f'Enter the path to the first audio file:')
    name1 = input()
    print(f'Enter the start time of the first file:')
    start_time1 = input()
    print(f'Enter the end time of the first file:')
    end_time1 = input()

    print(f'Enter the path to the first audio file:')
    name2 = input()
    print(f'Enter the start time of the first file:')
    start_time2 = input()
    print(f'Enter the end time of the first file:')
    end_time2 = input()

    print(f'Enter the name(endpath/name) (without type) of the finished file:')
    end_name = input()

    file1 = Sound(name1, start_time1, end_time1)
    file2 = Sound(name2, start_time2, end_time2)

    end_file = file1 + file2
    end_file.export(end_name+"."+type, format=type)
    print(f'The final file is located at: ' + end_name+"."+type)

if __name__ == '__main__':
    initiate_of_shift()


