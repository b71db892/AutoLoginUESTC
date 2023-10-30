# 不在同一个文件夹下 不设置起始地址的时候需要在代码更换地址
# $job = Start-Job -ScriptBlock {cd C:\path-to-AutoLoginUESTC-main; python login_once.py}
$job = Start-Job -ScriptBlock {python login_once.py}

Wait-Job $job

# 不需要日志可以注释这两行
$TimeLog = (Get-Date).toString("yyyy/MM/dd HH:mm:ss")
"${TimeLog} `n $(Receive-Job $job)`n`n" >> auto-login-log.txt

Remove-Job $job