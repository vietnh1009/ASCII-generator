# 错误1
## 运行`img2img`出现以下错误
相应类似错误出现在`img2img_color.py`、`video2video.py`、`video2video_color.py`中。
```
Traceback (most recent call last):
  File "E:\Git\ASCII-generator\img2img.py", line 67, in <module>
    main(opt)
  File "E:\Git\ASCII-generator\img2img.py", line 29, in main
    char_list, font, sample_character, scale = get_data(opt.language, opt.mode)
                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\Git\ASCII-generator\utils.py", line 117, in get_data
    char_list = sort_chars(char_list, font, language)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\Git\ASCII-generator\utils.py", line 13, in sort_chars
    char_width, char_height = font.getsize("A")
                              ^^^^^^^^^^^^
AttributeError: 'FreeTypeFont' object has no attribute 'getsize'
```

## 解决方式
主要是因为用的 Pillow 版本已经弃用了 FreeTypeFont.getsize() 方法，为了实现不同版本的通用性（兼容旧版本和新版本的 Pillow），
增加以下方法，修改`utils.py`、`img2img.py`、`img2img_color.py`、`video2video.py`、`video2video_color.py`

```
def get_char_size(font, char):
    if hasattr(font, "getsize"):#用于检查对象是否具有某个属性或方法
        return font.getsize(char)  # 旧版本 Pillow
    else:
        bbox = font.getbbox(char)  # 新版本 Pillow
        return bbox[2] - bbox[0], bbox[3] - bbox[1]
```

# 错误2
## 运行`video2video.py`出现以下错误
```
SyntaxWarning: invalid escape sequence '\|'
  CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
```
## 解决方式
主要原因是反斜杠\的特殊性，`\|`被认为是一个转义字符，但是实际上不存在该转义字符。
两种方式，直接再添加一个反斜杠，即`\\|`，或者在字符串前面添加一个`r`，即
```
CHAR_LIST = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
```

# 错误3
## 运行`video2video.py`出现以下错误
```
OpenCV: FFMPEG: tag 0x44495658/'XVID' is not supported with codec id 12 and format 'mp4 / MP4 (MPEG-4 Part 14)'
OpenCV: FFMPEG: fallback to use tag 0x7634706d/'mp4v'
```
## 解决办法
使用 OpenCV 和 FFMPEG 进行视频编码时，遇到了格式兼容性问题。
OpenCV 默认使用的编码器 XVID 与 .mp4 格式不兼容，因此 FFMPEG 会回退到另一个编码器 mp4v。
使用 mp4v编解码器（'mp4v'）来确保 .mp4 格式的兼容性
```
out = cv2.VideoWriter(opt.output, cv2.VideoWriter_fourcc(*"mp4v"), fps,
                                  ((out_image.shape[1], out_image.shape[0])))
```