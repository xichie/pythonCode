



def combine_files(inputpath : '输入路径', output_file : '输出文件名'):
    '''
        结果最终保存在当前目录下
    '''
    import os
    cur_dir = os.getcwd()
    output_dir = os.path.join(cur_dir, output_file)
    file_names = os.listdir(inputpath)

    for name in file_names:
        abs_dir = os.path.join(inputpath, name)
        if os.path.isdir(abs_dir):
            combine_files(abs_dir, output_file)
        else:
            f = open(abs_dir)
            out = open(output_dir, 'a+')
            for line in f.readlines():
                out.write(line)
            f.close()
            out.close()
                
if __name__ == "__main__":
    path = r"C:\Users\qjx\Desktop\Datasets_Healthy_Older_People"
    output_file = "1.txt"
    combine_files(path, output_file)    
