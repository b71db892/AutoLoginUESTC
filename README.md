# UESTC 电子科技大学网络认证脚本
------------------------------
### 搞这干啥？
- 学校的电信宽带自动掉线太频繁了，移动的稍好一点但也不行（尊贵的移动还屏蔽了游戏串流软件，真是谢谢你）
- 校园网很稳定，很少掉线。但是如果再出现封在家里一个月没法回学校的情况，那就得想办法让电脑一直在线了，不然没法给老板打工。
### 怎么用？
- 支持登录以下类型的网络（我都试过的）：
```angular2html
- 校园网有线接入+学号认证（在主楼做的测试，至今可用）
- 移动、电信寝室宽带有线接入+学号认证（类似于硕丰6、7、8组团那种插网线直接弹出认证页面的，至今可用）
```
只需修改config.py就行。然后手动注销断网，输入：
```angular2html
python login_once.py
```
如果能联网，那说明配置没问题。
之后一直运行always_online.py就行了。
```angular2html
python always_online.py
```
- docker-compose部署方法：
```bash
echo "version: '3.4'
services:
  stash:
    image: alexandersande/network-login:latest
    container_name: nwlogin
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-file: "10"
        max-size: "2m"
    environment:
      # 你的学号
      - LOGIN_ID=11111111111111
      # 信息门户密码
      - LOGIN_PASSWORD=114514
      # 寝室公寓=3 主楼有线校园网=1
      - LOCATION=3
      # 电信:"dx", 移动:"cmcc", 校园网:"dx-uestc"
      - SERVICE_PROVIDER=cmcc
      # Ping的IP地址
      - PINGIP=114.114.114.114" > docker-compose.yaml
docker-compose up -d
```

### 抄的！抄的！抄的！
- 楼主入学的时候深澜软件的网络认证页面已经经过混淆了，还好GitHub有大佬之前写好的登录流程相关代码。
所以就完全照着抄了这个https://github.com/coffeehat/BIT-srun-login-script
- 好多学校都是这套登录逻辑，所以GitHub脚本很多，上边这个链接里也有支持openwrt的go版本。
