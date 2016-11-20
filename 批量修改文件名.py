# 下载的字幕文件名和视频文件名不一致 播放时要手动加载字幕
# (坚持各种重复操作能使用程序自动化就交个程序处理的原则)
# 使用此程序将字幕重命名 与视频一致

import  os
import  shutil

def rename():
    count=0;
    mainpath="E:\\迅雷下载\\The.Big.Bang.Theory.S03.720p.BluRay.x264-SiNNERS";
    mainfiles=os.listdir(mainpath);
    assfiles=os.listdir(mainpath+"\\143730926419240");
    for file in mainfiles:
        filePath=os.path.join(mainpath,file);#拼接文件的完整路径
        if os.path.isdir(filePath) or os.path.splitext(file)[1] !='.mkv' :
            continue;
        assFilePath=os.path.join(mainpath+"\\143730926419240",assfiles[count]);
        fileType=os.path.splitext(assFilePath)[1];
        if os.path.isdir(assFilePath) or fileType!='.ass':
            continue;
        fileName = os.path.splitext(file)[0];
        Newdir=os.path.join(mainpath,fileName+fileType)#新的目标文件名 包括绝对地址
        shutil.copyfile(assFilePath,Newdir)#复制文件 并且重命名
      #  os.rename("oldname", "newname") 重命名
        count+=1
rename()