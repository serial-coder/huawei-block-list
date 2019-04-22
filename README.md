# huawei-block-list

- [huawei-block-list](#huawei-block-list)
  - [Description](#description)
  - [Setup Blocking](#setup-blocking)
    - [Setup Blocking with Algo VPN](#setup-blocking-with-algo-vpn)
    - [Setup Blocking with OpenDNS](#setup-blocking-with-opendns)
  - [Details](#details)
    - [Version of ROM](#version-of-rom)
    - [Pre-installed Appllications](#pre-installed-appllications)
    - [Configuration of Huawei-related Applications](#configuration-of-huawei-related-applications)
    - [Network Configuration](#network-configuration)
    - [Usage Behaviors](#usage-behaviors)
  - [Timeline](#timeline)

## Description

<p align="center"><img src ="img/dnsmasq.jpg" /></p>

Domain names on `master.txt` are captured DNS requests from Huawei P30 Pro purchased in Thailand. All domains located in China and/or has an IP address within China's ASN. The device hasn't configured with Huawei services, including Huawei ID or any Hi services.

Please note that:
- The block list may includes test domain names, `baidu.com` and `qq.com`.
- By relying on techniques in `update.py` to verify location domain names. Some domain names such as `tencent-cloud.net` and `hwcdn.net` are not flagged. I will find a way to fix this issue later.

## Setup Blocking

### Setup Blocking with Algo VPN

1. Setup [Algo VPN](https://github.com/trailofbits/algo) and enable adblocking feature on both server and client-side
2. Update `/usr/local/sbin/adblock.sh` to include [the raw version of block list](https://raw.githubusercontent.com/pe3zx/huawei-block-list/master/master.txt). The block list should be appended to `BLOCKLIST_URLS` variable.

```sh
awk '{gsub(/"$/,"https://raw.githubusercontent.com/pe3zx/huawei-block-list/master/master.txt \"")}' /usr/local/sbin/adblock.sh
```

3. Execute `/usr/local/sbin/adblock.sh` to apply new block list to dnsmasq. The script will be automatically executed by cron to pull and apply any updates.

```sh
sh /usr/local/sbin/adblock.sh
```

### Setup Blocking with OpenDNS

If you don't have your own server or don't want to mess with configuration stuff, you can get [a free OpenDNS account](https://www.opendns.com/home-internet-security/) which you can create up to 25 domains to block. However, OpenDNS doesn't support leading dot domain like `.cn`. I recommend to add each domain which has only ccTLD, and add something like `gov.cn` or `com.cn` to make you life easier.

<p align="center"><img src ="img/opendns.png" /></p>

## Details

### Version of ROM

- Android 9
- EMUI 9.1.0 (Build number 9.1.0.124)
- Vendor country info
  - Vendor: HW
  - Country: spcseas

### Pre-installed Appllications

There are consumer applications already installed on the device, including Uber, Facebook and SwiftKey, but I can't remember all of it. System-related and utilities are listing below, except `com.android.*` and `com.google.*`.

- com.hicloud.android.clone
- com.hisi.mapcon
- com.huawei.HwMultiScreenShot
- com.huawei.KoBackup
- com.huawei.android.FloatTasks
- com.huawei.android.chr
- com.huawei.android.dsdscardmanager
- com.huawei.android.hsf
- com.huawei.android.hwaps
- com.huawei.android.hwouc
- com.huawei.android.instantonline
- com.huawei.android.instantshare
- com.huawei.android.internal.app
- com.huawei.android.karaoke
- com.huawei.android.launcher
- com.huawei.android.mirrorshare
- com.huawei.android.projectmenu
- com.huawei.android.pushagent
- com.huawei.android.remotecontroller
- com.huawei.android.thememanager
- com.huawei.android.wfdft
- com.huawei.androidx
- com.huawei.aod
- com.huawei.appmarket
- com.huawei.arengine.service
- com.huawei.autoinstallapkfrommcc
- com.huawei.bd
- com.huawei.bluetooth
- com.huawei.browser
- com.huawei.camera
- com.huawei.contacts.sync
- com.huawei.contactscamcard
- com.huawei.desktop.explorer
- com.huawei.desktop.systemui
- com.huawei.featurelayer.featureframework
- com.huawei.featurelayer.sharedfeature.map
- com.huawei.fido.uafclient
- com.huawei.gameassistant
- com.huawei.hiaction
- com.huawei.hiai
- com.huawei.hicard
- com.huawei.hidisk
- com.huawei.hifolder
- com.huawei.himovie.overseas
- com.huawei.hitouch
- com.huawei.hiview
- com.huawei.hiviewtunnel
- com.huawei.hwasm
- com.huawei.hwdetectrepair
- com.huawei.hwid
- com.huawei.hwstartupguide
- com.huawei.iaware
- com.huawei.iconnect
- com.huawei.imedia.dolby
- com.huawei.ims
- com.huawei.intelligent
- com.huawei.languagedownloader
- com.huawei.lbs
- com.huawei.livewallpaper.paradise
- com.huawei.mmitest
- com.huawei.motionservice
- com.huawei.msdp
- com.huawei.nb.service
- com.huawei.nearby
- com.huawei.numberidentity
- com.huawei.omacp
- com.huawei.parentcontrol
- com.huawei.pcassistant
- com.huawei.phoneservice
- com.huawei.powergenie
- com.huawei.printservice
- com.huawei.recsys
- com.huawei.scanner
- com.huawei.screenrecorder
- com.huawei.search
- com.huawei.securitymgr
- com.huawei.synergy
- com.huawei.systemmanager
- com.huawei.systemserver
- com.huawei.tips
- com.huawei.tmecustomize
- com.huawei.trustagent
- com.huawei.vassistant
- com.huawei.videoeditor
- com.huawei.wifieapsimplmn
- com.huawei.wifiprobqeservice
- com.ironsource.appcloud.oobe.huawei
- com.qeexo.smartshot
- com.swiftkey.swiftkeyconfigurator
- com.touchtype.swiftkey

### Configuration of Huawei-related Applications

The following list are "Do not accept to share information" applications. These applications still showing a privacy notice to me or still need my permission to access system components:

- AppGallery
- AppAssistant
- HUAWEI Themes
- HUAWEI Browser
- HiCare
- Recorder
- Backup
- PhoneClone

The following features are disabled:

- Huawei Share
- HiTouch

### Network Configuration

Cellular network from one of top three mobile operators in Thailand. Always connecting to personal VPN deployed on Amazon EC2 instance in Asia Pacific region. The VPN I used is [Algo from trailofbits](https://github.com/trailofbits/algo) with a local DNS server (dnsmasq), connect via [WireGuard](https://www.wireguard.com/).

### Usage Behaviors

Mostly like every normal users do. Brought back to Songkran Festival to try one of the best camera phones in the world. Listening to Blackpink's new album. Reading articles. Tweeting.

## Timeline

- **April 22, 2019**: Received a message from Huawei Thailand for supporting. They will try to coordinate with Huawei HQ.