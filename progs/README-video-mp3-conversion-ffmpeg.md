# Video / Audio Conversion

FFMPEG for the win!

## `.mkv` to `.mp3`

With terminal location in same dir as `input.mkv`:

`ffmpeg -i input.mkv -c:a libmp3lame output.mp3`

Works!

## Batch

https://stackoverflow.com/questions/5784661/how-do-you-convert-an-entire-directory-with-ffmpeg

```
for i in *.{mkv,mp4}(.N); do ffmpeg -i "$i" -c:a libmp3lame "${i%.*}.mp3"; done
```

To copy directly from our cloud directory to our eshkol repo directory:

```
\
BOOKNAME='23-yeshayahu'; \
echo "/Users/nikos/repos/eshkol-ampelon/tanach/audio/$BOOKNAME/${i%.*}.mp3" \

for i in *.{mkv,mp4}(.N); do ffmpeg -i "$i" -c:a libmp3lame "/Users/nikos/repos/eshkol-ampelon/tanach/audio/$BOOKNAME/${i%.*}.mp3"; done
```


## Loop problems

```
for i in *.mp4(.N) *.mkv(.N) *.txt(.N) *.md(.N); do echo "cool: $i"; done
```

(KEY was `(.N)` part! was failing otherwise... is STUPID that is needed nonetheless...)

https://stackoverflow.com/a/14505622/264031

