curl https://github.com/baiyecha/ippost/blob/master/ip \
    |grep -o -E '<td id="LC1" class="blob-code blob-code-inner js-file-line">(.+?)</td>' \
    |grep -o -E '([0-9]{1,3}[\.]){3}[0-9]{1,3}'
