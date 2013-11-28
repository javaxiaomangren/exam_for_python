import os
import crypt


def create_user(name, username, password):
    encPass = crypt.crypt(password, "22")
    cmd = """sudo useradd -p %s -s /bin/bash -d /home/%s -m -c "%s" %s"""
    return os.system(cmd % (encPass, username, name, username))

create_user("test", "test_yang2", "windy")
