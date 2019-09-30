import os

os.chdir(r'C:\Users\FH\Music\VipSongsDownload')
print(os.getcwd())

file_list = os.listdir(os.getcwd())
for file_name in file_list:
    if file_name[-4:] == 'qmc3':
        print('原始文件名：', file_name)
        name = file_name[:-4] + '.mp3'
        print('更新文件名：', name)
        os.rename(file_name, name)
        print('完成！！！')
		