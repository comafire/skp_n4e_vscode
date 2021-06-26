from invoke import task
import os, sys, re, time
import skp_env, skp_util

@task
def install(c):
    skp_util.mkdir_usr(c, f"{skp_env.VSCODE_HOME}")
    if skp_util.is_macos(c):
        # 아래 에러 방지를 위해 readlink 가 gnu readlink 를 사용하도록 coreutils 설치 및 링크 수정

        # readlink: illegal option -- f
        # usage: readlink [-n] [file ...]

        # > brew install coreutils
        # > ln -s "$(which greadlink)" "$(dirname "$(which greadlink)")/readlink" 

        # 아래 에러 방지를 위해 icu4c 설치

        # dyld: Library not loaded: /usr/local/opt/icu4c/lib/libicui18n.66.dylib
        # Referenced from: /Users/comafire/LocalDrive/skp/usr/code-server-3.3.1-macos-amd64/bin/../lib/node
        # Reason: image not found

        # > brew install icu4c
        cmd = "brew update"
        skp_util.run_with_exit(c, cmd)
        cmd = "brew install coreutils"
        skp_util.run_with_exit(c, cmd)
        path_readlink = "/usr/local/bin/readlink"
        if not os.path.isfile(path_readlink):
            cmd = 'ln -s "$(which greadlink)" "$(dirname "$(which greadlink)")/readlink"'
            skp_util.run_with_exit(c, cmd)
        cmd = "brew install icu4c"
        skp_util.run_with_exit(c, cmd)
        url = f"https://github.com/cdr/code-server/releases/download/v{skp_env.VSCODE_VER}/code-server-{skp_env.VSCODE_VER}-macos-amd64.tar.gz"
        fname = url.split('/')[-1]
        cmd = f"wget -q {url} -O {skp_env.VSCODE_HOME}/usr/{fname}" # 출력이 길다면, -q 옵션 사용 가능
        skp_util.run_with_exit(c, cmd)
        cmd = f"cd {skp_env.VSCODE_HOME}/usr && rm -rf ./code-server && mkdir ./code-server && tar -zxf {fname} -C code-server --strip-components=1"
        skp_util.run_with_exit(c, cmd)        
    if skp_util.is_ubuntu(c):
        url = f"https://github.com/cdr/code-server/releases/download/v{skp_env.VSCODE_VER}/code-server-{skp_env.VSCODE_VER}-linux-amd64.tar.gz"
        fname = url.split('/')[-1]
        cmd = f"wget -q {url} -O {skp_env.VSCODE_HOME}/usr/{fname}" # 출력이 길다면, -q 옵션 사용 가능
        skp_util.run_with_exit(c, cmd)
        cmd = f"cd {skp_env.VSCODE_HOME}/usr && rm -rf ./code-server && mkdir ./code-server && tar -zxf {fname} -C code-server --strip-components=1"
        skp_util.run_with_exit(c, cmd)        

@task
def start(c):
    cmd = f"envsubst < {skp_env.VSCODE_HOME}/etc/pm2.json | pm2 start -"
    skp_util.run_with_exit(c, cmd)

@task
def stop(c):
    cmd = f"envsubst < {skp_env.VSCODE_HOME}/etc/pm2.json | pm2 stop -"
    skp_util.run_with_exit(c, cmd)
    cmd = f"envsubst < {skp_env.VSCODE_HOME}/etc/pm2.json | pm2 delete -"
    skp_util.run_with_exit(c, cmd)


@task
def restart(c):
    stop(c)
    time.sleep(3)
    start(c)
